import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_records = 10000

departments = ['Emergency', 'Cardiology', 'Orthopedics', 'Pediatrics', 'General Surgery']
severities = ['Low', 'Medium', 'High', 'Critical']

start_date = datetime(2025, 1, 1)
data = {
    'patient_id': [f"PAT-{np.random.randint(10000, 99999)}" for _ in range(n_records)],
    'admission_timestamp': [start_date + timedelta(minutes=int(x)) for x in np.random.randint(0, 525600, n_records)],
    'department': np.random.choice(departments, n_records, p=[0.4, 0.15, 0.15, 0.15, 0.15]),
    'triage_severity': np.random.choice(severities, n_records, p=[0.3, 0.4, 0.2, 0.1]),
    'er_wait_time_minutes': np.random.exponential(scale=45, size=n_records).astype(int),
    'length_of_stay_days': np.random.poisson(lam=4, size=n_records) + 1,
    'is_readmitted_30d': np.random.choice([0, 1], n_records, p=[0.85, 0.15]),
    'total_cost_usd': np.random.normal(loc=5000, scale=1500, size=n_records).round(2)
}

df = pd.DataFrame(data)
df.to_csv('data/hospital_operations.csv', index=False)
print("Synthetic dataset generated: data/hospital_operations.csv")