package com.attendance.service;

import com.attendance.dto.StudentRequest;
import com.attendance.exception.ResourceNotFoundException;
import com.attendance.model.Student;
import com.attendance.repository.AttendanceRepository;
import com.attendance.repository.StudentRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class StudentService {

    private final StudentRepository students;
    private final AttendanceRepository attendance;

    public StudentService(StudentRepository students, AttendanceRepository attendance) {
        this.students = students;
        this.attendance = attendance;
    }

    public Student create(StudentRequest req) {
        return students.save(new Student(req.name().trim(), req.rollNo().trim(),
                req.email().trim(), req.branch().trim()));
    }

    public List<Student> findAll() {
        return students.findAll();
    }

    public Student findById(Long id) {
        return students.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Student not found"));
    }

    @Transactional
    public Student update(Long id, StudentRequest req) {
        Student s = findById(id);
        s.setName(req.name().trim());
        s.setRollNo(req.rollNo().trim());
        s.setEmail(req.email().trim());
        s.setBranch(req.branch().trim());
        return students.save(s);
    }

    @Transactional
    public void delete(Long id) {
        Student s = findById(id);
        attendance.deleteByStudentId(id);   // remove the student's attendance rows too
        students.delete(s);
    }

    public List<Student> search(String keyword) {
        return students.search(keyword.trim());
    }
}
