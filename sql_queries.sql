-- Total spending by category
SELECT category, SUM(amount) AS total_spent
FROM expenses
GROUP BY category
ORDER BY total_spent DESC;


-- Monthly spending trend
SELECT substr(expense_date, 1, 7) AS month, SUM(amount) AS total_spent
FROM expenses
GROUP BY month
ORDER BY month;


-- City wise spending 
SELECT city, SUM(amount) AS total_spent
FROM expenses
GROUP BY city;


-- Payment Method Analysis
SELECT payment_method, SUM(amount) AS total_spent
FROM expenses
GROUP BY payment_method;