# Developer Salary Survey Analysis 📊

This project performs an exploratory data analysis (EDA) on a developer survey dataset to uncover insights about industry participation, yearly compensation distribution, salary outliers, and correlations between demographic and compensation-related variables.

The analysis leverages Python data science libraries such as **Pandas**, **Matplotlib**, and **Seaborn** to visualize trends and apply statistical techniques for outlier detection.

---

## 🚀 Features

- 📈 Industry-wise distribution of survey respondents
- 💰 Statistical analysis of yearly compensation
- 🚨 Outlier detection using:
  - Standard Deviation (3σ Rule)
  - Interquartile Range (IQR) Method
- 📦 Data cleaning by removing extreme compensation outliers
- 🔗 Correlation analysis between numeric variables
- 🎨 Visualizations including bar charts, box plots, and heatmaps

---

## 🗂 Dataset

- **File:** `survey_data.csv`
- **Key Columns Used:**
  - `Industry`
  - `ConvertedCompYearly`
  - `Age`

> ⚠️ Ensure the dataset is placed in the project root directory before running the script.

---

## 🛠️ Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- Seaborn

---

## 📊 Analysis Workflow

### 1. Data Loading
Reads survey data from a CSV file into a Pandas DataFrame.

### 2. Industry Distribution
- Counts respondents by industry
- Visualizes results using a bar chart

### 3. Salary Analysis
- Computes mean, median, and standard deviation of yearly compensation
- Identifies extreme high-income outliers using the **3σ rule**

### 4. Outlier Detection (IQR Method)
- Calculates Q1, Q3, and IQR
- Detects and removes salary outliers
- Visualizes compensation spread using a box plot

### 5. Data Cleaning
- Removes extreme compensation values to produce a cleaner dataset

### 6. Correlation Analysis
- Converts age groups into approximate numeric values
- Computes correlation matrix for numeric features
- Displays correlations using a heatmap

---

## 📈 Visualizations Included

- Bar chart: Respondents by industry
- Box plot: Salary distribution and outliers
- Heatmap: Correlation matrix of numeric variables

---

## 📌 Output

* Printed statistical summaries in the console
* Interactive visual plots displayed during execution

---

## 📄 License

This project is licensed under the MIT License. Feel free to use, modify, and distribute.

---

## 🙌 Acknowledgments

* Python open-source data science ecosystem

```

## 🙌 Author

  Varrun Vashisht
