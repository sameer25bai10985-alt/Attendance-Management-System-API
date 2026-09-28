package com.attendance.controller;

import com.attendance.exception.ResourceNotFoundException;
import com.attendance.model.Student;
import com.attendance.service.StudentService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.WebMvcTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;

import static org.mockito.ArgumentMatchers.any;
import static org.mockito.Mockito.when;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.jsonPath;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@WebMvcTest(StudentController.class)
class StudentControllerTest {

    @Autowired MockMvc mvc;
    @MockBean StudentService service;

    @Test
    void createReturns201() throws Exception {
        when(service.create(any())).thenReturn(new Student("Asha", "R101", "asha@x.com", "CSE"));

        mvc.perform(post("/students").contentType(MediaType.APPLICATION_JSON)
                        .content("""
                                {"name":"Asha","roll_no":"R101","email":"asha@x.com","branch":"CSE"}
                                """))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.message").value("Student saved successfully"))
                .andExpect(jsonPath("$.data.roll_no").value("R101"));
    }

    @Test
    void missingFieldReturns400() throws Exception {
        mvc.perform(post("/students").contentType(MediaType.APPLICATION_JSON)
                        .content("{\"name\":\"Asha\"}"))
                .andExpect(status().isBadRequest());
    }

    @Test
    void unknownStudentReturns404() throws Exception {
        when(service.findById(99L)).thenThrow(new ResourceNotFoundException("Student not found"));

        mvc.perform(get("/students/99"))
                .andExpect(status().isNotFound())
                .andExpect(jsonPath("$.message").value("Student not found"));
    }
}
