package com.attendance.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

@JsonInclude(JsonInclude.Include.NON_NULL)
public record PercentageResponse(Long studentId, Long subjectId, double attendancePercentage) {
}
