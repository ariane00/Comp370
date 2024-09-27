import csv
import argparse
from datetime import datetime

parser = argparse.ArgumentParser(description='Script to output nyc borough complaints.')
parser.add_argument('-i', '--input', required=True, help='Input CSV file')
parser.add_argument('start_date', type=str, help='The start date of the search (YYYY-MM-DD)')
parser.add_argument('end_date', type=str, help='The end date of the search (YYYY-MM-DD)')
parser.add_argument('-o', '--output', type=str, help='Output file to save the results (optional)')

args = parser.parse_args()

start_date = args.start_date
start_date = datetime.strptime(start_date, '%Y-%m-%d')
end_date = args.end_date
end_date = datetime.strptime(end_date, '%Y-%m-%d')
borough = args.borough
input_file = args.input

complaints = {}

with open(input_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        complaint_date = datetime.strptime(row['Created Date'], '%Y-%m-%d')
        if start_date <= complaint_date <= end_date:
            borough = row['Borough']
            complaint_type = row['Complaint Type']

            key = (complaint_type, borough)
            if key not in complaint_counts:
                complaint_counts[key] = 0

            complaint_counts[key] += 1

results = ["complaint type,borough,count"]
for (complaint_type, borough), count in complaint_counts.items():
    results.append(f"{complaint_type},{borough},{count}")
if output_file:
    with open(output_file, 'w') as file:
        file.write("\n".join(results))
else:
    print("\n".join(results))
