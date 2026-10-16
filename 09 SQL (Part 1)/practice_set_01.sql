USE college;

CREATE TABLE IF NOT EXISTS Teacher(
id INT PRIMARY KEY,
name varchar(20) NOT NULL,
subject varchar(20) NOT NULL,
salary INT DEFAULT 20000 
);

INSERT INTO Teacher(id,name,subject,salary)
VALUES
(23,"ajay","math",50000),
(47,"bharat","english",60000),
(18,"chetan","chemistry",45000),
(9,"divya","physics",90000);

SELECT * FROM Teacher;

SELECT * FROM Teacher
WHERE salary > 50000;

ALTER TABLE Teacher
CHANGE COLUMN salary ctc INT;

SET SQL_SAFE_UPDATES = 0;

UPDATE Teacher
SET ctc = 1.25* ctc;

ALTER TABLE Teacher
ADD column city varchar(30) default "Gurgaon";

ALTER TABLE Teacher
DROP COLUMN ctc;
