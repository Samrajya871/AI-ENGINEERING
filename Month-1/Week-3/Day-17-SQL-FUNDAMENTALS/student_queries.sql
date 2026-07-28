/*
Student Database System

Create a database named:

student_management.db

Create a students table with:

id
name
age
course
email

Insert at least 10 student records.

Practice these queries:

Display all students.
Display only names and emails.
Find students older than 21.
Find students enrolled in "AI".
Sort students by age.
Show the first 5 students
*/
CREATE TABLE students(
id INTEGER PRIMARY KEY,
name TEXT,
age INTEGER,
course TEXT,
email TEXT);

INSERT INTO students VALUES
(1, 'Alice Smith', 20, 'Computer Science', 'alice.smith@example.com'),
(2, 'Bob Johnson', 22, 'Electrical Engineering', 'bob.johnson@example.com'),
(3, 'Charlie Brown', 19, 'Mechanical Engineering', 'charlie.brown@example.com'),
(4, 'Diana Prince', 21, 'Data Science', 'diana.prince@example.com'),
(5, 'Ethan Hunt', 23, 'Cyber Security', 'ethan.hunt@example.com'),
(6, 'Fiona Gallagher', 20, 'Information Technology', 'fiona.g@example.com'),
(7, 'George Clark', 22, 'Software Engineering', 'george.clark@example.com'),
(8, 'Hannah Abbott', 19, 'Biotechnology', 'hannah.a@example.com'),
(9, 'Ian Malcolm', 24, 'Mathematics', 'ian.malcolm@example.com'),
(10, 'Julia Roberts', 21, 'Physics', 'julia.roberts@example.com');


SELECT * FROM students;

SELECT name,email FROM students;

SELECT * FROM students
WHERE age>21;

SELECT * FROM students
WHERE course="Physics";

SELECT * FROM students
ORDER BY age asc; 

SELECT * FROM students
LIMIT 5;