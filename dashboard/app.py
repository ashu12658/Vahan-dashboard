import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehicle Dashboard", layout="wide")

st.title("📊 Vehicle Class-wise & Manufacturer Growth Dashboard")

# ===============================
# 🚘 Vehicle Class-wise Section
# ===============================
df_vehicle = pd.read_csv("data/clean_data.csv")
df_vehicle.columns = df_vehicle.columns.str.strip()

st.sidebar.header("🚘 Vehicle Data Filters")
year_vehicle = st.sidebar.selectbox("Select Year for Vehicle Data", sorted(df_vehicle['Year'].unique()))
subcategory = st.sidebar.multiselect("Select Subcategory", df_vehicle['Subcategory'].unique(), default=df_vehicle['Subcategory'].unique())

filtered_vehicle = df_vehicle[(df_vehicle['Year'] == year_vehicle) & (df_vehicle['Subcategory'].isin(subcategory))]

st.subheader("📋 Filtered Vehicle Data")
st.dataframe(filtered_vehicle)

st.subheader("📊 Vehicle Count by Class")
fig_vehicle = px.bar(filtered_vehicle, x="Vehicle Class", y="Total Vehicles", color="Subcategory", barmode="group")
st.plotly_chart(fig_vehicle, use_container_width=True)

# ===============================
# 🏭 Manufacturer YoY Section
# ===============================
st.title("🏭 Manufacturer-wise YoY Growth")

df_manufacturer = pd.read_csv("data/manufacturer_data.csv")
df_manufacturer.columns = df_manufacturer.columns.str.strip()

df_manufacturer = df_manufacturer.sort_values(['Manufacturer', 'Category', 'Year'])
df_manufacturer['YoY Growth (%)'] = df_manufacturer.groupby(['Manufacturer', 'Category'])['Total Vehicles'].pct_change() * 100
df_manufacturer['YoY Growth (%)'] = df_manufacturer['YoY Growth (%)'].fillna(0).round(2)

st.sidebar.header("🏭 Manufacturer Filters")
year_manu = st.sidebar.selectbox("Select Year for Manufacturer Data", sorted(df_manufacturer['Year'].unique()), key='manu_year')
category = st.sidebar.selectbox("Select Vehicle Category", df_manufacturer['Category'].unique(), key='manu_category')

filtered_manu = df_manufacturer[(df_manufacturer['Year'] == year_manu) & (df_manufacturer['Category'] == category)]
required_cols = ['Manufacturer', 'Total Vehicles', 'YoY Growth (%)']
missing_cols = [col for col in required_cols if col not in filtered_manu.columns]

if missing_cols:
    st.error(f"Missing columns in manufacturer data: {missing_cols}")
    st.write("Available columns:", filtered_manu.columns.tolist())
else:
    st.subheader(f"📈 YoY Growth for {category} in {year_manu}")
    st.dataframe(filtered_manu[required_cols])
    fig_manu = px.bar(filtered_manu, x='Manufacturer', y='YoY Growth (%)', text='YoY Growth (%)', color='Manufacturer')
    st.plotly_chart(fig_manu, use_container_width=True)

# ===============================
# 📉 Manufacturer QoQ Section
# ===============================
st.title("📉 Manufacturer-wise QoQ Growth")

try:
    df_qoq = pd.read_csv("data/qoq_data.csv")
    df_qoq.columns = df_qoq.columns.str.strip()

    if 'Quarter' not in df_qoq.columns:
        st.error("❌ 'Quarter' column missing from qoq_data.csv. Re-run qoq_clean.py.")
        st.write("Available columns:", df_qoq.columns.tolist())
        st.stop()

    st.sidebar.header("📆 QoQ Filters")
    year_qoq = st.sidebar.selectbox("Select Year for QoQ", sorted(df_qoq['Year'].unique()), key='qoq_year')
    category_qoq = st.sidebar.selectbox("Select Category for QoQ", df_qoq['Category'].unique(), key='qoq_cat')
    quarter_qoq = st.sidebar.selectbox("Select Quarter", df_qoq['Quarter'].unique(), key='qoq_quarter')

    filtered_qoq = df_qoq[
        (df_qoq['Year'] == year_qoq) &
        (df_qoq['Category'] == category_qoq) &
        (df_qoq['Quarter'] == quarter_qoq)
    ]

    if not filtered_qoq.empty:
        st.subheader(f"📉 QoQ Growth for {category_qoq} in {quarter_qoq} {year_qoq}")
        st.dataframe(filtered_qoq[['Manufacturer', 'Total Vehicles', 'QoQ Growth (%)']])

        fig_qoq = px.bar(filtered_qoq, x="Manufacturer", y="QoQ Growth (%)", text="QoQ Growth (%)", color="Manufacturer")
        st.plotly_chart(fig_qoq, use_container_width=True)
    else:
        st.warning("No QoQ data available for selected filters.")

except FileNotFoundError:
    st.warning("📁 QoQ data file not found. Please generate `data/qoq_data.csv` using utils/qoq_clean.py")
