-- SELECT
SELECT * FROM superstore;

-- WHERE
SELECT *
FROM superstore
WHERE Sales > 200;

-- ORDER BY
SELECT "Customer Name", Sales, Profit
FROM superstore
ORDER BY Sales DESC;

-- LIMIT
SELECT *
FROM superstore
LIMIT 10;

-- GROUP BY
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

-- HAVING
SELECT Category, SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category
HAVING SUM(Sales) > 200000;

-- INNER JOIN
SELECT
    s.Region,
    rm.Manager,
    SUM(s.Sales) AS Total_Sales
FROM superstore s
INNER JOIN region_manager rm
ON s.Region = rm.Region
GROUP BY s.Region, rm.Manager;

-- SUBQUERY
SELECT *
FROM superstore
WHERE Sales >
(
    SELECT AVG(Sales)
    FROM superstore
);

-- CTE
WITH category_sales AS
(
    SELECT Category,
           SUM(Sales) AS Total_Sales
    FROM superstore
    GROUP BY Category
)
SELECT * FROM category_sales;

-- ROW_NUMBER
SELECT
    "Customer Name",
    Sales,
    ROW_NUMBER() OVER (ORDER BY Sales DESC) AS Row_Num
FROM superstore;

-- RANK
SELECT
    "Customer Name",
    Sales,
    RANK() OVER (ORDER BY Sales DESC) AS Sales_Rank
FROM superstore;

-- LAG
SELECT
    "Order Date",
    Sales,
    LAG(Sales) OVER (ORDER BY "Order Date") AS Previous_Sale
FROM superstore;

-- LEAD
SELECT
    "Order Date",
    Sales,
    LEAD(Sales) OVER (ORDER BY "Order Date") AS Next_Sale
FROM superstore;

-- VIEW
CREATE VIEW high_sales AS
SELECT *
FROM superstore
WHERE Sales > 200;

SELECT * FROM high_sales;