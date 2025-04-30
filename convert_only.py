import csv

file_name = input('Please enter a file name (include .dat): ')
file_name_csv = file_name.replace('.dat', '.csv')

header = ['UTC Date & Time', 'Local Date & Time', 'Temperature', 'Counts', 'Frequency', 'MSAS']

with open(file_name, 'r') as dat_file, open(file_name_csv, 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    for i, line in enumerate(dat_file):
        if i < 35:
            continue
        if i == 35:
            csv_writer.writerow(header)
        row = line.strip().split(';')
        csv_writer.writerow(row)