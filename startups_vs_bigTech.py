import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ai_jobs_updated_2026.csv')
distinct_sizes=df['company_size'].unique()
'''
salaries_in_size=df.groupby('company_size')['annual_salary_usd'].median()

print(distinct_sizes)
print(salaries_in_size)

##A boxplot to understand size of the company and salaries
sns.boxplot(data=df, x='company_size', y='annual_salary_usd')

plt.title('size_vs_salary')
plt.xlabel('Size')
plt.ylabel('salary (usd)')
plt.show()  ##This shows though big techs pay more comparitively higher in general but there are some outliers that suggest, for some job_titles or maybe some employees, startups are ready to pay competitively.
'''

##1.startups + job_title vs big tech + job_title
##2. startups + experience vs big tech + experience
##3. Entry levels on both

##1.

'''
plt.figure(figsize=(14, 7))
sns.barplot(data=df, x='job_category', y='annual_salary_usd', hue='company_size', ci=None)

plt.title('Salary Comparison: On the basis of Job category')
plt.ylabel('Average Salary (USD)')
plt.xlabel('Job Category')
plt.legend(title='Company Size (S=Startup, L=Big Tech)')
plt.show()  ##Big techs pay more.
'''

##2. 
'''
plt.figure(figsize=(14, 7))
sns.barplot(data=df, x='years_of_experience', y='annual_salary_usd', hue='company_size', errorbar=None)

plt.title('Salary Comparison: On the basis of years of experience')
plt.ylabel('Average Salary (USD)')
plt.xlabel('Years of Experience')
plt.legend(title='Company Size (S=Startup, L=Big Tech)')
plt.show()
'''

# --- STEP 1: Define the "Great Pay" Outliers ---
startups = df[df['company_size'].isin(['Startup (1-50)'])]
Q1 = startups['annual_salary_usd'].quantile(0.25)
Q3 = startups['annual_salary_usd'].quantile(0.75)
IQR = Q3 - Q1
startup_outliers = startups[startups['annual_salary_usd'] > (Q3 + 1.5 * IQR)]

# --- STEP 2: Extract the "Who are they?" info ---
print("--- THE STARTUP 'OUTLIER' PROFILE ---")

# 1. What are their Job Titles?
print("\nTop 10 Job Titles for High Earners:")
print(startup_outliers['job_category'].value_counts().head(10))

# 2. What is their Experience Level?
print("\nExperience Level Distribution:")
print(startup_outliers['years_of_experience'].value_counts().head(10))

# 3. Where are they located?
print("\nTop 10 Locations for High Earners:")
print(startup_outliers['country'].value_counts().head(10))

# 4. Are they Remote?
print("\nRemote Work? :")
print(startup_outliers['remote_work'].value_counts().head(10))

#5. What is their industry?
print("\n Industry type: ")
print(startup_outliers['industry'].value_counts().head(10))