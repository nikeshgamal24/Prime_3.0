USE college;

CREATE TABLE IF NOT EXISTS student(
 roll_no INT PRIMARY KEY,
 name varchar(30)  NOT NULL,
 city varchar(30) NOT NULL,
 marks FLOAT
);

select * from student;

INSERT INTO student(roll_no,name, city, marks)
VALUES
(110,"adam","Delhi",76),
(109,"bob","Mumbai",65),
(124,"casey","Pune",94),
(112,"duke","Pune",80);

SELECT * FROM student 
where marks > 75;

SELECT city,max(marks) FROM student
GROUP BY city;

ALTER TABLE student
ADD COLUMN grade varchar(10);

SET SQL_SAFE_UPDATES = 0;

UPDATE student
SET grade = CASE
	WHEN marks > 80 THEN "O"
    WHEN marks >= 70 and marks <= 80 THEN "A"
    WHEN marks >= 60 and marks <= 70 THEN "B"
END;

SELECT * FROM student;
