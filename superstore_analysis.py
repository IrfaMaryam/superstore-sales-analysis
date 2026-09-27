import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Superstore sample_Cleaned.csv", encoding="cp1252")

# ==========================================
# 1. SALES BY REGION
# ==========================================

sales_region = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_region.plot(kind="bar")

plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 2. PROFIT BY REGION
# ==========================================

profit_region = df.groupby("Region")["Profit"].sum()

plt.figure(figsize=(8, 5))
profit_region.plot(kind="bar")

plt.title("Profit by Region")
plt.xlabel("Region")
plt.ylabel("Total Profit")

plt.tight_layout()
plt.show()


# ==========================================
# 3. SALES BY CATEGORY
# ==========================================

sales_category = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
sales_category.plot(kind="bar")

plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")

plt.tight_layout()
plt.show()


# ==========================================
# 4. MONTHLY SALES TREND
# ==========================================

df["Order Date"] = pd.to_datetime(df["Order Date"], dayfirst=True)

monthly_sales = df.groupby(
    df["Order Date"].dt.to_period("M")
)["Sales"].sum()

plt.figure(figsize=(10, 5))
monthly_sales.plot(kind="line")

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ==========================================
# 5. TOP 10 PRODUCTS BY SALES
# ==========================================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(10, 6))
top_products.sort_values().plot(kind="barh")

plt.title("Top 10 Products by Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")

plt.tight_layout()
plt.show()


# ==========================================
# 6. SALES VS PROFIT
# ==========================================

plt.figure(figsize=(8, 5))
plt.scatter(df["Sales"], df["Profit"])

plt.title("Sales vs Profit")
plt.xlabel("Sales")
plt.ylabel("Profit")

plt.tight_layout()
plt.show()