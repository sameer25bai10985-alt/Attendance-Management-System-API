package com.attendance.model;

import jakarta.persistence.*;
import java.time.LocalDate;

/**
 * One attendance row = one student, one subject, one day.
 * The unique constraint is what guarantees "no duplicate attendance".
 */
@Entity
@Table(name = "attendance",
        uniqueConstraints = @UniqueConstraint(
                name = "uk_attendance_student_subject_date",
                columnNames = {"student_id", "subject_id", "attendance_date"}))
public class Attendance {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "student_id", nullable = false)
    private Long studentId;

    @Column(name = "subject_id", nullable = false)
    private Long subjectId;

    @Column(name = "attendance_date", nullable = false)
    private LocalDate attendanceDate;

    /** "present" or "absent" (stored lowercase). */
    @Column(nullable = false, length = 10)
    private String status;

    public Attendance() { }

    public Attendance(Long studentId, Long subjectId, LocalDate attendanceDate, String status) {
        this.studentId = studentId;
        this.subjectId = subjectId;
        this.attendanceDate = attendanceDate;
        this.status = status;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public Long getStudentId() { return studentId; }
    public void setStudentId(Long studentId) { this.studentId = studentId; }
    public Long getSubjectId() { return subjectId; }
    public void setSubjectId(Long subjectId) { this.subjectId = subjectId; }
    public LocalDate getAttendanceDate() { return attendanceDate; }
    public void setAttendanceDate(LocalDate attendanceDate) { this.attendanceDate = attendanceDate; }
    public String getStatus() { return status; }
    public void setStatus(String status) { this.status = status; }
}
