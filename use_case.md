# Use Case Diagram

**Primary actor:** Teacher / Faculty (the person operating the API, e.g. via Postman or a
connected frontend)

**Secondary actor:** Developer / Integrator (a client application consuming the REST API)

```mermaid
flowchart LR
    Teacher((Teacher /<br/>Faculty))
    Dev((Developer /<br/>Client App))

    subgraph "Attendance Management System API"
        UC1[Create Subject]
        UC2[View Subjects]
        UC3[Mark Attendance]
        UC4[View Attendance by Student]
        UC5[View Attendance by Date]
        UC6[Calculate Overall<br/>Attendance Percentage]
        UC7[Calculate Subject-wise<br/>Attendance Percentage]
        UC8[Create / Update /<br/>Delete Student]
        UC9[Search Students]
    end

    Teacher --> UC1
    Teacher --> UC2
    Teacher --> UC3
    Teacher --> UC4
    Teacher --> UC5
    Teacher --> UC6
    Teacher --> UC7
    Teacher --> UC8
    Teacher --> UC9

    Dev --> UC1
    Dev --> UC2
    Dev --> UC3
    Dev --> UC4
    Dev --> UC5
    Dev --> UC6
    Dev --> UC7
```

## Use case descriptions

| Use Case | Precondition | Main Flow | Postcondition |
|---|---|---|---|
| Create Subject | Subject name/code not already used | Client submits subject name + code | New subject stored |
| Mark Attendance | Subject and student exist | Client submits the students, subject, date, status | Attendance row stored, duplicates rejected |
| View Attendance by Student | Student has attendance history | Client requests by student ID | List of attendance records returned |
| Calculate Attendance Percentage | At least one attendance record exists | Client requests percentage by student (and optionally subject) | Percentage value returned |
| Manage Students | — | Client creates/updates/deletes/searches student records | Student table reflects change |
