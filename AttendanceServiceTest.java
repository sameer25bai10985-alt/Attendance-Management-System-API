package com.attendance.service;

import com.attendance.dto.AttendanceRequest;
import com.attendance.exception.DuplicateResourceException;
import com.attendance.exception.ResourceNotFoundException;
import com.attendance.model.Attendance;
import com.attendance.repository.AttendanceRepository;
import com.attendance.repository.StudentRepository;
import com.attendance.repository.SubjectRepository;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.extension.ExtendWith;
import org.mockito.InjectMocks;
import org.mockito.Mock;
import org.mockito.junit.jupiter.MockitoExtension;

import java.time.LocalDate;

import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.*;

@ExtendWith(MockitoExtension.class)
class AttendanceServiceTest {

    @Mock AttendanceRepository attendance;
    @Mock StudentRepository students;
    @Mock SubjectRepository subjects;
    @InjectMocks AttendanceService service;

    private final AttendanceRequest req =
            new AttendanceRequest(1L, 2L, LocalDate.of(2026, 9, 29), "Present");

    @Test
    void markSavesLowercaseStatus() {
        when(students.existsById(1L)).thenReturn(true);
        when(subjects.existsById(2L)).thenReturn(true);
        when(attendance.existsByStudentIdAndSubjectIdAndAttendanceDate(1L, 2L, req.attendanceDate()))
                .thenReturn(false);
        when(attendance.save(any(Attendance.class))).thenAnswer(i -> i.getArgument(0));

        Attendance saved = service.mark(req);

        assertEquals("present", saved.getStatus());
    }

    @Test
    void markRejectsDuplicate() {
        when(students.existsById(1L)).thenReturn(true);
        when(subjects.existsById(2L)).thenReturn(true);
        when(attendance.existsByStudentIdAndSubjectIdAndAttendanceDate(1L, 2L, req.attendanceDate()))
                .thenReturn(true);

        assertThrows(DuplicateResourceException.class, () -> service.mark(req));
        verify(attendance, never()).save(any());
    }

    @Test
    void markRejectsUnknownStudent() {
        when(students.existsById(1L)).thenReturn(false);
        assertThrows(ResourceNotFoundException.class, () -> service.mark(req));
    }

    @Test
    void overallPercentageIsRoundedToTwoDecimals() {
        when(attendance.countByStudentId(1L)).thenReturn(3L);
        when(attendance.countByStudentIdAndStatus(1L, "present")).thenReturn(2L);
        assertEquals(66.67, service.overallPercentage(1L));
    }

    @Test
    void percentageWithNoRecordsThrowsNotFound() {
        when(attendance.countByStudentIdAndSubjectId(1L, 2L)).thenReturn(0L);
        assertThrows(ResourceNotFoundException.class, () -> service.subjectPercentage(1L, 2L));
    }
}
