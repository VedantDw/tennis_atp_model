import pandas as pd
import os

# List all files in the current directory
files = [f for f in os.listdir() if f.startswith("atp_matches") and f.endswith(".csv")]

# Load and explore one of the CSV files
for file in files:
    print(f"Exploring file: {file}")
    data = pd.read_csv(file)
    print(data.head())  # Display the first 5 rows
    print(data.info())  # Display column information
    print("\n")
    