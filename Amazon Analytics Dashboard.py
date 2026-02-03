import pandas as pd
df = pd.read_csv("amazon_india_states_monthly_2024.csv")
print(df.head())
print(df.info())
print(df.describe())
print("States:", df['state'].nunique())
print("Months:", df['month'].nunique())
state_summary = df.groupby("state")[["total_orders", "total_revenue"]].sum().sort_values(by="total_revenue", ascending=False)
print(state_summary)
monthly_summary = df.groupby("month")[["total_orders", "total_revenue"]].sum()

print(monthly_summary)
top_states = state_summary.head(5)
print("Top 5 States by Revenue:\n", top_states)
import matplotlib.pyplot as plt
state_summary["total_revenue"].plot(kind="bar", figsize=(12,6), title="Total Revenue by State")
plt.ylabel("Revenue (INR)")
plt.show()
monthly_summary["total_orders"].plot(kind="line", marker="o", figsize=(10,5), title="Monthly Orders Trend (All States)")
plt.ylabel("Total Orders")
plt.show()
maha = df[df['state'] == "Maharashtra"]

plt.plot(maha['month'], maha['total_revenue'], marker="o")
plt.title("Maharashtra - Monthly Revenue Trend (2024)")
plt.xticks(rotation=45)
plt.ylabel("Revenue (INR)")
plt.show()


#Questions and Answers....

#1 What is the total sales revenue for the year?

total_revenue = df["total_revenue"].sum()
print("Total Sales Revenue:", total_revenue)

#2 Which month had the highest and lowest sales?
monthly_revenue = df.groupby("month")["total_revenue"].sum()

highest_month = monthly_revenue.idxmax()
lowest_month = monthly_revenue.idxmin()

print("Highest Sales Month:", highest_month, "=", monthly_revenue.max())
print("Lowest Sales Month:", lowest_month, "=", monthly_revenue.min())
#3 What is the average order value (AOV) across all transactions?
aov = df["avg_order_value"].mean()
print("Average Order Value (AOV):", aov)
#4 Which products generated the most revenue?
product_revenue = df.groupby("total_revenue")["total_revenue"].sum().sort_values(ascending=False)
print("Top 5 Products by Revenue:\n", product_revenue.head(5))
#5 Which categories are most profitable?
category_revenue = df.groupby("total_orders")["total_revenue"].sum().sort_values(ascending=False)
print("Most Profitable Categories:\n", category_revenue)
#6 Which region contributed the highest sales?
state_to_region = {
    "Delhi": "North", "Punjab": "North", "Haryana": "North", "Uttar Pradesh": "North",
    "Maharashtra": "West", "Gujarat": "West", "Rajasthan": "West",
    "Karnataka": "South", "Tamil Nadu": "South", "Kerala": "South", "Telangana": "South",
    "West Bengal": "East", "Odisha": "East", "Bihar": "East",
    "Madhya Pradesh": "Central"
}
df["region"] = df["state"].map(state_to_region)

