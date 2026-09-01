-- 1. Average ER Wait Time & Length of Stay by Department and Severity
SELECT 
    department,
    triage_severity,
    COUNT(patient_id) AS total_patients,
    ROUND(AVG(er_wait_time_minutes), 1) AS avg_er_wait_mins,
    ROUND(AVG(length_of_stay_days), 1) AS avg_los_days,
    ROUND(SUM(is_readmitted_30d) * 100.0 / COUNT(patient_id), 2) AS readmission_rate_pct
FROM `your_project.hospital_data.operations`
GROUP BY department, triage_severity
ORDER BY department, avg_er_wait_mins DESC;

-- 2. Monthly Hospital Operational Revenue and Readmission Metrics
SELECT 
    DATE_TRUNC(DATE(admission_timestamp), MONTH) AS month_start,
    COUNT(DISTINCT patient_id) AS monthly_admissions,
    ROUND(SUM(total_cost_usd), 2) AS total_revenue_usd,
    ROUND(AVG(er_wait_time_minutes), 1) AS avg_wait_time
FROM `your_project.hospital_data.operations`
GROUP BY month_start
ORDER BY month_start ASC;