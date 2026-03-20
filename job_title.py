import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ai_jobs_updated_2026.csv')
# Group by Job Title and calculate Median Salary
'''
job_rankings = df.groupby('job_title')['annual_salary_usd'].median().sort_values(ascending=False)

# Display the Top 10
print("Top 10 Highest Paying AI Roles (Median):")
print(job_rankings.head(10))

# Visualization
plt.figure(figsize=(10, 6))
job_rankings.head(10).plot(kind='barh', color='teal')
plt.title('Highest Paying AI Roles in 2026')
plt.xlabel('Median Salary (USD)')
plt.gca().invert_yaxis() # Highest at the top
plt.show()
'''
##answer is AI Solutions Architect

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Split the skills into lists and 'explode' them
# This creates a new row for every single skill in the list
df_skills = df.copy()
df_skills['skill'] = df_skills['required_skills'].str.split('|')
df_skills = df_skills.explode('skill')

# 2. Clean up whitespace (important for accurate grouping)
df_skills['skill'] = df_skills['skill'].str.strip()

# 3. Calculate median salary per skill
# We filter for skills that appear at least 10 times to avoid 'lucky' outliers
skill_stats = df_skills.groupby('skill')['annual_salary_usd'].agg(['median', 'count'])
top_skills = skill_stats[skill_stats['count'] > 10].sort_values(by='median', ascending=False)

# 4. Display and Plot the Top 15
print("Top 15 Highest Paying AI Skills (Median USD):")
print(top_skills.head(15))

plt.figure(figsize=(10, 8))
sns.barplot(x=top_skills['median'].head(15), y=top_skills.head(15).index, palette='viridis')
plt.title('Top 15 Highest Paying AI Skills in 2026')
plt.xlabel('Median Annual Salary (USD)')
plt.show()