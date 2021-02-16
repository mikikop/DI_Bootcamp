<!-- Exercise 1 -->

SELECT
	rating, COUNT(*)
FROM film
GROUP BY rating;

SELECT
	title, rating
FROM film
WHERE rating IN ('G','PG-13')

SELECT
	title, rating, length, rental_rate
FROM film
WHERE rating IN ('G','PG-13') AND length < 120 AND rental_rate < 3.00
ORDER BY title ASC

UPDATE customer
SET first_name = 'Michael',
    last_name = 'Perez'
WHERE customer_id = 1;

<!-- Exercise 2 -->

UPDATE students
SET birth_date = '02/11/1998'
WHERE student_id IN (1,3);

UPDATE students
SET last_name = 'Guez'
WHERE student_id = 5;

DELETE FROM students
WHERE student_id = 3;

SELECT count(*)
FROM students

SELECT count(*)
FROM students
WHERE birth_date > '1/01/2000'

ALTER TABLE students
ADD COLUMN math_grade integer;

UPDATE students
SET math_grade = 80
WHERE student_id = 1

UPDATE students
SET math_grade = 90
WHERE student_id IN (2,4)

UPDATE students
SET math_grade = 40
WHERE student_id = 6

SELECT count(*)
FROM students
WHERE math_grade >83

INSERT INTO students(last_name, first_name, birth_date, math_grade)
VALUES ('Simpson', 'Omer', '2003-06-14', 70 );

SELECT first_name, last_name, count(math_grade) AS total_grade
FROM students
GROUP BY first_name,last_name


