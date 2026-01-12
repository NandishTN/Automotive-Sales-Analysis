SELECT Region, SUM(Revenue) AS Total_Revenue
FROM automotive_sales
GROUP BY Region;

SELECT Model, SUM(Revenue) AS Total_Revenue
FROM automotive_sales
GROUP BY Model
ORDER BY Total_Revenue DESC
LIMIT 10;
