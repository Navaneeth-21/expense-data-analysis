# Expense Data Analysis using Python & SQL

## 📌 Project Overview
This project focuses on analyzing transactional expense data to extract meaningful insights.
It demonstrates a step-by-step evolution from basic CSV-based analysis to SQL-powered analytics
using Python.

The project is built in **levels**, showing progressive enhancement of data analytics skills.


## 🧱 Tech Stack
- Python
- Pandas
- SQLite
- Matplotlib
- SQL


## 📁 Project Structure
   expense-data-analysis/
   │
   ├── expenses.csv # Source dataset
   ├── load_to_db.py # Loads CSV data into SQLite database
   ├── analysis.py # Executes SQL queries and generates charts
   ├── sql_queries.sql # SQL queries for analytics
   ├── requirements.txt
   ├── README.md
   └── .gitignore


## 🚀 Level 1: CSV-Based Data Analysis (Basic)

### Description
In Level 1, expense data is analyzed directly from a CSV file using Python and Pandas.
The goal is to understand the dataset and perform basic aggregations and visualizations.

### Features
- Load CSV data using Pandas
- Category-wise expense aggregation
- Monthly spending trend analysis
- City-wise and payment-method analysis
- Data visualization using Matplotlib

### Skills Demonstrated
- Data cleaning and preprocessing
- Pandas `groupby` operations
- Basic data visualization
- Python scripting

## ▶️ How to run only this level-1
1. Comment out the level-2 part in analysis.py
2. Uncomment the level-1 part in analysis.py
3. Install dependencies
```bash
   pip install -r requirements.txt
```
4. Run in terminal
```bash
   python analysis.py
```



## 🚀 Level 2: SQL-Based Data Analysis (Expansion)

### Description
In Level 2, the project is expanded by introducing an SQL database.
The CSV data is loaded into an SQLite database, and all analytics are performed using SQL queries.
Python is used to execute queries and visualize results.

### Features
- Load CSV data into SQLite3 database
- Write reusable SQL queries for analytics
- Execute SQL queries using Python
- Generate charts from SQL query results

### SQL Queries Implemented
- Category-wise total spending
- Monthly spending trend
- City-wise spending distribution
- Payment method usage analysis

### Skills Demonstrated
- SQL aggregation and grouping
- SQLite database handling
- Python–SQL integration
- Data-driven visualization
- Clean project architecture


## 📊 Visualizations
- Bar chart for category-wise spending and payment methods
- Line chart for monthly spending trends
- Pie chart for city-wise spending

## ▶️ How to Run 

### 1. Install dependencies
```bash
   pip install -r requirements.txt
```

2. Load CSV data into database
```bash
   python load_to_db.py
```

3. Run analysis and generate charts
```bash
   python analysis.py
```

## 🚀 Level 3: Interactive Dashboard

### Description
An interactive dashboard built using Streamlit to visualize SQL-based expense analytics.
The dashboard presents category-wise, monthly, city-wise and payment method spending insights in a user-friendly web interface.

### Features
- Interactive web dashboard
- Charts generated from SQL query results
- Clean and minimal UI
- End-to-end data pipeline visualization

## ▶️ How to Run 

### 1. Install dependencies
```bash
   pip install -r requirements.txt
```
2. Run the following command 
```bash
   streamlit run dashboard.py
```
3. You'll be redirected to local url in your web browser
