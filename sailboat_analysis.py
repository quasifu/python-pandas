import pandas as pd

# Load the Excel file
file_path = "SimplySails.xlsx"
sheet_name = "Sailboat Activities"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter rows with Maintenance entries
maintenance_df = df[df['Entry Type'] == 'Maintenance']

# Group by Serial Number and calculate total maintenance hours
maintenance_hours = maintenance_df.groupby('Serial Number')['Hours'].sum()

# Find the boat with the most maintenance hours
most_maintenance_boat = maintenance_hours.idxmax()
max_maintenance_hours = maintenance_hours.max()

# Print the result
print(f"The boat with the most maintenance is {most_maintenance_boat} with {max_maintenance_hours} hours of maintenance.")
