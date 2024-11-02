import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data creation
data = {
    'Year': [2020, 2020, 2021, 2021, 2022, 2022, 2023, 2023],
    'Type': ['Phishing', 'Ransomware', 'Phishing', 'Data Breach', 'Ransomware', 'Phishing', 'Data Breach', 'DDoS'],
    'Count': [1500, 200, 2500, 100, 300, 1500, 500, 600],
    'Impact': ['High', 'Critical', 'High', 'Medium', 'Critical', 'High', 'Medium', 'High']
}

# Data for attacks in India
india_data = {
    'Industry': ['Finance', 'Healthcare', 'Retail', 'Education', 'Government'],
    'India_Count': [800, 300, 500, 150, 250],
}

df = pd.DataFrame(data)
india_df = pd.DataFrame(india_data)

# Set the aesthetics for seaborn
sns.set(style="whitegrid")

# 1. Bar Graph: Count of Cyberattacks by Year
plt.figure(figsize=(10, 5))
bar_plot = df.groupby('Year')['Count'].sum().plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Total Cyberattacks by Year', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Cyberattacks', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for rect in bar_plot.patches:
    height = rect.get_height()
    bar_plot.annotate(f'{height}', (rect.get_x() + rect.get_width() / 2, height), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()

# 2. Pie Chart: Distribution of Cyberattack Types
plt.figure(figsize=(8, 8))
sizes = df['Type'].value_counts()
explode = [0.1 if i == sizes.idxmax() else 0 for i in sizes.index]
sizes.plot(kind='pie', autopct='%1.1f%%', startangle=90, colors=sns.color_palette('Set2'), explode=explode)
plt.title('Distribution of Cyberattack Types', fontsize=16)
plt.ylabel('')
plt.tight_layout()
plt.show()

# 3. Line Graph: Trend of Phishing Attacks Over Years
phishing_data = df[df['Type'] == 'Phishing']
plt.figure(figsize=(10, 5))
plt.plot(phishing_data['Year'], phishing_data['Count'], marker='o', color='orange', linewidth=2, label='Phishing Attacks')
plt.fill_between(phishing_data['Year'], phishing_data['Count'], color='orange', alpha=0.1)
plt.title('Trend of Phishing Attacks Over Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Phishing Attacks', fontsize=12)
plt.xticks(phishing_data['Year'])
plt.grid()
plt.legend()
plt.tight_layout()
plt.show()

# 4. Heatmap: Cyberattacks Impact
impact_data = pd.crosstab(df['Year'], df['Impact'])
plt.figure(figsize=(8, 6))
sns.heatmap(impact_data, annot=True, cmap='YlGnBu', fmt='d', linewidths=.5, cbar_kws={'label': 'Count'})
plt.title('Impact of Cyberattacks by Year', fontsize=16)
plt.ylabel('Year', fontsize=12)
plt.xlabel('Impact Level', fontsize=12)
plt.tight_layout()
plt.show()

# 5. Stacked Bar Chart: Cyberattack Types Over Years
df_pivot = df.pivot_table(index='Year', columns='Type', values='Count', aggfunc='sum', fill_value=0)
df_pivot.plot(kind='bar', stacked=True, figsize=(10, 5), colormap='Set3')
plt.title('Cyberattack Types Over Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Cyberattacks', fontsize=12)
plt.xticks(rotation=45)
plt.legend(title='Cyberattack Types')
plt.tight_layout()
plt.show()

# 6. Box Plot: Count of Cyberattacks by Impact
plt.figure(figsize=(10, 5))
sns.boxplot(x='Impact', y='Count', data=df, palette='pastel')
sns.swarmplot(x='Impact', y='Count', data=df, color='.25')
plt.title('Distribution of Cyberattacks Count by Impact Level', fontsize=16)
plt.xlabel('Impact Level', fontsize=12)
plt.ylabel('Number of Cyberattacks', fontsize=12)
plt.tight_layout()
plt.show()

# 7. Scatter Plot: Year vs. Count of Cyberattacks
plt.figure(figsize=(10, 5))
sns.regplot(x='Year', y='Count', data=df, scatter_kws={'color': 'red', 'alpha': 0.7}, line_kws={'color': 'blue'})
plt.title('Scatter Plot of Year vs. Count of Cyberattacks', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Number of Cyberattacks', fontsize=12)
plt.grid()
plt.tight_layout()
plt.show()

# 8. Area Chart: Cumulative Cyberattacks Over Years
cumulative_data = df.groupby('Year')['Count'].sum().cumsum()
plt.figure(figsize=(10, 5))
plt.fill_between(cumulative_data.index, cumulative_data, color='skyblue', alpha=0.4)
plt.plot(cumulative_data.index, cumulative_data, color='Slateblue', alpha=0.6, linewidth=2)
plt.title('Cumulative Cyberattacks Over Years', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Cumulative Number of Cyberattacks', fontsize=12)
plt.grid()
plt.tight_layout()
plt.show()

# 9. Bar Chart: Cyberattacks in India by Industry
plt.figure(figsize=(10, 5))
india_df.set_index('Industry')['India_Count'].plot(kind='bar', color='lightcoral', edgecolor='black')
plt.title('Cyberattacks in India by Industry', fontsize=16)
plt.xlabel('Industry', fontsize=12)
plt.ylabel('Number of Cyberattacks', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
for rect in plt.gca().patches:
    height = rect.get_height()
    plt.gca().annotate(f'{height}', (rect.get_x() + rect.get_width() / 2, height), ha='center', va='bottom', fontsize=10)
plt.tight_layout()
plt.show()

# 10. Total Percentage of Cyberattacks in India
total_india_attacks = india_df['India_Count'].sum()
total_cyberattacks = df['Count'].sum()
india_percentage = (total_india_attacks / total_cyberattacks) * 100

# Display the percentage of attacks in India
print(f'Total Cyberattacks in India: {total_india_attacks}')
print(f'Total Cyberattacks Worldwide: {total_cyberattacks}')
print(f'Percentage of Cyberattacks in India: {india_percentage:.2f}%')

# 11. Pie Chart: Percentage of Cyberattacks in India vs. Worldwide
plt.figure(figsize=(8, 8))
labels = ['Cyberattacks in India', 'Cyberattacks Worldwide']
sizes = [total_india_attacks, total_cyberattacks - total_india_attacks]
colors = ['lightcoral', 'lightblue']
explode = (0.1, 0)  # explode the Indian attacks slice
plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
plt.title('Percentage of Cyberattacks: India vs. Worldwide', fontsize=16)
plt.axis('equal')  # Equal aspect ratio ensures the pie chart is circular.
plt.tight_layout()
plt.show()
