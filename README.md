# 📚 ATTENDANCE MANAGEMENT SYSTEM API

> A simple REST API for managing students, subjects, attendance records, and attendance percentages using Python, Flask, and MySQL.

---

🎯 What This Project Does

Managing attendance manually can result in duplicate records, missed entries, and extra work when checking percentages.

This project provides APIs to handle these tasks through a backend system. Student, subject, and attendance data is stored in MySQL and can be accessed using tools such as Postman.

---

 ✨ Main Features

👨‍🎓 Student management
 📖 Subject management
 📝 Mark attendance
 🚫 Duplicate attendance checking
 📅 Attendance by date
👤 Attendance by student
 📊 Overall attendance percentage
 📚 Subject-wise attendance percentage
 🔄 JSON-based API responses

---

## 🛠️ Technologies

| Technology      | Use                       |
| --------------- | ------------------------- |
| 🐍 Python       | Main programming language |
| 🌐 Flask        | REST API development      |
| 🗄️ MySQL       | Data storage              |
| 🧪 Postman      | API testing               |
| 🔧 Git & GitHub | Version control           |

---

## 🗂️ Project Structure

```text
Attendance-Management-System-API/
│
├── app.py
├── db.py
│
├── student.py
├── student_routes.py
│
├── subject.py
├── subject_routes.py
│
├── attendance.py
├── attendance_routes.py
│
├── test_api.py
├── requirements.txt
├── .env.example
└── documentation files
```

---

🚀 Setup & Run

You don't need any previous knowledge of the project. Follow these steps in order.

1️⃣ Install Python

Install **Python 3.x** on your computer.

Check the installation:

```bash
python --version
```

---

 2️⃣ Install Dependencies

Open the project folder in the terminal and run:

```bash
pip install -r requirements.txt
```

This installs the packages required by the API.

---

3️⃣ Set Up MySQL

Install and start **MySQL**.

Create the database required for the project and make sure MySQL is running before starting the Flask application.

---

### 4️⃣ Configure the Database

Use `.env.example` as a reference for the database configuration.

Add your own MySQL details, such as:

* Database host
* Username
* Password
* Database name

 Do not upload real passwords or private database credentials to GitHub.

---

5️⃣ ▶️ Start the API

From the project folder, run:

```bash
python app.py
```

Once Flask starts successfully, the API is ready to receive requests.

---

# 🧪 Testing with Postman

Open **Postman** and test the available endpoints.

A basic testing flow is:

```text
👨‍🎓 Create Student
        ↓
📖 Create Subject
        ↓
📝 Mark Attendance
        ↓
🔍 Check Attendance
        ↓
📊 Calculate Percentage
```

The API returns the result of each operation in JSON format.

---

🧩 Main Modules

👨‍🎓 Student Module

Used to create and retrieve student information.

 📖 Subject Module

Handles subject creation, viewing, updating, and deletion.

📝 Attendance Module

Stores attendance records and checks for duplicate entries.

📊 Percentage Module

Uses the stored attendance records to calculate overall and subject-wise attendance percentages.

---

 🧪 Testing

`test_api.py` contains tests for different API situations, including:

 Valid requests
 Missing fields
 Empty input
 Duplicate attendance
 Attendance operations

---

📁 Documentation

Additional project documentation is available in the repository:

 `statement.md` — Problem statement and project scope
 `architecture.md` — System architecture
 `workflow.md` — API workflow
 `use_case.md` — Use cases
 `component_diagram.md` — System components
 `sequence_diagram.md` — API sequence flow
 `er_diagram.md` — Database relationships
  `design_decisions.md` — Design decisions
 `PROJECT_REPORT.md` — Detailed project report

---

🔮 Future Enhancements

Some features that can be added later:

* 🔔 Low attendance alerts
* 🔐 Authentication and user roles
* 📊 Attendance dashboard
* 📄 Attendance report export
* 📈 More detailed attendance analytics

---

✅ Conclusion

The project provides a backend API for handling the student, subject, and attendance information. Flask manages the API requests, while MySQL stores the data. Separating routes and database operations keeps the project easier to test and maintain.
