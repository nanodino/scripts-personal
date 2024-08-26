import os
import pandas as pd

current_directory = os.getcwd()

xlsx_files = [f for f in os.listdir(current_directory) if f.endswith('.xlsx')]

for xlsx_file in xlsx_files:
    excel_file = pd.ExcelFile(xlsx_file, engine='openpyxl')
    
    for sheet_name in excel_file.sheet_names:
        df = pd.read_excel(xlsx_file, sheet_name=sheet_name, engine='openpyxl')
        csv_file_name = f"{os.path.splitext(xlsx_file)[0]}_{sheet_name}.csv"
        df.to_csv(csv_file_name, index=False)

print("Conversion complete.")

