import csv
import sys

file_name = sys.argv[1] # Gets the file from command line 'python3 convert_and_moon [filename]'
file_name_csv = file_name.replace('.dat', '.csv')

header = ['UTC_Date_And_Time', 'Local_Date_And_Time', 'Temperature', 'Counts', 'Frequency', 'MSAS']

date_list = []

# Creates a new CSV file, removes the length header, adds the new header, and copies the .dat file information over
with open(file_name, 'r') as macleish_dat_file, open(file_name_csv, 'w', newline='') as macleish_csv_file:
    macleish_file_writer = csv.writer(macleish_csv_file)
    macleish_file_reader = csv.reader(macleish_dat_file, delimiter=';')
    macleish_file_writer.writerow(header)
    for macleish_row in list(macleish_file_reader)[35:]:
        macleish_file_writer.writerow(macleish_row)

moon_data_needed = []

# Gets the moon phase data based on the CSV's date
with open('moon_phases.csv', newline='') as moon_file, open(file_name_csv, 'r', newline='') as macleish_file:
    moon_file_reader = csv.reader(moon_file)
    moon_rows = list(moon_file_reader)
    macleish_file_reader = csv.reader(macleish_file)
    macleish_rows = list(macleish_file_reader)
    for moon_row in moon_rows: # This nested loop needs to be made more efficient - SQL would be best but we can't use embedded SQL
        for macleish_row in macleish_rows:
            if moon_row[0] == macleish_row[0].split('T')[0]: # Matches the dates in both CSVs since the Macleish data has a different format
                moon_data_needed.append(moon_row[1:4])

new_header = ['UTC_Date_And_Time', 'Local_Date_And_Time', 'Temperature', 'Counts', 'Frequency', 'MSAS', 'Area', 'Category', 'Phase']
new_data = [new_header]

# Adds the moon phase data to the CSV with the light data
with open(file_name_csv, 'r', newline='') as macleish_file:
    macleish_file_reader = csv.reader(macleish_file)
    rows = list(macleish_file_reader)
    for i in range(1, len(rows)):
        new_row = rows[i] + moon_data_needed[i-1]
        new_data.append(new_row)

with open(file_name_csv, 'w', newline='') as macleish_file:
    macleish_file_writer = csv.writer(macleish_file)
    macleish_file_writer.writerows(new_data)
