#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sales_data.csv")

st.title("Retail Sales Dashboard")

st.subheader("Total Sales")
st.write(df["Sales_Amount"].sum())

st.subheader("Sales by Region")
region_sales = df.groupby("Region")["Sales_Amount"].sum()

fig, ax = plt.subplots()
sns.barplot(x=region_sales.index, y=region_sales.values, ax=ax)
st.pyplot(fig)

st.subheader("Sales by Product Category")
cat_sales = df.groupby("Product_Category")["Sales_Amount"].sum()

fig2, ax2 = plt.subplots()
sns.barplot(x=cat_sales.index, y=cat_sales.values, ax=ax2)
st.pyplot(fig2)

st.subheader("Monthly Sales Trend")
monthly = df.groupby("month")["Sales_Amount"].sum()

fig3, ax3 = plt.subplots()
ax3.plot(monthly.index, monthly.values)
st.pyplot(fig3)

