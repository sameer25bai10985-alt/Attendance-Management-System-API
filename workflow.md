# Process Flow — Mark Attendance

This is the primary workflow of the system: a teacher/faculty member marking a student
present or absent for a subject on a given date.

```mermaid
flowchart TD
    A[Start: POST /attendance] --> B{Request body is valid JSON?}
    B -- No --> B1[Return 400: 'Request must be JSON']
    B -- Yes --> C{All required fields present<br/>student_id, subject_id,<br/>attendance_date, status?}
    C -- No --> C1[Return 400: 'attribute X missing']
    C -- Yes --> D{Any field empty?}
    D -- Yes --> D1[Return 400: 'attribute X cannot be empty']
    D -- No --> E[Call mark_attendance in models/attendance.py]
    E --> F{Duplicate entry for<br/>student+subject+date?}
    F -- Yes --> F1[Return 400: 'Attendance already marked or invalid data']
    F -- No --> G[Insert row into attendance table]
    G --> H[Return 201: 'Attendance marked successfully']
    B1 --> Z[End]
    C1 --> Z
    D1 --> Z
    F1 --> Z
    H --> Z
```

## Related read/report flow — Attendance Percentage

```mermaid
flowchart TD
    A[GET /attendance/percentage/student/id] --> B[Query all attendance rows for student]
    B --> C{Any records found?}
    C -- No --> C1[Return 404: 'No attendance records found']
    C -- Yes --> D[Count present rows / total rows * 100]
    D --> E[Return 200 with attendance_percentage]
```
