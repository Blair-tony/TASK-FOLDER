create database WON2;
use WON2;
CREATE TABLE Employees (
    employee_id INT,
    ename VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    position VARCHAR(100),
    department VARCHAR(100),
    salary DECIMAL(10, 2),
    start_date DATE,
    end_date DATE,
    email VARCHAR(255)
);
insert into  employees values(1, 'John Doe', 30, 'Male', 'Software Engineer', 'Engineering', 60000.00, '2020-01-01', NULL, 'john.doe@example.com');
insert into  employees values(2, 'Jane Smith', 28, 'Female', 'HR Manager', 'Human Resources', 70000.00, '2019-05-15', NULL, 'jane.smith@example.com');
insert into  employees values(3, 'Michael Johnson', 35, 'Male', 'Sales Representative', 'Sales', 55000.00, '2018-10-20', NULL, 'michael.johnson@example.com');
insert into  employees values(4, 'Emily Brown', 32, 'Female', 'Marketing Specialist', 'Marketing', 62000.00, '2021-02-10', NULL, 'emily.brown@example.com');
insert into  employees values(5, 'David Wilson', 45, 'Male', 'Finance Manager', 'Finance', 80000.00, '2017-07-01', NULL, 'david.wilson@example.com');
insert into  employees values(6, 'Sarah Martinez', 27, 'Female', 'Software Developer', 'Engineering', 65000.00, '2020-11-05', NULL, 'sarah.martinez@example.com');
insert into  employees values(7, 'Christopher Lee', 40, 'Male', 'Senior Analyst', 'Finance', 75000.00, '2016-04-15', NULL, 'christopher.lee@example.com');
insert into  employees values(8, 'Amanda Taylor', 38, 'Female', 'Project Manager', 'Engineering', 70000.00, '2019-08-20', NULL, 'amanda.taylor@example.com');
insert into  employees values(9, 'James Rodriguez', 33, 'Male', 'Accountant', 'Finance', 60000.00, '2019-01-10', NULL, 'james.rodriguez@example.com');
insert into  employees values(10, 'Olivia Garcia', 29, 'Female', 'Sales Manager', 'Sales', 78000.00, '2018-03-01', NULL, 'olivia.garcia@example.com');

select * from employees;

-- 1
select * from employees WHERE age > 18;
-- 2
INSERT INTO employees VALUES (11,'Sarah', 25, 'female','Sales Manager', 'Sales', 98000.00, '2018-03-03', NULL, 'sarah.garcia@example.com');
-- 3
SELECT DISTINCT department FROM employees;
-- 4
SELECT * FROM employees WHERE department = 'Engineering';
-- 5
SELECT * FROM employees WHERE age BETWEEN 25 AND 30;
-- 6
SELECT * FROM employees WHERE ename IN ('John Doe', 'Michael Johnson');
-- 7
SELECT * FROM employees WHERE department = 'Engineering' AND age BETWEEN 25 AND 35;
-- 8
SELECT * FROM employees WHERE department = 'Marketing' OR department = 'Sales';
-- 9 
SELECT * FROM employees WHERE age < 30 OR age > 40;
-- 10
SELECT * FROM employees WHERE department = 'Engineering' AND age > 30;
-- 11
SELECT * FROM employees WHERE age NOT BETWEEN 30 AND 40;
-- 12
SELECT * FROM employees WHERE ename LIKE 'J%' AND age > 25;
-- 13
SELECT * FROM employees WHERE department = 'Finance' AND ename = 'John Doe';
-- 14
SELECT * FROM employees WHERE age NOT IN (45,27);
-- 15
SELECT * FROM Employees WHERE (department = 'Engineering' OR department = 'Marketing') AND age = 30;
