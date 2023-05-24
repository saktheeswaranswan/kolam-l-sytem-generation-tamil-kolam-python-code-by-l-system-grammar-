import pandas as pd

# Path to the input CSV file
input_csv_file = 'output_coordinates.csv'

# Path to the output CSV file
output_csv_file = 'output.csv'

# Number to divide the X and Y coordinates by
divisor = 22

# Read the input CSV file
data = pd.read_csv(input_csv_file)

# Divide the X and Y coordinates by the divisor, round to integers, and convert to int data type
data['x'] = (data['x'] / divisor).round().astype(int)
data['y'] = (data['y'] / divisor).round().astype(int)

# Save the updated data to the output CSV file
data.to_csv(output_csv_file, index=False)

