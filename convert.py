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