import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#data_url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/n01PQ9pSmiRX6520flujwQ/survey-data.csv'
data_url = 'survey_data.csv'
df = pd.read_csv(data_url)
# print(df.info())

# Count Respondents by Industry
industry_count = df['Industry'].value_counts()
print(industry_count)
# Visualize the date with Bar Chart
plt.figure(figsize = (10,7))
industry_count.plot(kind = 'bar', figsize = (10,5))
plt.title("Distribution of Respondents by Industry")
plt.xlabel("Industry")
plt.ylabel("Number of Respondents")
plt.xticks(rotation = 90)
#plt.show()

print()
# Identify Extremely High Yearly Compensation(Standard Deviation Method)
mean_salary = df['ConvertedCompYearly'].mean()
median_salary = df['ConvertedCompYearly'].median()
std_salary = df['ConvertedCompYearly'].std()

print("Mean:", mean_salary)
print("Median:", median_salary)
print("Standard Deviation:", std_salary)
print()
# Define Outlier Threshold (3σ Rule)
threshold = mean_salary + 3 * std_salary
print("Outlier threshold:", threshold)
print()
# Identify High Compensation Outliers
high_salary_outliers = df[df['ConvertedCompYearly'] > threshold]
total_outliers = high_salary_outliers.shape[0]
print("Total number of outliers:", total_outliers)
print()
print(high_salary_outliers[['ConvertedCompYearly']].head())

# Identify Outliers Using the IQR Method (Very Important)
    # IQR = Interquartile Range
    # It measures the middle 50% of data.

# Step 1: Calculate Quartiles
Q1 = df['ConvertedCompYearly'].quantile(0.25)
Q3 = df['ConvertedCompYearly'].quantile(0.75)
IQR = Q3 - Q1

print("Q1:", Q1)
print("Q3:", Q3)
print("IQR:", IQR)
print()
#Step 2: Define Lower and Upper Bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("Lower bound:", lower_bound)
print("Upper bound:", upper_bound)
print()
iqr_outliers = df[
    (df['ConvertedCompYearly'] < lower_bound) |
    (df['ConvertedCompYearly'] > upper_bound)
]

print("Number of IQR outliers:", iqr_outliers.shape[0])

# Visualize Outliers Using Box Plot
plt.figure(figsize=(6,4))
sns.boxplot(x=df['ConvertedCompYearly'])
plt.title("Box Plot of ConvertedCompYearly")
plt.show()

# Remove Outliers from the Dataset

# Dataframe with correct data not outliers
df_no_outliers = df[
    (df['ConvertedCompYearly'] >= lower_bound) &
    (df['ConvertedCompYearly'] <= upper_bound)
]

print("Original size:", df.shape)
print("After removing outliers:", df_no_outliers.shape)

# Correlation Analysis with Age
# Step 1: Convert Age to Numeric (Approximate)
age_mapping = {
    'Under 18 years old': 16,
    '18-24 years old': 21,
    '25-34 years old': 30,
    '35-44 years old': 40,
    '45-54 years old': 50,
    '55-64 years old': 60,
    '65 years or older': 70
}
df_no_outliers['AgeNumeric'] = df_no_outliers['Age'].map(age_mapping)
# Step 2: Select Numeric Columns
numeric_df = df_no_outliers.select_dtypes(include=['number'])
# Step 3: Compute Correlation Matrix
correlation_matrix = numeric_df.corr()
print(correlation_matrix)
# Step 4: Visualize Correlation Matrix
plt.figure(figsize=(10,8))
sns.heatmap(correlation_matrix, annot=False, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.show()









