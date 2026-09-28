package com.attendance.service;

import com.attendance.dto.SubjectRequest;
import com.attendance.exception.ResourceNotFoundException;
import com.attendance.model.Subject;
import com.attendance.repository.AttendanceRepository;
import com.attendance.repository.SubjectRepository;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Service
public class SubjectService {

    private final SubjectRepository subjects;
    private final AttendanceRepository attendance;

    public SubjectService(SubjectRepository subjects, AttendanceRepository attendance) {
        this.subjects = subjects;
        this.attendance = attendance;
    }

    public Subject create(SubjectRequest req) {
        return subjects.save(new Subject(req.name().trim(), req.code().trim()));
    }

    public List<Subject> findAll() {
        return subjects.findAll();
    }

    public Subject findById(Long id) {
        return subjects.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Subject not found"));
    }

    @Transactional
    public Subject update(Long id, SubjectRequest req) {
        Subject s = findById(id);
        s.setName(req.name().trim());
        s.setCode(req.code().trim());
        return subjects.save(s);
    }

    @Transactional
    public void delete(Long id) {
        Subject s = findById(id);
        attendance.deleteBySubjectId(id);
        subjects.delete(s);
    }
}
