import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ai_jobs_updated_2026.csv')
# Compare average salary by Remote Ratio
remote_comparison = df.groupby('remote_work')['annual_salary_usd'].median()

# Visualize the difference
print(remote_comparison)