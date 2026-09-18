# 🎓 Proxy - AI Powered Attendance App

**Proxy** is an AI-based attendance management system that helps teachers automate student attendance using **face recognition** and **voice recognition**.  
It is designed to reduce proxy attendance, save classroom time, and make attendance tracking simple for both teachers and students.

---

## 🚀 Features

- 👩‍🎓 Student registration with face capture
- 🎙️ Optional voice enrollment for students
- 👨‍🏫 Separate teacher and student portals
- 🤖 Face recognition based attendance marking
- 🔊 Voice recognition based attendance support
- 📚 Subject creation and management by teachers
- 🔗 Subject enrollment using join codes and QR codes
- 📊 Attendance records and summary tracking
- 🔐 Secure teacher authentication using password hashing
- ☁️ Supabase database integration

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **Supabase**
- **dlib**
- **scikit-learn**
- **Librosa**
- **Resemblyzer**
- **pandas**
- **NumPy**
- **bcrypt**
- **Segno**
- **Pillow**

---

## ⚙️ How It Works

1. Students register using their face and optional voice sample.
2. Teachers create subjects and share join codes or QR codes.
3. Students enroll in subjects using the shared code.
4. Teachers upload classroom photos or record audio.
5. The system detects present students using AI.
6. Attendance records are stored and displayed in the dashboard.

---

## 📁 Project Structure

```text
Proxy---online-attendance-app/
├── app.py
├── requirements.txt
├── .streamlit/
└── src/
    ├── components/
    ├── database/
    ├── pipelines/
    ├── screens/
    └── ui/
```

---

## ▶️ Run Locally

```bash
git clone https://github.com/Sakshi-2565/Proxy---online-attendance-app.git
cd Proxy---online-attendance-app
pip install -r requirements.txt
streamlit run app.py
```

---

## 👩‍💻 Author

**Sakshi Vishwakarma**
