package com.attendance.controller;

import com.attendance.dto.ApiResponse;
import com.attendance.dto.AttendanceRequest;
import com.attendance.dto.PercentageResponse;
import com.attendance.model.Attendance;
import com.attendance.service.AttendanceService;
import jakarta.validation.Valid;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.time.LocalDate;
import java.util.List;

@RestController
@RequestMapping("/attendance")
public class AttendanceController {

    private final AttendanceService service;

    public AttendanceController(AttendanceService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<Attendance>> mark(@Valid @RequestBody AttendanceRequest req) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.of("Attendance marked successfully", service.mark(req)));
    }

    @GetMapping("/student/{studentId}")
    public ApiResponse<List<Attendance>> byStudent(@PathVariable Long studentId) {
        return ApiResponse.data(service.byStudent(studentId));
    }

    @GetMapping("/date/{date}")
    public ApiResponse<List<Attendance>> byDate(
            @PathVariable @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate date) {
        return ApiResponse.data(service.byDate(date));
    }

    @GetMapping("/percentage/student/{studentId}")
    public PercentageResponse overall(@PathVariable Long studentId) {
        return new PercentageResponse(studentId, null, service.overallPercentage(studentId));
    }

    @GetMapping("/percentage/student/{studentId}/subject/{subjectId}")
    public PercentageResponse bySubject(@PathVariable Long studentId, @PathVariable Long subjectId) {
        return new PercentageResponse(studentId, subjectId, service.subjectPercentage(studentId, subjectId));
    }
}
