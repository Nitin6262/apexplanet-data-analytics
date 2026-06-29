import pandas as pd
import os

# Load cleaned dataset
file_path = os.path.join("data", "cleaned_superstore.csv")

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print(df.head())

# -----------------------------
# Data Cleaning
# -----------------------------

# Remove duplicate rows
df = df.drop_duplicates()

# Remove rows with missing values
df = df.dropna()

print("\nData cleaned successfully!")
print(f"Rows after cleaning: {df.shape[0]}")

# -----------------------------
# Save Processed Data
# -----------------------------

output_path = os.path.join("data", "processed_superstore.csv")

df.to_csv(output_path, index=False)

print("\nProcessed dataset saved successfully!")
print(f"Saved to: {output_path}")

# -----------------------------
# Calculate KPIs
# -----------------------------

total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["Order ID"].nunique()
average_sales = df["Sales"].mean()
average_profit = df["Profit"].mean()

print("\n===== Key Performance Indicators =====")
print(f"Total Sales   : {total_sales:.2f}")
print(f"Total Profit  : {total_profit:.2f}")
print(f"Total Orders  : {total_orders}")
print(f"Average Sales : {average_sales:.2f}")
print(f"Average Profit: {average_profit:.2f}")

# -----------------------------
# Export Results to Excel
# -----------------------------

excel_path = os.path.join("data", "analytics_report.xlsx")

# Create KPI DataFrame
kpi_df = pd.DataFrame({
    "KPI": [
        "Total Sales",
        "Total Profit",
        "Total Orders",
        "Average Sales",
        "Average Profit"
    ],
    "Value": [
        total_sales,
        total_profit,
        total_orders,
        average_sales,
        average_profit
    ]
})

# Export to Excel
with pd.ExcelWriter(excel_path, engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="Processed Data", index=False)
    kpi_df.to_excel(writer, sheet_name="KPI Summary", index=False)

print("\nExcel report exported successfully!")
print(f"Saved to: {excel_path}")