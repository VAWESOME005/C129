import csv

dataset1 = []
dataset2 = []

with open("final.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset1.append(row)

with open("dataset_sorted.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset2.append(row)

headers_1 = dataset1[0]
headers_2 = dataset2[0]

planet_data_1 = dataset1[1:]
planet_data_2 = dataset2[1:]

headers = headers_1 + headers_2

planet_data = []

for index, data_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index] + planet_data_2[index])

with open("final_merged.csv", 'a+') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)
