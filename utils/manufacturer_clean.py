import pandas as pd

df = pd.read_csv("data/manufacturer_data.csv")

# Clean up commas if needed
df['Total Vehicles'] = df['Total Vehicles'].astype(str).str.replace(',', '').astype(int)

# Sort and calculate YoY Growth %
df = df.sort_values(by=['Manufacturer', 'Category', 'Year'])
df['YoY Growth (%)'] = df.groupby(['Manufacturer', 'Category'])['Total Vehicles'].pct_change() * 100

# Save to final file
df.to_csv("data/manufacturer_yoy.csv", index=False)
print("✅ YoY growth for manufacturer calculated.")
