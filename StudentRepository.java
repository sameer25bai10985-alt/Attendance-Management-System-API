package com.attendance.repository;

import com.attendance.model.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface StudentRepository extends JpaRepository<Student, Long> {

    @Query("""
            SELECT s FROM Student s
            WHERE LOWER(s.name) LIKE LOWER(CONCAT('%', :keyword, '%'))
               OR LOWER(s.rollNo) LIKE LOWER(CONCAT('%', :keyword, '%'))
               OR LOWER(s.email) LIKE LOWER(CONCAT('%', :keyword, '%'))
               OR LOWER(s.branch) LIKE LOWER(CONCAT('%', :keyword, '%'))
            """)
    List<Student> search(@Param("keyword") String keyword);
}
