import csv

data = []

with open("data_set.csv","r")as f:
    csvReader = csv.reader(f)

    for i in csvReader:
        data.append(i)
    
headers = data[0]
planet_data = data[1:]

for data_point in planet_data:
    data_point[2] = data_point[2].lower()
planet_data.sort(key=lambda planet_data:planet_data[2])

with open("data_set2_sorted.csv","a+")as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)
    csvWriter.writerows(planet_data)


