package com.attendance.dto;

import com.fasterxml.jackson.annotation.JsonInclude;

/** Same envelope the Flask API used: {"message": "...", "data": ...}. */
@JsonInclude(JsonInclude.Include.NON_NULL)
public record ApiResponse<T>(String message, T data) {

    public static <T> ApiResponse<T> of(String message, T data) {
        return new ApiResponse<>(message, data);
    }

    public static <T> ApiResponse<T> message(String message) {
        return new ApiResponse<>(message, null);
    }

    public static <T> ApiResponse<T> data(T data) {
        return new ApiResponse<>(null, data);
    }
}
