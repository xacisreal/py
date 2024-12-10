import csv
def read_csv_rows(filename):
    rows = []
    with open(filename, 'r') as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            rows.append(",".join(row))  
    return rows
# Example usage
csv_filename = "blah.csv"
rows_list = read_csv_rows(csv_filename)
print(rows_list)
