package com.attendance.dto;

import jakarta.validation.constraints.NotBlank;
import jakarta.validation.constraints.NotNull;
import jakarta.validation.constraints.Pattern;

import java.time.LocalDate;

public record AttendanceRequest(
        @NotNull Long studentId,
        @NotNull Long subjectId,
        @NotNull LocalDate attendanceDate,
        @NotBlank
        @Pattern(regexp = "(?i)present|absent", message = "must be 'present' or 'absent'")
        String status) {
}
