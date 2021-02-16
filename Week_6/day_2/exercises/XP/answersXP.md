<!-- Exercise 1 -->

SELECT *
FROM items
ORDER BY item_price ASC;

SELECT *
FROM items
WHERE item_price >= 80
ORDER BY item_price DESC;

SELECT first_name,last_name
FROM customers
ORDER BY first_name ASC
LIMIT 3;

SELECT last_name
FROM customers
ORDER BY last_name DESC;

INSERT INTO purchases(customer_id, item_id)
VALUES 
(2,1),
(2,2),
(1,3),
(4,1),
(5,2);

SELECT * FROM purchases <!-- not helping -->  

SELECT * FROM purchases INNER JOIN customers
ON purchases.customer_id = customers.customers_id;

SELECT * FROM purchases INNER JOIN customers
ON purchases.customer_id = customers.customers_id
WHERE customers.customers_id = 4;

SELECT first_name,last_name, item_name FROM purchases INNER JOIN customers
ON purchases.customer_id = customers.customers_id
INNER JOIN items 
ON items.items_id = purchases.item_id
WHERE items_id IN (1,2);


INSERT INTO items(item_name,item_price)
VALUES ('Hard Drive', 150);

INSERT INTO purchases (customer_id,item_id)
VALUES 
(3, 4);


SELECT first_name, last_name, item_name FROM purchases INNER JOIN customers
ON purchases.customer_id = customers.customers_id
JOIN items
ON purchases.item_id = items.items_id;


<!-- Exercise 2 -->

SELECT * FROM customer;

SELECT first_name || ' ' || last_name AS full_name FROM customer;

SELECT DISTINCT create_date FROM customer;

SELECT * 
FROM customer
ORDER BY first_name ASC;

SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

SELECT address, district, phone
FROM address
WHERE district = 'Texas';

SELECT *
FROM film
WHERE film_id IN (15,150);

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Back to the future';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Back to the future';

SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'Ba%';

SELECT film_id, title
FROM film
ORDER BY rental_rate
LIMIT 10;

SELECT film_id, title
FROM film
ORDER BY rental_rate
OFFSET 10
FETCH first 10 row only;

SELECT amount, payment_date
FROM payment INNER JOIN customer
ON payment.customer_id = customer.customer_id
ORDER BY payment.customer_id ASC;

SELECT
	film.film_id,
	title,
	inventory_id
FROM
	film
LEFT JOIN inventory 
    ON inventory.film_id = film.film_id
ORDER BY title;


SELECT
	city,
	country
FROM
	city
INNER JOIN country 
    ON city.country_id = country.country_id

SELECT
	staff.staff_id, payment.customer_id, customer.first_name, customer.last_name, payment.amount, payment.payment_date
FROM
	customer
INNER JOIN payment 
    ON customer.customer_id = payment.customer_id
INNER JOIN staff
	ON payment.staff_id = staff.staff_id
ORDER BY staff.staff_id




	

