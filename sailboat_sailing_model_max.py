import pandas as pd

# Load the Excel file
file_path = "SimplySails.xlsx"
sheet_name = "Sailboat Activities"
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Filter rows with Maintenance entries
sailing_df = df[df['Entry Type'] == 'Sailing']

# Group by Serial Number and calculate total maintenance hours
sailing_hours = sailing_df.groupby('Boat Model')['Hours'].sum()

# Find the boat with the most maintenance hours
most_sailing_model = sailing_hours.idxmax()
max_sailing_hours = sailing_hours.max()

# Print the result
print(f"The boat model with the most sailing is {most_sailing_model} with {max_sailing_hours} hours of sailing.")
