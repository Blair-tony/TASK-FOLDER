create database example;
use example;
select * from customer_master;
select * from sales_order1;
 
-- 2
SELECT * FROM customer_master LIMIT 10;
SELECT * FROM sales_order1 LIMIT 10;
 
-- 3
SELECT DISTINCT Item FROM sales_order1;
 
-- 4
SELECT * FROM sales_order1 WHERE UnitCost < 0;
 
 
-- 5
SELECT Item, MIN(UnitCost) AS min_unit_price, MAX(UnitCost) AS max_unit_price
FROM sales_order1
GROUP BY Item;
 
-- 6
SELECT SUM(Total) AS total_sales_2021
FROM sales_order1
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021;
 
-- 7
SELECT Item, SUM(Units) AS total_units_sold
FROM sales_order1
WHERE YEAR(STR_TO_DATE(OrderDate, '%d-%m-%Y')) = 2021
GROUP BY Item
ORDER BY total_units_sold DESC
LIMIT 1;
 
-- 8
SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer_master AS cm
JOIN sales_order1 AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales DESC
LIMIT 1;
 
SELECT cm.Region, SUM(so.Total) AS total_sales
FROM customer_master AS cm
JOIN sales_order1 AS so ON cm.Customer_ID = so.Customer_ID
GROUP BY cm.Region
ORDER BY total_sales ASC
LIMIT 1;
 
-- 9
SELECT cm.Customer, SUM(so.Total) AS total_sales_2022
FROM customer_master AS cm
JOIN sales_order1 AS so ON cm.Customer_ID = so.Customer_ID
WHERE YEAR(STR_TO_DATE(so.OrderDate, '%d-%m-%Y')) = 2022
GROUP BY cm.Customer
ORDER BY total_sales_2022 DESC
LIMIT 1;
 
-- 10
SELECT Item, `UnitCost` AS max_unit_cost
FROM sales_order1
WHERE `UnitCost` = (SELECT MAX(`UnitCost`) FROM sales_order1);
 
SELECT Item, `UnitCost` AS min_unit_cost
FROM sales_order1
WHERE `UnitCost` = (SELECT MIN(`UnitCost`) FROM sales_order1);
 
-- 11
SELECT * FROM sales_order1
WHERE Item LIKE 'P%';
 
-- 12
SELECT * FROM sales_order1
WHERE Item IN ('Pen', 'Pencil');
 
-- 13
SELECT * FROM sales_order1
WHERE `UnitCost` BETWEEN 1 AND 100;
 
-- 14
SELECT Customer_ID, COUNT(*) AS transaction_count
FROM sales_order1
GROUP BY Customer_ID
ORDER BY transaction_count DESC
LIMIT 1;

 
-- 15
WITH regional_sales AS (
    SELECT cm.Region, so.Item, SUM(so.Units) AS total_units_sold,
           ROW_NUMBER() OVER(PARTITION BY cm.Region ORDER BY SUM(so.Units) DESC) AS rank_per_region
    FROM customer_master AS cm
    JOIN sales_order1 AS so ON cm.Customer_ID = so.Customer_ID
    GROUP BY cm.Region, so.Item
)

SELECT Region, Item, total_units_sold
FROM regional_sales
WHERE rank_per_region = 1
ORDER BY Region;

-- 16
-- 1 Calculate the Total Revenue by Month
SELECT YEAR(OrderDate) AS Sales_Year, MONTH(OrderDate) AS Sales_Month, SUM(Total) AS Total_Revenue
FROM sales_order1
GROUP BY Sales_Year, Sales_Month;

-- 2 Identify the Top Selling Item
SELECT Item, SUM(Units) AS Total_Units_Sold
FROM sales_order1
GROUP BY Item
ORDER BY Total_Units_Sold DESC
LIMIT 1;

-- 3 Find Customers Who Have Not Made Purchases
SELECT Customer_ID
FROM customer_master
WHERE Customer_ID NOT IN (SELECT DISTINCT Customer_ID FROM sales_order1);

-- 4 Find Customers with Duplicate Names
SELECT Customer, COUNT(*) AS Name_Count
FROM customer_master
GROUP BY Customer
HAVING Name_Count > 1;

-- 5 Calculate the Total Revenue for Each Region in the Year 2022
SELECT cm.Region, SUM(so.Total) AS Total_Revenue
FROM customer_master AS cm
JOIN sales_order1 AS so ON cm.Customer_ID = so.Customer_ID
WHERE YEAR(so.OrderDate) = 2022
GROUP BY cm.Region;




select * from customer_master;
select * from sales_order1;