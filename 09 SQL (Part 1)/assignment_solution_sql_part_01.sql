USE college;

CREATE TABLE IF NOT EXISTS employee(
EmpID INT PRIMARY KEY,
FirstName VARCHAR(20) NOT NULL,
LastName VARCHAR(20) NOT NULL,
Department VARCHAR(20) 	NOT NULL,
Salary INT,
HireDate DATE
);

INSERT INTO employee (EmpID, FirstName, LastName, Department, Salary, HireDate)
VALUES 
(101, 'Alice', 'Johnson', 'IT', 6500.00, '2020-03-15'),
(102, 'Mark', 'Rivera', 'HR', 4800.00, '2019-07-22'),
(103, 'Sophia', 'Lee', 'Finance', 7200.00, '2021-01-10'),
(104, 'Daniel', 'Kim', 'IT', 5800.00, '2018-11-05'),
(105, 'Emma', 'Brown', 'Marketing', 5300.00, '2022-04-18'),
(106, 'Liam', 'Patel', 'Finance', 6900.00, '2020-09-29'),
(107, 'Olivia', 'Garcia', 'HR', 4600.00, '2017-06-30'),
(108, 'Noah', 'Thompson', 'IT', 7500.00, '2023-02-12'),
(109, 'Ava', 'Martinez', 'Marketing', 5100.00, '2019-12-02'),
(110, 'Ethan', 'Davis', 'Finance', 8000.00, '2016-05-14');

-- qn 1
SELECT * FROM employee;


-- qn 2
SELECT FirstName, LastName, Salary FROM employee;

-- qn 3
SELECT * FROM employee
WHERE Department = 'IT';

-- qnq 4
SELECT * FROM employee
WHERE Salary > 6000;

-- qn 5
SELECT * FROM employee
ORDER BY HireDate DESC;

-- qn 6
SELECT distinct(Department) FROM employee;

-- qn 7
SELECT * FROM employee
WHERE FirstName LIKE "A%";

-- qn 8
SELECT * FROM employee
WHERE Salary >= 4000 and Salary <= 7000;

-- qn 9
SELECT avg(Salary) FROM employee;

-- qn 10
SELECT Department, count(EmpId) AS "Number of Employee" 
FROM employee
group by Department
Having count(EmpId) >= 3;
