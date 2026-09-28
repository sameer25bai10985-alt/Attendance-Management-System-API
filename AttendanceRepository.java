package com.attendance.repository;

import com.attendance.model.Attendance;
import org.springframework.data.jpa.repository.JpaRepository;

import java.time.LocalDate;
import java.util.List;

public interface AttendanceRepository extends JpaRepository<Attendance, Long> {

    boolean existsByStudentIdAndSubjectIdAndAttendanceDate(Long studentId, Long subjectId, LocalDate date);

    List<Attendance> findByStudentIdOrderByAttendanceDate(Long studentId);

    List<Attendance> findByAttendanceDate(LocalDate date);

    long countByStudentId(Long studentId);

    long countByStudentIdAndStatus(Long studentId, String status);

    long countByStudentIdAndSubjectId(Long studentId, Long subjectId);

    long countByStudentIdAndSubjectIdAndStatus(Long studentId, Long subjectId, String status);

    void deleteByStudentId(Long studentId);

    void deleteBySubjectId(Long subjectId);
}
