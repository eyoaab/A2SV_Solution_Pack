# Write your MySQL query statement below
SELECT e1.employee_id, e1.name, COUNT(e2.reports_to) AS reports_count, ROUND(AVG(e2.age)) AS average_age
FROM Employees e1
JOIN Employees e2
ON e1.employee_id = e2.reports_to
WHERE e2.reports_to IS NOT NULL
GROUP BY e2.reports_to
ORDER BY e1.employee_id;
