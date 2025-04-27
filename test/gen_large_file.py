import csv

input_file = 'your_input.csv'
output_file = 'large_py.csv'
target_size_mb = 200
line_count = 0

data = []
try:
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        for row in reader:
            data.append(row)
            line_count += 1
except FileNotFoundError:
    print(f"Error:file '{input_file}' not found!")
    exit()

if not data:
    print("Error:input file is empty!")
    exit()

bytes_written = 0
with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)
    while bytes_written < target_size_mb * 1024 * 1024:
        writer.writerows(data)
        bytes_written = outfile.tell()

print(f"'{output_file}' {bytes_written / (1024 * 1024):.2f} MB is generated!")
