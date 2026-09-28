-- Optional: Hibernate creates these tables automatically (ddl-auto=update).
-- Use this file if you prefer to create the schema manually.
CREATE DATABASE IF NOT EXISTS attendance_db;
USE attendance_db;

CREATE TABLE IF NOT EXISTS students (
    id      BIGINT AUTO_INCREMENT PRIMARY KEY,
    name    VARCHAR(100) NOT NULL,
    roll_no VARCHAR(50)  NOT NULL UNIQUE,
    email   VARCHAR(150) NOT NULL UNIQUE,
    branch  VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS subjects (
    id   BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    code VARCHAR(30)  NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS attendance (
    id              BIGINT AUTO_INCREMENT PRIMARY KEY,
    student_id      BIGINT      NOT NULL,
    subject_id      BIGINT      NOT NULL,
    attendance_date DATE        NOT NULL,
    status          VARCHAR(10) NOT NULL,
    CONSTRAINT uk_attendance_student_subject_date UNIQUE (student_id, subject_id, attendance_date),
    CONSTRAINT fk_att_student FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
    CONSTRAINT fk_att_subject FOREIGN KEY (subject_id) REFERENCES subjects(id) ON DELETE CASCADE
);
