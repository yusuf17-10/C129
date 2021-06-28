import csv

data_set_1 = []
data_set_2 = []

with open("final.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data_set_1.append(row)

with open("data_set2_sorted.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data_set_2.append(row)

header_1 = data_set_1[0]
planet_data_1 = data_set_1[1:]

header_2 = data_set_2[0]
planet_data_2 = data_set_2[1:]

headers = header_1+header_2

planet_data =[]

for index,delete_row in enumerate(planet_data_1):
    planet_data.append(planet_data_1[index]+planet_data_2[index])

with open("data_set2_sorted.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)
