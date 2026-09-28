package com.attendance.service;

import com.attendance.dto.AttendanceRequest;
import com.attendance.exception.DuplicateResourceException;
import com.attendance.exception.ResourceNotFoundException;
import com.attendance.model.Attendance;
import com.attendance.repository.AttendanceRepository;
import com.attendance.repository.StudentRepository;
import com.attendance.repository.SubjectRepository;
import org.springframework.stereotype.Service;

import java.time.LocalDate;
import java.util.List;

@Service
public class AttendanceService {

    static final String PRESENT = "present";

    private final AttendanceRepository attendance;
    private final StudentRepository students;
    private final SubjectRepository subjects;

    public AttendanceService(AttendanceRepository attendance,
                             StudentRepository students,
                             SubjectRepository subjects) {
        this.attendance = attendance;
        this.students = students;
        this.subjects = subjects;
    }

    public Attendance mark(AttendanceRequest req) {
        if (!students.existsById(req.studentId())) {
            throw new ResourceNotFoundException("Student not found");
        }
        if (!subjects.existsById(req.subjectId())) {
            throw new ResourceNotFoundException("Subject not found");
        }
        if (attendance.existsByStudentIdAndSubjectIdAndAttendanceDate(
                req.studentId(), req.subjectId(), req.attendanceDate())) {
            throw new DuplicateResourceException("Attendance already marked for this student, subject and date");
        }
        return attendance.save(new Attendance(req.studentId(), req.subjectId(),
                req.attendanceDate(), req.status().toLowerCase()));
    }

    public List<Attendance> byStudent(Long studentId) {
        return attendance.findByStudentIdOrderByAttendanceDate(studentId);
    }

    public List<Attendance> byDate(LocalDate date) {
        return attendance.findByAttendanceDate(date);
    }

    /** Overall percentage across all subjects. */
    public double overallPercentage(Long studentId) {
        long total = attendance.countByStudentId(studentId);
        if (total == 0) {
            throw new ResourceNotFoundException("No attendance records found");
        }
        return percent(attendance.countByStudentIdAndStatus(studentId, PRESENT), total);
    }

    /** Percentage for one subject. */
    public double subjectPercentage(Long studentId, Long subjectId) {
        long total = attendance.countByStudentIdAndSubjectId(studentId, subjectId);
        if (total == 0) {
            throw new ResourceNotFoundException("No attendance records found");
        }
        return percent(attendance.countByStudentIdAndSubjectIdAndStatus(studentId, subjectId, PRESENT), total);
    }

    private double percent(long present, long total) {
        return Math.round(present * 10000.0 / total) / 100.0;   // 2 decimal places
    }
}
