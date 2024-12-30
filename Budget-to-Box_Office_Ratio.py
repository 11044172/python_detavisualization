import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file
data_path = '/Users/eusyoicloud.com/Desktop/プログラミング特訓/データ分析/movie.xlsx'  # Specify the file path
sheet_name = "工作表1"  # Specify the sheet name or number if necessary
df = pd.read_excel(data_path, sheet_name=sheet_name)

# Extract the required columns and rename them for clarity
data = df[["English titles", "總票數 Total number of votes", "預算 Budget"]]
data.columns = ["Title", "Tickets_Sold", "Budget"]

# Clean the Budget column
# Remove "million" and convert to numeric
data["Budget"] = data["Budget"].str.replace("million", "").str.strip()
data["Budget"] = pd.to_numeric(data["Budget"], errors='coerce') * 1e6  # Convert to numeric and scale to TWD

# Clean the Tickets_Sold column
data["Tickets_Sold"] = pd.to_numeric(data["Tickets_Sold"], errors='coerce')

# Drop rows with missing or invalid data
data = data.dropna(subset=["Budget", "Tickets_Sold"])

# Calculate revenue (assuming average ticket price is 200 TWD)
TICKET_PRICE = 200
data["Revenue"] = data["Tickets_Sold"] * TICKET_PRICE

# Calculate correlation coefficient
correlation = data["Budget"].corr(data["Revenue"])
print(f"Correlation coefficient between budget and revenue: {correlation:.2f}")

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(data["Budget"], data["Revenue"], alpha=0.7, edgecolors='k')
plt.title("Correlation between Budget and Revenue", fontsize=16)
plt.xlabel("Budget (TWD)", fontsize=14)
plt.ylabel("Revenue (TWD)", fontsize=14)
plt.grid(True)

# Show the plot
plt.tight_layout()
plt.show()
