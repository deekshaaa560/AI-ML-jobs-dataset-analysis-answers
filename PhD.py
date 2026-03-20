#Is a PhD worth it for AI roles?
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('ai_jobs_updated_2026.csv')
'''
# 1. Calculate the mean and sort it (sorting makes the chart much easier to read!)
salary_by_edu = tabular_data.groupby('education_required')['annual_salary_usd'].median().sort_values(ascending=False)

# 2. Plot as a bar chart
salary_by_edu.plot(kind='barh', figsize=(10, 6), color='skyblue')

# 3. Add labels and title
plt.title('Average Annual Salary by Education Level')
plt.xlabel('Average Salary (USD)')
plt.ylabel('Education Required')
plt.xticks(rotation=45) # Rotates the labels so they don't overlap
plt.show()  ##here it shows that with a PhD- an employee may be earning more than other degree holders.

'''
##Let's check if master's or bachelor's + experience(atleast 5 yrs) comes even near to an entry level PhD employee or not

# 1. Define the Groups
phd_entry = df[(df['education_required'] == 'PhD') & (df['years_of_experience'] <= 2)]
industry_5yr = df[((df['education_required'] == "Master's") | (df['education_required'] == "Bachelor's")) & 
                  (df['years_of_experience'] == 5)]

# 2. Calculate Medians
med_phd = phd_entry['annual_salary_usd'].median()
med_ind = industry_5yr['annual_salary_usd'].median()

print(f"Median Salary - Entry PhD: ${med_phd:,.0f}")
print(f"Median Salary - 5yr Industry (Master's/Bachelor's): ${med_ind:,.0f}")

# 3. Visualization for your project
plt.figure(figsize=(8, 6))
plt.bar(['PhD Entry-Level', 'Master/Bachelor (5 yrs)'], [med_phd, med_ind], color=['#4C72B0', '#55A868'])
plt.title('Is a PhD Worth It? (Salary Comparison)')
plt.ylabel('Median Annual Salary (USD)')
plt.show()


