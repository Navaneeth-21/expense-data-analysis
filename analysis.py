import pandas as pd
import matplotlib.pyplot as plt


# --------------------------- Level-2 (Analysis using python + pandas + SQL) ------------------------------

import sqlite3

#Connect to the database
conn = sqlite3.connect("expense_data.db")

# Read sql file
with open("sql_queries.sql", "r") as file:
    sql_content = file.read()


# Split queries by semicolon
queries = sql_content.strip().split(';')


# 1. Category-wise spending
df_category = pd.read_sql_query(queries[0], conn)

plt.bar(df_category["category"], df_category["total_spent"])
plt.title('Total Spending by Category')
plt.show()


# 2. Monthly Spending Trend
df_monthly = pd.read_sql_query(queries[1], conn)
df_monthly["month"] = pd.to_datetime(df_monthly["month"])
df_monthly["month_name"] = df_monthly["month"].dt.strftime("%b")

plt.plot(df_monthly["month_name"], df_monthly["total_spent"], marker = 'o')
plt.title("Monthly Spending Trend")
plt.show()


# 3. City-wise spending
df_city = pd.read_sql_query(queries[2], conn)

plt.pie(df_city["total_spent"], labels = df_city["city"], autopct = "%1.1f%%" )
plt.title("City-Wise Spending Analysis")
plt.show()


# Payment Method Analysis
df_payment = pd.read_sql_query(queries[3], conn)

plt.bar(df_payment["payment_method"], df_payment["total_spent"])
plt.title("Payment Method Analysis")
plt.show()


# close the connection
conn.close()







"""
# ---------------------------- Level-1 (Analysis using only python and pandas) ----------------------------------

#Load the expense data
df = pd.read_csv('expenses.csv')

#Removing empty rows
df.dropna(inplace = True)

#convert the data column
df['expense_date'] = pd.to_datetime(df['expense_date'])

#Removing duplicates
df.drop_duplicates(inplace = True)

print('Data loaded successfully.....')
print(df.head())

# ----------------------------------- 1. Total Spending Over Time -----------------------------------

# Calculating total spending by category
category_spending = df.groupby('category')['amount'].sum()
print('\n 1. Total Spending by category:')
print(category_spending)


#Plotting total spending by category
category_spending.plot(kind = 'bar', title = 'Total Spending by Category')
plt.xlabel('Category')
plt.ylabel('Total Amount Spent')
plt.tight_layout()
plt.show()


# ----------------------------------- 2. Monthly Spending Trend -----------------------------------

df['month'] = df['expense_date'].dt.to_period('M')
monthly_spending = df.groupby('month')['amount'].sum()
print('\n 2. Monthly Spending Trend:')
print(monthly_spending)

#plotting
monthly_spending.plot(kind = 'line', marker = 'o', title = 'Monthly Spending Trend')
plt.xlabel('Month')
plt.ylabel('Total Amount Spent')
plt.tight_layout()
plt.show()

# ----------------------------------- 3. City-wise Spending Analysis -----------------------------------

city_spending = df.groupby('city')['amount'].sum()
print('\n 3. City-wise Spending Analysis:')
print(city_spending)

#plotting
city_spending.plot(kind = 'pie', autopct = '%1.1f%%', title = 'City-wise Spending Analysis')
plt.ylabel('')
plt.tight_layout()
plt.show()


# ----------------------------------- 4. Payment Method Analysis -----------------------------------

payment_analysis = df.groupby('payment_method')['amount'].sum()
print('\n 4. Payment Method Analysis:')
print(payment_analysis)

#plotting
payment_analysis.plot(kind = 'bar', title = 'Payment Method Analysis')
plt.xlabel('Payment Method')
plt.ylabel('Total Amount Spent')
plt.tight_layout()
plt.show()

"""