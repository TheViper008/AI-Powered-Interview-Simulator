from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
import os
import json
from .gemini_helper import topicListPrompt, askGemini, feedbackPrompt, questions_schema, feedback_schema, companySpecificPrompt, JdPrompt
from .whisper_helper import transcribeAudio
from docx import Document
import PyPDF2
from simulator.confidence_model.classify import classify_audio


def selectInterview(request):
  return render(request=request, template_name="select_interview.html")


def topics(request):
  if request.method == "POST":
    clear_audio_uploads()
    topicList = request.POST.get("topicList", [])
    number_of_questions = request.POST.get("number_of_questions", 5)
    prompt = topicListPrompt.format(number_of_questions, topicList)
    list_of_questions = askGemini(prompt, questions_schema)
    print("*" * 10)
    print(prompt)
    print("*" * 10)
    print("*" * 10)
    print(list_of_questions)
    print("*" * 10)
    request.session["questions"] = list_of_questions
    request.session["number_of_questions"] = len(list_of_questions)
    return redirect("/interview")
  

def throughJD(request):
    if request.method == "POST":
        clear_audio_uploads()
        jdFile = request.FILES.get("jd")
        number_of_questions = request.POST.get("number_of_questions", 5)
        file_content = ""

        if jdFile:
            file_name = jdFile.name
            file_extension = os.path.splitext(file_name)[1].lower()
            
            if file_extension == ".txt":
                # Read file content directly
                file_content = jdFile.read().decode('utf-8')

            elif file_extension == ".docx":
                # Read docx file
                doc = Document(jdFile)  # Pass file object directly
                text = [p.text for p in doc.paragraphs]
                file_content = "\n".join(text)

            elif file_extension == ".pdf":
                # Read PDF file
                reader = PyPDF2.PdfReader(jdFile)  # Pass file object directly
                text = [page.extract_text() for page in reader.pages if page.extract_text()]
                file_content = "\n".join(text)

            else:
                raise TypeError("Invalid file type")

        prompt = JdPrompt.format(number_of_questions, file_content)
        list_of_questions = askGemini(prompt, questions_schema)
        request.session["questions"] = list_of_questions
        request.session["number_of_questions"] = len(list_of_questions)
        return redirect("/interview")

    

def companySpec(request):
    if request.method == "POST":
        clear_audio_uploads()
        companyName = request.POST.get("companyName")
        companyRole = request.POST.get("companyRole")
        number_of_questions = request.POST.get("number_of_questions", 5)
        prompt = companySpecificPrompt.format(number_of_questions, companyName, companyRole)
        list_of_questions = askGemini(prompt, questions_schema)
        request.session["questions"] = list_of_questions
        request.session["number_of_questions"] = len(list_of_questions)
        return redirect("/interview")

        
  

def interview_questions(request):
  questions = request.session.get("questions")
  return render(request, 'questions_test.html', {'questions': json.dumps(questions)})

@csrf_exempt
def audio_upload(request):
    if request.method == "POST" and request.FILES:
        files = request.FILES
        saved_files = []

        for key, audio_file in files.items():
            file_path = os.path.join( 'audio_uploads', audio_file.name)

            if default_storage.exists(file_path):
                    default_storage.delete(file_path)

            saved_path = default_storage.save(file_path, ContentFile(audio_file.read()))
            saved_files.append(saved_path)
            print(saved_files)

        return JsonResponse({
            'message': 'Audio files uploaded successfully!',
            'files': saved_files,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


import os

def feedback(request):
    answers = {}
    audio_files = []

    number_of_questions = request.session.get("number_of_questions")
    questions = request.session.get("questions")

    for i in range(number_of_questions):
        file_path = os.path.join('media', 'audio_uploads', f"question_{i + 1}.wav")

        if os.path.exists(file_path):
            transcribedText = transcribeAudio(filepath=file_path)
            answers[questions[i]] = transcribedText
            audio_files.append(file_path)
        else:
            answers[questions[i]] = "(Skipped)"
            audio_files.append(None)  # Placeholder to keep index alignment

    prompt = feedbackPrompt.format(answers)
    response = askGemini(prompt, feedback_schema)

    for i, answer_feedback in enumerate(response):
        if audio_files[i] is not None:
            answer_feedback["audio_confidence"] = classify_audio(audio_files[i])
        else:
            answer_feedback["audio_confidence"] = "N/A (Skipped)"

    return render(request, "feedback.html", {"feedback": response})
import glob
def clear_audio_uploads():
    audio_folder = os.path.join('media', 'audio_uploads')  # Or fix path here
    audio_files = glob.glob(os.path.join(audio_folder, '*.wav'))
    print(f"Clearing {len(audio_files)} audio files...")
    for file in audio_files:
        try:
            os.remove(file)
            print(f"Deleted {file}")
        except Exception as e:
            print(f"Error deleting {file}: {e}")



def home(request):
    return render(request, 'home.html')
  