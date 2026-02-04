import pandas as pd
import sqlite3

# Read CSV 
df = pd.read_csv('expenses.csv')

# Connect to sqlite database
conn = sqlite3.connect("expense_data.db")

# Move the data into sql database
df.to_sql("expenses", conn, if_exists = 'replace', index = 'False')

conn.close()
print(' CSV Data loaded into sql database successfully')