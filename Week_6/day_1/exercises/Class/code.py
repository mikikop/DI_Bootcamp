SELECT <columns> FROM <table> WHERE <condition>;
SELECT * FROM people WHERE age >= 25;
SELECT fname, lname FROM people WHERE fname = "Adam";
INSERT INTO <table> (<columns>) VALUES (<values>)
INSERT INTO people (fname, lname, age) VALUES ("Dave", "Davison", 45);
UPDATE <table> SET <column> = <value> WHERE <condition>;
UPDATE people SET fname="Robert" WHERE id=2;
UPDATE people SET fname="Robert";
DELETE FROM <table> WHERE <condition>;
DELETE FROM people WHERE id > 2;
Instead of = you can use LIKE with a wildcard '%something%'