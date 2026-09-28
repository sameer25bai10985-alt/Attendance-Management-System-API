package com.attendance.dto;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;

public record StudentRequest(
        @NotBlank String name,
        @NotBlank String rollNo,
        @NotBlank @Email String email,
        @NotBlank String branch) {
}
