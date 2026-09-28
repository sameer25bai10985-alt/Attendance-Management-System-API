package com.attendance.controller;

import com.attendance.dto.ApiResponse;
import com.attendance.dto.SubjectRequest;
import com.attendance.model.Subject;
import com.attendance.service.SubjectService;
import jakarta.validation.Valid;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/subjects")
public class SubjectController {

    private final SubjectService service;

    public SubjectController(SubjectService service) {
        this.service = service;
    }

    @PostMapping
    public ResponseEntity<ApiResponse<Subject>> create(@Valid @RequestBody SubjectRequest req) {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(ApiResponse.of("Successfully saved subject", service.create(req)));
    }

    @GetMapping
    public ApiResponse<List<Subject>> getAll() {
        return ApiResponse.data(service.findAll());
    }

    @GetMapping("/{id}")
    public ApiResponse<Subject> getById(@PathVariable Long id) {
        return ApiResponse.data(service.findById(id));
    }

    @PutMapping("/{id}")
    public ApiResponse<Subject> update(@PathVariable Long id, @Valid @RequestBody SubjectRequest req) {
        return ApiResponse.of("Subject updated successfully", service.update(id, req));
    }

    @DeleteMapping("/{id}")
    public ApiResponse<Void> delete(@PathVariable Long id) {
        service.delete(id);
        return ApiResponse.message("Subject deleted successfully");
    }
}
