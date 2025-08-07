import pandas as pd

try:
    df = pd.read_csv("data/manufacturer_yoy.csv")
    print("✅ File loaded successfully")
    print(df.head())
    print("🧠 Columns are:", df.columns.tolist())
except Exception as e:
    print("❌ Error loading file:", e)
