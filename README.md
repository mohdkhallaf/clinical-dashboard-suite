# 📊 Clinical Dashboard & Operational Performance Suite

[![SQL](https://img.shields.io/badge/SQL-BigQuery-blue.svg)](https://cloud.google.com/bigquery)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboard-yellow.svg)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-green.svg)](https://www.python.org/)

An enterprise-grade healthcare analytics solution designed to evaluate hospital operational efficiency, monitor ER wait times, bed occupancy, and 30-day readmission metrics across clinical departments.

## 📌 Architecture
1. **Data Pipeline:** Python generation script creating synthetic hospital operations data (10,000+ patient records).
2. **Data Warehouse:** Google BigQuery star-schema model.
3. **Analytics Engine:** SQL aggregation views tracking KPI shifts by severity and department.
4. **Visualization:** Interactive Power BI executive dashboard with dynamic filtering.
```[cite: 1]