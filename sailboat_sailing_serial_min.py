import pandas as pd

# Load the Excel file
file_path = "SimplySails.xlsx"
sheet_name = "Sailboat Activities"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter rows with Maintenance entries
sailing_df = df[df['Entry Type'] == 'Sailing']

# Group by Serial Number and calculate total maintenance hours
sailing_hours = sailing_df.groupby('Serial Number')['Hours'].sum()

# Find the boat with the most maintenance hours
least_sailing_boat = sailing_hours.idxmin()
least_sailing_hours = sailing_hours.min()

# Print the result
print(f"The boat with the least sailing is {least_sailing_boat} with {least_sailing_hours} hours of sailing.")
