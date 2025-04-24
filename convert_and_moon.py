import csv

file_name = input('Please enter a file name (include .dat): ')
file_name_csv = file_name.replace('.dat', '.csv')

header = ['YYYY-MM-DDTHH:mm:ss.fff', 'YYYY-MM-DDTHH:mm:ss.fff', 'Celsius', 'number', 'Hz', 'mag/arcsec^2']

with open(file_name, 'r') as dat_file, open(file_name_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i, line in enumerate(dat_file):
        if i < 35:
            continue
        if i == 35:
            csv_writer.writerow(header)
        row = line.strip().split(';')  # Adjust delimiter if needed
        csv_writer.writerow(row)

with open(file_name_csv, newline='') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)
    date = rows[1][0]
    date = date[:date.find('T')]

with open('moon_phases_UTC_1800-2050.csv', newline='') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)
    for row in rows:
        if row[0] == date:
            row_needed = row[1:4]

new_header = ['YYYY-MM-DDTHH:mm:ss.fff', 'YYYY-MM-DDTHH:mm:ss.fff', 'Celsius', 'number', 'Hz', 'mag/arcsec^2', 'Area', 'Category', 'Phase']

with open(file_name_csv, 'r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)
    
new_headers = [new_header]

for i, row in enumerate(rows[1:]):
    updated_row = row + row_needed
    new_headers.append(updated_row)

# Write back to the file (or a new file)
with open(file_name_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(new_headers)
