import csv

with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  planets_data = list(reader)

headers  = planets_data[0]
planets_data.pop(0)

for i in planets_data:
    i[2] =i[2].lower()

#to convert the third column of planets_data in the alphabetical order
planets_data.sort(key=lambda planets_data: planets_data[2])

with open("data1_sorted.csv", "w") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planets_data)
