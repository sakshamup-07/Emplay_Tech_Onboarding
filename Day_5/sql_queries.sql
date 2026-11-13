CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    department VARCHAR(50),
    salary NUMERIC(10, 2)
);
INSERT INTO employees (id, name, age, department, salary)
VALUES
(1, 'Rahul', 25, 'Engineering', 50000),
(2, 'Aman', 27, 'HR', 60000),
(3, 'Priya', 24, 'Engineering', 45000),
(4, 'Neha', 29, 'Finance', 70000),
(5, 'Rohan', 26, 'HR', 55000);

select * from employees 
where department = 'HR';

delete from employees 
where age = 27;

truncate table employees
SELECT DISTINCT department FROM employees;
SELECT * FROM employees
WHERE salary > 50000;

SELECT * FROM employees
WHERE department = 'Engineering'
AND salary > 50000;

SELECT * FROM employees
WHERE department = 'HR'
OR department = 'Finance';

SELECT * FROM employees
WHERE NOT department = 'HR';

SELECT * FROM employees
ORDER BY salary ASC;

SELECT *
FROM employees e
WHERE e.name ILIKE '%a%'
ORDER BY e.salary DESC
LIMIT 2;

SELECT *
FROM employees e
WHERE e.name ILIKE '%a'
ORDER BY e.salary desc;

SELECT * FROM employees
WHERE department IN ('HR', 'Finance');

SELECT * FROM employees
WHERE salary BETWEEN 40000 AND 60000;

SELECT COUNT(*) AS total_employees
FROM employees;

SELECT SUM(salary) AS total_salary
FROM employees;

SELECT AVG(salary) AS average_salary
FROM employees;
SELECT
    MIN(salary) AS lowest_salary,
    MAX(salary) AS highest_salary
FROM employees;

SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;

SELECT
    department,
    COUNT(*) AS employee_count,
    SUM(salary) AS total_salary,
    AVG(salary) AS average_salary
FROM employees
GROUP BY department
HAVING COUNT(*) > 1;

CREATE TABLE departments (
    id INT PRIMARY KEY,
    department_name VARCHAR(50) UNIQUE
);
INSERT INTO departments (id, department_name)
VALUES
(1, 'Engineering'),
(2, 'HR'),
(3, 'Finance'),
(4, 'Marketing');

SELECT
    e.name,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department = d.department_name;

    select 
e.name,
e.department
from employees e 
left join departments d 
on e.department =d.department_name;

delete from departments 
where department_name ='HR';
select * from departments d 

select
e.name,
e.department
from employees e 
right join departments d 
on e.department =d.department_name;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    department_id INT,
    FOREIGN KEY (department_id)
        REFERENCES departments(id)
);