import pandas as pd

import matplotlib.pyplot as plt

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