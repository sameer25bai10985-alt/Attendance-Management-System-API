package com.attendance.controller;

import com.attendance.dto.ApiResponse;
import com.attendance.dto.StudentRequest;
import com.attendance.model.Student;
import com.attendance.service.StudentService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/students")
public class StudentController {

    private final StudentService service;

    public StudentController(StudentService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<Student>> create(@Valid @RequestBody StudentRequest req) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.of("Student saved successfully", service.create(req)));
    }

    @GetMapping
    public ApiResponse<List<Student>> getAll() {
        return ApiResponse.data(service.findAll());
    }

    @GetMapping("/{id}")
    public ApiResponse<Student> getById(@PathVariable Long id) {
        return ApiResponse.data(service.findById(id));
    }

    @PutMapping("/{id}")
    public ApiResponse<Student> update(@PathVariable Long id, @Valid @RequestBody StudentRequest req) {
        return ApiResponse.of("Student updated successfully", service.update(id, req));
    }

    @DeleteMapping("/{id}")
    public ApiResponse<Void> delete(@PathVariable Long id) {
        service.delete(id);
        return ApiResponse.message("Student deleted successfully");
    }

    @GetMapping("/search")
    public ApiResponse<List<Student>> search(@RequestParam String keyword) {
        return ApiResponse.data(service.search(keyword));
    }
}
