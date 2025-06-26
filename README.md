---

# AI-Powered Interview Simulator 🎤🤖

An AI-driven virtual interview simulation platform that helps users prepare for interviews with personalized, real-time feedback on **grammar**, **confidence**, and **content accuracy**.

## 🔍 Project Overview

The AI-Powered Interview Simulator is designed to offer users a realistic, voice-based mock interview experience. Users can select topics, job roles, or input job descriptions, and the system dynamically generates relevant interview questions. Users respond using voice, and their answers are evaluated for key aspects like:

- **Speech confidence** (using Wav2Vec & emotion recognition)
- **Grammar and language quality** (via Gemini API)

The platform provides a detailed feedback report to help users identify their strengths and improve weak areas—boosting their confidence and interview readiness.

---

## ⚙️ Key Features

- 🎯 **Topic-Based Practice**: Users can choose specific domains (e.g., HR, Technical, Behavioral) or upload job descriptions.
- 🎙️ **Voice-Based Responses**: Simulates real interview scenarios using voice input.
- 📝 **Real-Time Transcription**: Uses **Whisper** for accurate speech-to-text conversion.
- 🔍 **Confidence & Emotion Analysis**: Leverages **Wav2Vec** and **Speech Emotion Recognition (SER)** models.
- ✍️ **Grammar & Clarity Feedback**: Utilizes **Gemini** to provide corrections and suggestions.
- 📊 **Performance Scoring**: Generates comprehensive reports with scores and improvement tips.

---

## 🧠 Technologies Used

- **Python**, **Django** – Backend framework
- **JavaScript**, **Bootstrap** – Frontend
- **OpenAI Whisper** – Speech-to-text transcription
- **Google’s Wav2Vec** – Speech analysis and emotion/confidence detection
- **Gemini API** – NLP, grammar analysis, content feedback
- **Media Recorder API** – Audio capture from user

---

## 🚀 How It Works

1. User selects an interview type or inputs job description.
2. Gemini API generates a customized set of questions.
3. User records audio responses using the web interface.
4. Audio is transcribed using Whisper and analyzed.
5. Feedback is generated on:
   - Grammar & structure
   - Confidence levels
   - Relevance & accuracy
6. Users receive a final report with scores and suggestions.

---

## 💻 How to Run the Application

Follow these steps to set up and run the project locally:

### 1. Clone the Repository

```bash
git clone https://github.com/TheViper008/AI-Powered-Interview-Simulator.git
cd AI-Powered-Interview-Simulator
```

### 2. (Optional) Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
python manage.py runserver
```

Then open your browser and go to:

```
http://127.0.0.1:8000/
```

---

## 📌 Notes

* ✅ Make sure your system has a working **microphone** for voice input.
* 🌐 An **internet connection** is required for API-based features like Gemini or cloud Whisper.
* 🧠 Ensure **Whisper**, **Wav2Vec**, and other models are properly configured if running locally.

---

## 📂 Dataset Sources

* **[LJ Speech Dataset](https://www.kaggle.com/datasets/mathurinache/the-lj-speech-dataset)** – For training speech-to-text models.
* **[Voice-Based Confidence Recognizer](https://www.kaggle.com/datasets/swarupakulkarni/voice-based-confidence-recognizer)** – For training emotion/confidence recognition.

---

## 🎓 Academic Context

This project was developed as part of the final-year engineering curriculum at **CMR Institute of Technology** under the **Visvesvaraya Technological University** guidelines.

---

## 🛠️ Future Improvements

* Mobile app version with offline support
* Multi-language support
* Behavioral and emotional coaching insights
* Integration with job portals for end-to-end interview preparation

---

## 🧑‍💻 Authors

* **V. Anantharaman** – [@TheViper008](https://github.com/TheViper008)
* **Vaishnav Sudheer** - [@AnanthJaeger401](https://github.com/AnanthJaeger401)

Project guided by **Mrs. Krishna Sowjanya K**, Assistant Professor, Dept. of CSE, CMRIT

---

## 📄 License

This project is for academic and educational purposes. Contact authors for extended use.

```
