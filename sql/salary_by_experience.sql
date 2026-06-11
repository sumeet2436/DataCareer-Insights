SELECT experience_level,
       ROUND(AVG(salary_in_usd),2) AS avg_salary
FROM fact_salaries
GROUP BY experience_level
ORDER BY avg_salary DESC;