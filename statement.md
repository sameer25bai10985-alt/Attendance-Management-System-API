# Project Title

**Attendance Management System API**

# Problem Statement

Managing attendance manually in colleges can take a lot of time. It can also cause problems such as duplicate attendance entries, mistakes while calculating percentages, and difficulty in finding a student's previous attendance records.

This project provides a backend REST API to manage attendance in a structured way. It stores student, subject, and attendance details in a MySQL database. The API allows users to add and manage records, mark attendance, view attendance details, and calculate attendance percentages when required.

# Scope of the Project

The project focuses on the backend part of an attendance management system. It provides APIs for managing students and subjects and for recording attendance.

The system can be used to:

* Add, update, delete, and search student records
* Create and manage subjects
* Mark attendance for students
* Check and prevent duplicate attendance entries
* View attendance by student
* View attendance by date
* Calculate overall attendance percentage
* Calculate subject-wise attendance percentage

The current project is developed using **Flask and MySQL**. It does not include a graphical frontend, user authentication, notifications, or biometric attendance. These features can be added in the future if required.

# Target Users

* College teachers and faculty members
* Academic coordinators
* Educational institutions
* Developers who want to build a frontend using the API

# High-Level Features

1. **Subject Management** – Create and manage subject records.
2. **Student Management** – Add, update, delete, and search student records.
3. **Attendance Marking** – Record attendance for students.
4. **Duplicate Prevention** – Prevent the same attendance record from being added twice.
5. **Student-wise Attendance** – View attendance records for a particular student.
6. **Date-wise Attendance** – Check attendance records for a particular date.
7. **Overall Percentage** – Calculate a student's overall attendance percentage.
8. **Subject-wise Percentage** – Calculate attendance percentage for a particular subject.
9. **Input Validation** – Check the received data and return suitable HTTP responses for invalid requests.
