<!-- Exercise 1 -->
SELECT name FROM language;

SELECT fi.title,  fi.description, la.name FROM film fi INNER JOIN language la
	ON fi.language_id = la.language_id

SELECT fi.title,  fi.description, la.name FROM film fi LEFT JOIN language la
	ON fi.language_id = la.language_id

<!-- The languages are Italian, French, German, Mandarin, Japanese -->
SELECT fi.title,  fi.description, la.name FROM film fi RIGHT JOIN language la
	ON fi.language_id = la.language_id


CREATE TABLE new_film (
   id SERIAL PRIMARY KEY,
   name VARCHAR(100) NOT NULL,
);


INSERT INTO new_film(name)
VALUES 
('Back to the Future'),
('Back to the Future II'),
('Terminator'),
('Rocky')
;


CREATE TABLE customer_review (
   review_id SERIAL PRIMARY KEY,
   film_id INT NOT NULL,
   language_id INT,
   title VARCHAR(100),
   score INT NOT NULL,
   review_text VARCHAR,
   last_update TIMESTAMP default current_timestamp,
   CHECK (score BETWEEN 1 AND 10)
);


INSERT INTO customer_review(film_id,language_id,title,score,review_text)
VALUES 
(6,1,'Agent Truman',3,'Is the agent is a good film? i don''t htink because there is no action'),
(37,1,'Arizona Bang',5,'Big bang in Arizona. Good film')
;

INSERT INTO customer_review(film_id,language_id,title,score,review_text)
VALUES 
(2,1,'Back to the Future II',8,'One of the best movie ever made')
;

<!-- The row in customer_review is not deleted -->
DELETE FROM new_film
WHERE id = 2;

<!-- Exercise 2 -->

UPDATE film
SET language_id = 5
WHERE film_id = 1

UPDATE film
SET language_id = 4
WHERE film_id = 2

UPDATE film
SET language_id = 3
WHERE film_id = 3


