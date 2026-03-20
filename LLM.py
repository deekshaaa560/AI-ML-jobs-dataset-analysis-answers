import pandas as pd
df=pd.read_csv('ai_jobs_updated_2026.csv')

# Define keywords associated with LLMs and Generative AI
llm_keywords = ['llms','llm fine-tuning', 'llm', 'generative ai', 'genai', 'transformer', 'langchain', 'bert', 'gpt', 'nlp', 'prompt engineering']

# Create a function to flag the rows
def check_llm(row):
    # Check both the job title and the required skills (lowercase for matching)
    content = str(row['job_title']).lower() + " " + str(row['required_skills']).lower()
    if any(keyword in content for keyword in llm_keywords):
        return 'LLM / GenAI'
    return 'Traditional AI/ML'

# Apply the function to your dataframe
df['tech_stack'] = df.apply(check_llm, axis=1)


# Statistical Comparison
salary_comparison = df.groupby('tech_stack')['annual_salary_usd'].agg(['mean', 'median', 'count'])
print(salary_comparison)

# Calculate the "LLM Premium" percentage
premium = ((salary_comparison.loc['LLM / GenAI', 'median'] / 
            salary_comparison.loc['Traditional AI/ML', 'median']) - 1) * 100

print(f"\nOn average, LLM-related roles pay {premium:.2f}% more than traditional AI roles.")

