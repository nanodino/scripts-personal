import os
import pandas as pd

# Get the current directory
current_directory = os.getcwd()

# List all .xlsx files in the current directory
xlsx_files = [f for f in os.listdir(current_directory) if f.endswith('.xlsx')]

# Process each .xlsx file
for xlsx_file in xlsx_files:
    # Load the Excel file
    excel_file = pd.ExcelFile(xlsx_file)
    
    # Process each sheet in the Excel file
    for sheet_name in excel_file.sheet_names:
        # Read the sheet into a DataFrame
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name)
        
        # Create a CSV file name based on the Excel file and sheet name
        csv_file_name = f"{os.path.splitext(xlsx_file)[0]}_{sheet_name}.csv"
        
        # Save the DataFrame to a CSV file
        df.to_csv(csv_file_name, index=False)

print("Conversion complete.")
