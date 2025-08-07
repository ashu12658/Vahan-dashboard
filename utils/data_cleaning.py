import pandas as pd

def load_raw_data(path="data/raw_data.csv"):
    df = pd.read_csv(path)
    return df

def clean_data(df):
    for col in ['4WIC', 'LMV', 'MMV', 'HMV', 'Total']:
        df[col] = df[col].astype(str).str.replace(',', '').astype(int)
    df['Year'] = 2025
    long_df = df.melt(
        id_vars=['Year', 'Vehicle Class'],
        value_vars=['4WIC', 'LMV', 'MMV', 'HMV'],
        var_name='Subcategory',
        value_name='Total Vehicles'
    )
    return long_df

# 👇👇 This part is needed to actually RUN it
if __name__ == "__main__":
    df = load_raw_data("data/raw_data.csv")
    cleaned = clean_data(df)
    cleaned.to_csv("data/clean_data.csv", index=False)
    print("✅ Cleaned data saved to data/clean_data.csv")
