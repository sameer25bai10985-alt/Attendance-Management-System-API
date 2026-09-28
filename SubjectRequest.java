package com.attendance.dto;

import jakarta.validation.constraints.NotBlank;

public record SubjectRequest(
        @NotBlank String name,
        @NotBlank String code) {
}
