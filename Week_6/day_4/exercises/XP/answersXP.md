<!-- Ex1 -->

SELECT first_name "First Name", last_name  "Last Name" 
FROM employees

SELECT
   DISTINCT department_id d
FROM
   employees
ORDER BY d ASC;

SELECT * FROM employees 
ORDER BY first_name DESC

SELECT first_name, last_name, salary, salary*.15 PF
FROM employees


SELECT employee_id, first_name, last_name, salary PF 
FROM employees
ORDER BY salary ASC

SELECT sum(salary) total_salary 
FROM employees


SELECT min(salary) "Minimum salary", max(salary) "Maximum salary"
FROM employees

SELECT round(avg(salary),2) "Average salary"
FROM employees

SELECT count(employee_id) "number of employees"
FROM employees

SELECT UPPER(first_name) "First Name"
FROM employees

SELECT LEFT(first_name, 3) "Initiales"
FROM employees

SELECT CONCAT(first_name,' ',last_name) "Full Name"
FROM employees

SELECT CONCAT(first_name,' ',last_name) as "Full Name", length(first_name)+length(last_name)
FROM employees;

SELECT * 
FROM employees 
WHERE  first_name 
SIMILAR TO   '%0|1|2|3|4|5|6|7|8|9%';

SELECT *
FROM employees
LIMIT 10

<!-- Ex2 -->

SELECT CONCAT(first_name,' ',last_name) as "name", salary
FROM employees 
WHERE  salary BETWEEN 10000 AND 15000


SELECT first_name
FROM employees
WHERE first_name LIKE '%c%'
AND first_name LIKE '%e%';

SELECT e.last_name, j.job_title, e.salary
FROM employees e INNER JOIN jobs j
	ON e.job_id = j.job_id
WHERE j.job_title != 'Programmer' AND j.job_title != 'Shpping Clerk'
	AND salary NOT IN (4500,10000,15000)

SELECT last_name
FROM employees
WHERE char_length(last_name) = 6

SELECT last_name
FROM employees
WHERE last_name LIKE '__e%'


SELECT DISTINCT job_id  
FROM employees;

SELECT *
FROM employees
WHERE last_name IN ('Jones','Blake','Scott','King','Ford')

<!-- Ex3 -->

UPDATE employees
SET email = 'not available'
WHERE department_id = 11



