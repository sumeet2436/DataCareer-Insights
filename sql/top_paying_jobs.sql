SELECT job_title,
       ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM fact_salaries
GROUP BY job_title
ORDER BY avg_salary DESC
LIMIT 10;