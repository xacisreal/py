import pandas as pd
source_file_path = r'C:\Users\MLM\Downloads\Mail List.xlsx'
destination_file_path = r'C:\Users\MLM\Downloads\Certificate List.xlsx'  
try:
    df_mail_list = pd.read_excel(source_file_path, sheet_name='Sheet1') 
except Exception as e:
    print("Error reading the specified sheet from the source file:", e)
    exit()
try:
    df_cert_list = pd.read_excel(destination_file_path, sheet_name='Certificate List')
except FileNotFoundError:
     df_cert_list = pd.DataFrame()
df_combined = pd.concat([df_cert_list, df_mail_list], axis=1)  # Horizontally combine
with pd.ExcelWriter(destination_file_path, engine='openpyxl', mode='w') as writer:
    df_combined.to_excel(writer, sheet_name='Certificate List', index=False)
print("Data combined from 'Mail List' to 'Certificate List' in", destination_file_path)
