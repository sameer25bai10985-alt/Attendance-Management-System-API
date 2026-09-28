package com.attendance.model;

import jakarta.persistence.*;

@Entity
@Table(name = "students")
public class Student {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, length = 100)
    private String name;

    @Column(name = "roll_no", nullable = false, unique = true, length = 50)
    private String rollNo;

    @Column(nullable = false, unique = true, length = 150)
    private String email;

    @Column(nullable = false, length = 100)
    private String branch;

    public Student() { }

    public Student(String name, String rollNo, String email, String branch) {
        this.name = name;
        this.rollNo = rollNo;
        this.email = email;
        this.branch = branch;
    }

    public Long getId() { return id; }
    public void setId(Long id) { this.id = id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getRollNo() { return rollNo; }
    public void setRollNo(String rollNo) { this.rollNo = rollNo; }
    public String getEmail() { return email; }
    public void setEmail(String email) { this.email = email; }
    public String getBranch() { return branch; }
    public void setBranch(String branch) { this.branch = branch; }
}
