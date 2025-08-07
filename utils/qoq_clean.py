import pandas as pd

# ✅ Load the monthly data
df = pd.read_csv("data/monthly_data.csv")
df.columns = df.columns.str.strip()

# ✅ Map Month to Quarter
month_to_quarter = {
    'Jan': 'Q1', 'Feb': 'Q1', 'Mar': 'Q1',
    'Apr': 'Q2', 'May': 'Q2', 'Jun': 'Q2',
    'Jul': 'Q3', 'Aug': 'Q3', 'Sep': 'Q3',
    'Oct': 'Q4', 'Nov': 'Q4', 'Dec': 'Q4',
}

df['Quarter'] = df['Month'].map(month_to_quarter)

# ✅ DEBUG: Print to check
print("🔍 Sample DataFrame with Quarter:")
print(df.head(3))

# ✅ Group data quarterly
grouped = df.groupby(
    ['Year', 'Quarter', 'Category', 'Manufacturer']
)['Total Vehicles'].sum().reset_index()

# ✅ Sort data properly for QoQ calculation
grouped = grouped.sort_values(by=['Manufacturer', 'Category', 'Year', 'Quarter'])

# ✅ Calculate QoQ Growth
grouped['QoQ Growth (%)'] = grouped.groupby(['Manufacturer', 'Category'])['Total Vehicles'].pct_change() * 100
grouped['QoQ Growth (%)'] = grouped['QoQ Growth (%)'].fillna(0).round(2)

# ✅ Final clean-up
grouped.columns = grouped.columns.str.strip()

# ✅ DEBUG: Print final columns
print("✅ Final Columns in grouped:")
print(grouped.columns.tolist())

# ✅ Save final output
grouped.to_csv("data/qoq_data.csv", index=False)
print("✅ qoq_data.csv CREATED with Quarter column")
