
<div align="center">

# 📊 Python Data Analysis Journey

### From Numerical Computing to Decision-Ready Insights

**A Complete Python Data Analysis Learning Repository & Project Portfolio**

[![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![NumPy](https://img.shields.io/badge/NumPy-Numerical_Computing-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
[![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge)](https://matplotlib.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-Statistics-4C72B0?style=for-the-badge)](https://seaborn.pydata.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**[Learning Roadmap](#-learning-roadmap) • [Real-World Projects](#-real-world-projects) • [Installation](#-getting-started) • [Author](#-author)**

</div>

---

## 🎯 About This Repository

**Python Data Analysis Journey** is a structured, practical, and comprehensive repository demonstrating essential data analysis concepts using Python and its ecosystem of powerful libraries.

The repository progresses from **NumPy fundamentals and Pandas DataFrames** to advanced data manipulation, statistics, visualization, exploratory data analysis, SQL integration, and complete real-world-style projects.

It emphasizes three major principles:

- **Understand the concepts** rather than simply memorize syntax.
- **Build practical implementations** using clean, reusable Python code.
- **Convert data into insights** through reliable analysis and visualization.

The repository is designed for students, aspiring data analysts, AI/ML enthusiasts, developers, and technical recruiters.

---

## 🧰 Technologies and Tools

| Technology | Purpose |
|:---|:---|
| Python 3.11+ | Core programming and data processing |
| NumPy | Numerical computing and multidimensional arrays |
| Pandas | Data manipulation and structured data analysis |
| SciPy | Probability, distributions, and statistical tests |
| Matplotlib | Data visualization and scientific plotting |
| Seaborn | Statistical data visualization |
| MySQL | Relational database storage and queries |
| SQLAlchemy | Database connectivity and SQL integration |
| MySQL Connector | MySQL driver for Python |
| python-dotenv | Environment variable configuration |
| pytest | Automated Python testing |
| Ruff | Code formatting and linting |
| Git & GitHub | Version control and project documentation |

---

## 🎓 Learning Objectives

This repository demonstrates how to:

1. Create and manipulate multidimensional NumPy arrays.
2. Work with Pandas Series and DataFrames.
3. Import, export, filter, and transform datasets.
4. Detect and handle missing, duplicated, and inconsistent values.
5. Perform grouping, merging, aggregation, and pivot operations.
6. Apply descriptive statistics and probability concepts.
7. Understand correlations, distributions, and statistical relationships.
8. Create informative charts using Matplotlib and Seaborn.
9. Perform univariate, bivariate, and multivariate analysis.
10. Integrate SQL databases with Python.
11. Build reproducible end-to-end data analysis projects.
12. Communicate useful findings through clear visualizations and reports.

---

## 🗺️ Learning Roadmap

| Module | Topic | Key Concepts |
|:---:|:---|:---|
| 01 | NumPy Fundamentals | Arrays, indexing, slicing, operations, broadcasting, linear algebra |
| 02 | Pandas Fundamentals | Series, DataFrames, reading files, filtering, sorting, indexing |
| 03 | Data Cleaning | Missing values, duplicates, data types, outliers |
| 04 | Data Manipulation | GroupBy, merging, joins, pivot tables, transformations |
| 05 | Statistics | Descriptive statistics, probability, correlation, distributions |
| 06 | Data Visualization | Matplotlib, Seaborn, line, bar, scatter, histograms |
| 07 | Exploratory Data Analysis | Univariate, bivariate, multivariate analysis |
| 08 | SQL-Python Integration | MySQL connections, parameterized queries, DataFrames |
| 09 | Real-World Projects | Student performance, e-commerce, air quality |
| 10 | Quality Assurance | Testing, linting, validation, reproducibility |

---

## 📂 Repository Structure

```text
Python-Data-Analysis-Journey/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
├── LICENSE
├── pyproject.toml
│
├── 01_NumPy_Fundamentals/
│   ├── 01_arrays.py
│   ├── 02_indexing_slicing.py
│   ├── 03_array_operations.py
│   ├── 04_broadcasting.py
│   └── 05_linear_algebra.py
│
├── 02_Pandas_Fundamentals/
│   ├── 01_series.py
│   ├── 02_dataframes.py
│   ├── 03_reading_files.py
│   ├── 04_filtering_sorting.py
│   └── 05_indexing.py
│
├── 03_Data_Cleaning/
│   ├── 01_missing_values.py
│   ├── 02_duplicates.py
│   ├── 03_data_types.py
│   └── 04_outliers.py
│
├── 04_Data_Manipulation/
│   ├── 01_groupby.py
│   ├── 02_merge_join.py
│   ├── 03_pivot_tables.py
│   └── 04_transformations.py
│
├── 05_Statistics/
│   ├── 01_descriptive_statistics.py
│   ├── 02_probability.py
│   ├── 03_correlation.py
│   └── 04_distributions.py
│
├── 06_Data_Visualization/
│   ├── 01_matplotlib_basics.py
│   ├── 02_line_bar_charts.py
│   ├── 03_scatter_histograms.py
│   └── 04_seaborn_visualizations.py
│
├── 07_Exploratory_Data_Analysis/
│   ├── 01_univariate_analysis.py
│   ├── 02_bivariate_analysis.py
│   └── 03_feature_relationships.py
│
├── 08_SQL_Python_Integration/
│   ├── 01_database_connection.py
│   ├── 02_sql_to_dataframe.py
│   └── 03_data_analysis.py
│
├── 09_Real_World_Projects/
│   │
│   ├── Student_Performance_Analysis/
│   │   ├── README.md
│   │   ├── generate_data.py
│   │   └── main.py
│   │
│   ├── ECommerce_Sales_Analysis/
│   │   ├── README.md
│   │   ├── generate_data.py
│   │   └── main.py
│   │
│   └── Air_Quality_Data_Analysis/
│       ├── README.md
│       ├── generate_data.py
│       └── main.py
│
├── datasets/
│   └── README.md
│
└── tests/
    ├── test_data_cleaning.py
    └── test_project_pipelines.py
```

---

## 📘 Module Documentation

<details>
<summary><strong>01 — NumPy Fundamentals</strong></summary>

NumPy provides efficient numerical computation using multidimensional arrays.

### Concepts Covered

- Array creation and initialization
- Array dimensions, shapes, and data types
- Indexing and slicing
- Vectorized mathematical operations
- Broadcasting
- Reshaping and flattening
- Statistical operations
- Linear algebra and matrix operations

### Learning Outcome

Understand how NumPy improves numerical computation through vectorization and efficient array processing.

</details>

<details>
<summary><strong>02 — Pandas Fundamentals</strong></summary>

Pandas provides powerful tools for working with structured and tabular data.

### Concepts Covered

- Series and DataFrames
- Reading CSV and JSON files
- Indexing with `loc` and `iloc`
- Filtering and sorting records
- Selecting and modifying columns
- Descriptive summaries
- Exporting processed data

### Learning Outcome

Learn to explore, organize, and transform tabular datasets efficiently.

</details>

<details>
<summary><strong>03 — Data Cleaning</strong></summary>

Real datasets often contain missing, duplicated, incorrect, and inconsistent values.

### Concepts Covered

- Missing-value detection
- Imputation and removal strategies
- Duplicate detection and handling
- Data type conversion
- Outlier identification
- Data validation
- Reusable cleaning functions

### Learning Outcome

Create reliable datasets for further analysis while documenting important cleaning decisions.

</details>

<details>
<summary><strong>04 — Data Manipulation</strong></summary>

Data manipulation converts raw information into structured analytical results.

### Concepts Covered

- Grouping and aggregation
- Merging and joining DataFrames
- Pivot tables
- Reshaping
- Column transformations
- Date and time operations
- Derived features

### Learning Outcome

Perform advanced analytical transformations using Pandas.

</details>

<details>
<summary><strong>05 — Statistics</strong></summary>

Statistics provides the mathematical foundation for understanding data.

### Concepts Covered

- Mean, median, and mode
- Variance and standard deviation
- Percentiles and quartiles
- Probability
- Common probability distributions
- Correlation and covariance
- Introductory hypothesis testing

### Learning Outcome

Interpret quantitative relationships and variation using statistical methods.

</details>

<details>
<summary><strong>06 — Data Visualization</strong></summary>

Visualization transforms numerical information into understandable graphical representations.

### Concepts Covered

- Matplotlib fundamentals
- Line charts
- Bar charts
- Scatter plots
- Histograms
- Box plots
- Heatmaps
- Seaborn statistical charts
- Labels, legends, and styling

### Learning Outcome

Create informative visualizations that communicate analytical findings clearly.

</details>

<details>
<summary><strong>07 — Exploratory Data Analysis</strong></summary>

EDA identifies patterns, anomalies, trends, and relationships within datasets.

### Concepts Covered

- Univariate analysis
- Bivariate analysis
- Multivariate analysis
- Correlation analysis
- Feature relationships
- Missing-data exploration
- Statistical summaries
- Interpretation of findings

### Learning Outcome

Conduct systematic exploratory analysis before developing predictive models or making analytical conclusions.

</details>

<details>
<summary><strong>08 — SQL and Python Integration</strong></summary>

SQL integration allows Python to analyze data stored in relational databases.

### Concepts Covered

- MySQL database connections
- Secure environment configuration
- Parameterized SQL queries
- SQLAlchemy integration
- Importing query results into Pandas
- Database aggregations
- Combined SQL and Python analysis

### Learning Outcome

Build database-driven analytical workflows with secure, maintainable Python implementations.

</details>

---

## 🏆 Real-World Projects

The repository contains three end-to-end analytical case studies.

Each project follows this workflow:

**Data Generation → Validation → Cleaning → Transformation → EDA → Visualization → Insights**

### 🎓 Project 1 — Student Performance Analysis

**Directory:** `09_Real_World_Projects/Student_Performance_Analysis/`

Investigates relationships between student performance and academic indicators.

**Analysis Includes:**

- Student score distributions
- Attendance and academic performance
- Study time and assessment results
- Subject-wise performance
- Correlation analysis
- Group comparisons
- Actionable educational insights

**Skills:** Pandas, statistics, data cleaning, Matplotlib, Seaborn, EDA.

### 🛒 Project 2 — E-Commerce Sales Analysis

**Directory:** `09_Real_World_Projects/ECommerce_Sales_Analysis/`

Analyzes simulated commercial transactions to identify sales patterns.

**Analysis Includes:**

- Total revenue
- Order statistics
- Product performance
- Category-wise sales
- Revenue trends
- Sales comparisons
- Business performance insights

**Skills:** Aggregation, grouping, time series, business analytics, visualization.

### 🌍 Project 3 — Air Quality Data Analysis

**Directory:** `09_Real_World_Projects/Air_Quality_Data_Analysis/`

Explores simulated air-quality measurements across locations and time periods.

**Analysis Includes:**

- Pollutant distributions
- Location-based comparisons
- Time-based trends
- Correlation between pollutants
- Outlier analysis
- Environmental data visualization
- Interpretations of measurement patterns

**Skills:** Data cleaning, descriptive statistics, EDA, visualization.

> **Dataset Transparency:** All three project generators produce synthetic data for educational purposes. These records are not actual student results, commercial transactions, or environmental measurements. Findings are based on the simulated datasets rather than real-world observations.

---

## 🚀 Getting Started

### Prerequisites

Ensure that the following tools are installed:

- Python 3.11 or newer
- pip
- Git
- VS Code or another Python editor
- MySQL Server for SQL integration examples

### Step 1 — Clone the Repository

```bash
git clone https://github.com/k-m-rahaman/Python-Data-Analysis-Journey.git
cd Python-Data-Analysis-Journey
```

### Step 2 — Create a Virtual Environment

**Windows PowerShell**

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Git Bash (Windows)**

```bash
py -3 -m venv .venv
source .venv/Scripts/activate
```

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

A virtual environment keeps project dependencies separate from your system-wide Python installation.

### Step 3 — Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4 — Run Python Programs

Run scripts from the repository root.

**NumPy example:**

```bash
python 01_NumPy_Fundamentals/01_arrays.py
```

**Pandas example:**

```bash
python 02_Pandas_Fundamentals/02_dataframes.py
```

**Statistics example:**

```bash
python 05_Statistics/01_descriptive_statistics.py
```

### Step 5 — Run a Complete Project

Generate the student-performance dataset:

```bash
python 09_Real_World_Projects/Student_Performance_Analysis/generate_data.py
```

Execute the analysis:

```bash
python 09_Real_World_Projects/Student_Performance_Analysis/main.py
```

The other two projects use the same `generate_data.py` and `main.py` convention.

---

## 💻 Example: Analyzing Student Scores

```python
import numpy as np
import pandas as pd

students = pd.DataFrame(
    {
        "name": ["Asha", "Rahul", "Mira", "Arjun"],
        "marks": [85, 76, 92, 81],
    }
)

average_marks = np.mean(students["marks"].to_numpy())
highest_marks = students["marks"].max()

print(f"Average Marks: {average_marks:.2f}")
print(f"Highest Marks: {highest_marks}")
```

**Expected Output:**

```text
Average Marks: 83.50
Highest Marks: 92
```

This example demonstrates how NumPy and Pandas work together to analyze tabular data.

---

## 🗄️ SQL Database Configuration

The SQL-Python module connects to a MySQL database.

Copy the environment template to a local `.env` file:

**PowerShell**

```powershell
Copy-Item .env.example .env
```

**Git Bash**

```bash
cp .env.example .env
```

Edit `.env` with your local connection credentials:

```dotenv
MYSQL_HOST=localhost
MYSQL_PORT=3306
MYSQL_USER=analysis_reader
MYSQL_PASSWORD=your_local_password
MYSQL_DATABASE=analytics_lab
```

Run the database connection example:

```bash
python 08_SQL_Python_Integration/01_database_connection.py
```

> Never commit `.env`, passwords, access tokens, or other secrets to GitHub. Database examples use parameterized SQL queries where appropriate.

---

## ✅ Testing and Code Quality

The repository includes configuration for automated quality checks.

**Run tests:**

```bash
python -m pytest
```

**Check code quality:**

```bash
python -m ruff check .
```

**Check formatting:**

```bash
python -m ruff format --check .
```

The Python implementations follow these principles:

- Clear and meaningful function names
- Modular implementations
- PEP 8-oriented formatting
- Relevant docstrings and comments
- Appropriate type hints
- Error handling and input validation
- Portable paths
- Reproducible analytical procedures
- Transparent documentation

---

## 📊 Skills Demonstrated

| Technical Skills | Professional Practices |
|:---|:---|
| Numerical Computing | Modular Code Organization |
| Data Cleaning | Version Control |
| Data Manipulation | Documentation |
| Statistical Analysis | Error Handling |
| Data Visualization | Reproducible Execution |
| Exploratory Data Analysis | Testing and Linting |
| SQL Integration | Secure Configuration |
| Analytical Reporting | Communication of Insights |

---

## 📚 References

Official documentation used throughout the repository:

- [Python](https://docs.python.org/3/)
- [NumPy](https://numpy.org/doc/stable/)
- [Pandas](https://pandas.pydata.org/docs/)
- [SciPy](https://docs.scipy.org/doc/scipy/)
- [Matplotlib](https://matplotlib.org/stable/)
- [Seaborn](https://seaborn.pydata.org/)
- [SQLAlchemy](https://docs.sqlalchemy.org/)
- [pytest](https://docs.pytest.org/)
- [Ruff](https://docs.astral.sh/ruff/)

---

## 👨‍💻 Author

<div align="center">

### Kazi Mustafijur Rahaman

**B.Tech in Computer Science & Engineering (AI & ML)**

Passionate about Python, Artificial Intelligence, Machine Learning, Data Analysis, and Software Development.

[![GitHub](https://img.shields.io/badge/GitHub-k--m--rahaman-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/k-m-rahaman)

</div>

---

## 📄 License

This project is licensed under the MIT License.

See the [LICENSE](LICENSE) file for details.

---

<div align="center">

### ⭐ Learn. Analyze. Visualize. Improve.

**Turning data into understanding, one Python project at a time.**

</div>
