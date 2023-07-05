-- Here you can find the analysis I have done after uploading the book data
-- to the postgres database.
-- Later I used Power BI to create visualisation dashboard.

-- Used this to see all data
SELECT * FROM fetched_books;

-- Updated the price column to get rid of £ sign
UPDATE fetched_books 
SET price = REPLACE(price, '£', '');

-- Deleted a row with null data
DELETE FROM fetched_books
WHERE rating IS NULL;

-- Make price column float, not a varchar
ALTER TABLE fetched_books
ALTER COLUMN price TYPE float8 USING price::float8;

-- 10 most affordable books with rating 5
SELECT 
	title, 
	price, 
	rating 
FROM fetched_books 
WHERE (TRIM(rating) = 'Five') AND (price < 15)
ORDER BY price
LIMIT 10;

-- 10 least affordable books with rating 1
SELECT 
	title, 
	price, 
	rating 
FROM fetched_books 
WHERE (TRIM(rating) = 'One') AND (price > 50)
ORDER BY price DESC
LIMIT 10;

-- How many books are in each category?
SELECT
	COUNT(title),
	rating
FROM fetched_books
GROUP BY rating;

-- In stock percentage:
SELECT 
	(COUNT(*)/
	(SELECT 
		COUNT(title) 
		FROM fetched_books 
		WHERE TRIM(stock) = 'In stock'))*100 || '%' 
		AS percentage_in_stock
FROM fetched_books;








