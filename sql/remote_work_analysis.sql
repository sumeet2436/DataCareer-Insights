SELECT remote_ratio,
       COUNT(*) AS total_jobs
FROM fact_salaries
GROUP BY remote_ratio
ORDER BY remote_ratio;