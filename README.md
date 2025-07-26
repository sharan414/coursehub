# 📚 CourseHub – Quiz Management System

**CourseHub** is a Flask-based mini learning platform that enables instructors to create quizzes and students to take them. It includes features like quiz creation, question addition, secure student login, and quiz result tracking.

---

## 🚀 Features

### 👨‍🏫 Instructor Panel
- Create quizzes with custom titles.
- Add multiple questions with options A–D and mark the correct answer.
- View quiz results for each quiz and see student scores.

### 👨‍🎓 Student Panel
- Take available quizzes from the dashboard.
- Answer multiple-choice questions and submit responses.
- Instantly view your quiz score after submission.

### 🔐 Authentication
- Secure login system for students and instructors.
- Access-restricted pages using Flask-Login.

---

## 🛠️ Technologies Used

- **Flask** – Web framework (Python)
- **Jinja2** – Templating engine
- **Flask-Login** – Authentication
- **SQLite** – Lightweight relational database
- **SQLAlchemy** – ORM for database interaction
- **Tailwind CSS** – Modern UI styling

---

## 📁 Folder Structure

CourseHub/
│
├── templates/
│   ├── create_quiz.html
│   ├── add_questions.html
│   ├── take_quiz.html
│   ├── quiz_results.html
│   ├── available_quizzes.html
│   ├── login.html
│   ├── dashboard.html
│
├── static/
│   └── styles.css (custom styles if needed)
│
├── models/
│   └── models.py (Quiz, Question, Submission, User models)
│
├── routes/
│   └── quiz_routes.py
│
├── app.py
├── extensions.py
└── requirements.txt

---

## ✅ To-Do (Optional Enhancements)

- Add quiz time limits.
- Email notifications after quiz submissions.
- Graphs for quiz performance (using Chart.js or Recharts).
- Role separation (Teacher vs Student dashboard).

---

## 🙌 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss your ideas.

---

## 📄 License

This project is open-source 