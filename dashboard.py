import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATA
# ==========================================

df = pd.read_csv(
    "Superstore sample_Cleaned.csv",
    encoding="cp1252"
)

df["Order Date"] = pd.to_datetime(
    df["Order Date"],
    dayfirst=True
)


# ==========================================
# DASHBOARD TITLE
# ==========================================

st.title("Sales & Profit Dashboard")
st.write("Superstore Sales Analysis")


# ==========================================
# FILTERS
# ==========================================

st.sidebar.header("Filters")

region = st.sidebar.multiselect(
    "Select Region",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

category = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category))
]


# ==========================================
# KEY METRICS
# ==========================================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
average_discount = filtered_df["Discount"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Sales", f"${total_sales:,.2f}")
col2.metric("Total Profit", f"${total_profit:,.2f}")
col3.metric("Average Discount", f"{average_discount:.2%}")


# ==========================================
# SALES BY REGION
# ==========================================

st.subheader("Sales by Region")

sales_region = filtered_df.groupby("Region")["Sales"].sum()

fig, ax = plt.subplots()
sales_region.plot(kind="bar", ax=ax)

ax.set_xlabel("Region")
ax.set_ylabel("Total Sales")
ax.set_title("Sales by Region")

st.pyplot(fig)


# ==========================================
# PROFIT BY REGION
# ==========================================

st.subheader("Profit by Region")

profit_region = filtered_df.groupby("Region")["Profit"].sum()

fig, ax = plt.subplots()
profit_region.plot(kind="bar", ax=ax)

ax.set_xlabel("Region")
ax.set_ylabel("Total Profit")
ax.set_title("Profit by Region")

st.pyplot(fig)


# ==========================================
# SALES BY CATEGORY
# ==========================================

st.subheader("Sales by Category")

sales_category = filtered_df.groupby("Category")["Sales"].sum()

fig, ax = plt.subplots()
sales_category.plot(kind="bar", ax=ax)

ax.set_xlabel("Category")
ax.set_ylabel("Total Sales")
ax.set_title("Sales by Category")

st.pyplot(fig)


# ==========================================
# MONTHLY SALES TREND
# ==========================================

st.subheader("Monthly Sales Trend")

monthly_sales = filtered_df.groupby(
    filtered_df["Order Date"].dt.to_period("M")
)["Sales"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

fig, ax = plt.subplots(figsize=(10, 5))
monthly_sales.plot(kind="line", ax=ax)

ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")
ax.set_title("Monthly Sales Trend")

plt.xticks(rotation=45)

st.pyplot(fig)


# ==========================================
# TOP 10 PRODUCTS BY SALES
# ==========================================

st.subheader("Top 10 Products by Sales")

top_products = filtered_df.groupby(
    "Product Name"
)["Sales"].sum().sort_values(ascending=False).head(10)

fig, ax = plt.subplots(figsize=(10, 6))
top_products.sort_values().plot(kind="barh", ax=ax)

ax.set_xlabel("Total Sales")
ax.set_ylabel("Product Name")
ax.set_title("Top 10 Products by Sales")

st.pyplot(fig)


# ==========================================
# SALES VS PROFIT
# ==========================================

st.subheader("Sales vs Profit")

fig, ax = plt.subplots()

ax.scatter(
    filtered_df["Sales"],
    filtered_df["Profit"]
)

ax.set_xlabel("Sales")
ax.set_ylabel("Profit")
ax.set_title("Sales vs Profit")

st.pyplot(fig)