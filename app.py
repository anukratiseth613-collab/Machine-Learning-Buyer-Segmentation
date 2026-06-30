import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Buyer Segmentation Dashboard")
df = pd.read_csv("buyer_segmentation_results.csv")

st.subheader("Dataset Preview")
st.dataframe(df.head())

st.subheader("Cluster Distribution")
st.bar_chart(df["Cluster"].value_counts())

st.subheader("Average Satisfaction Score by Cluster")
st.bar_chart(df.groupby("Cluster")["satisfaction_score"].mean())

st.subheader("Loan Applied by Cluster")
st.bar_chart(df.groupby("Cluster")["loan_applied"].sum())

country_cols = [col for col in df.columns if col.startswith("country_")]

st.subheader("Country Distribution")
st.bar_chart(df[country_cols].sum())
st.success("Dashboard Created Successfully!")
