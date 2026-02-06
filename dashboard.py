import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# st.set_page_config(page_title="Expense Analytics Dashboard", layout="wide")

# Page title
st.title("📊 Expense Analytics Dashboard")


DB_PATH = "expense_data.db"
CSV_PATH = "expenses.csv"
SQL_FILE = "sql_queries.sql"


# Connecting to the database
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    expense_date TEXT,
    category TEXT,
    amount REAL,
    city TEXT,
    payment_method TEXT
)
""")

# Load CSV into DB only if table is empty
row_count = cursor.execute("SELECT COUNT(*) FROM expenses").fetchone()[0]

if row_count == 0:
    df_csv = pd.read_csv(CSV_PATH)
    df_csv.to_sql("expenses", conn, if_exists="append", index=False)
    conn.commit()



# Read sql file
with open("sql_queries.sql", "r") as file:
    sql_content = file.read()

# Split queries by semicolon
queries = [q.strip() for q in sql_content.split(";") if q.strip()]


# 1. Category-wise spending

st.subheader("Category-wise Spending")

df_category = pd.read_sql_query(queries[0], conn)

fig1, ax1 = plt.subplots()
ax1.bar(df_category["category"], df_category["total_spent"])
ax1.set_xlabel("Category")
ax1.set_ylabel("Amount")
ax1.set_title("Total Spending by Category")

st.pyplot(fig1)


# 2. Monthly Spending trend

st.subheader("Monthly Spending Trend")

df_monthly = pd.read_sql_query(queries[1], conn)
df_monthly["month"] = pd.to_datetime(df_monthly["month"])
df_monthly["month_name"] = df_monthly["month"].dt.strftime("%b")

fig2, ax2 = plt.subplots()
ax2.plot(df_monthly["month_name"], df_monthly["total_spent"], marker = "o")
ax2.set_xlabel("Month")
ax2.set_ylabel("Amount")
ax2.set_title("Monthly Spending trend")

st.pyplot(fig2)


# 3. City wise spending

st.subheader("City-wise Spending Distribution")

df_city = pd.read_sql_query(queries[2], conn)

fig3, ax3 = plt.subplots()

ax3.pie(
    df_city["total_spent"],
    labels = df_city["city"],
    autopct = "%1.1f%%"
)

ax3.set_title("City-wise spending")

st.pyplot(fig3)



# Payment method Analysis

st.subheader("Payment wise analysis")

df_payment = pd.read_sql_query(queries[3], conn)

fig4, ax4 = plt.subplots()

ax4.bar(df_payment["payment_method"], df_payment["total_spent"])
ax4.set_xlabel("Payment Method")
ax4.set_ylabel("Amount")
ax4.set_title("Payment Method Analysis")

st.pyplot(fig4)


# Close the connection
conn.close()