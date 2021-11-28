# merging the data1.csv andd data2_sorted.csv
import csv

with open('data2_sorted.csv', newline="") as f:
  reader = csv.reader(f)
  data2 = list(reader)
  
with open('data1.csv', newline="") as f:
  reader = csv.reader(f)
  data1 = list(reader)

header1 = data1[0]
header2 = data2[0]
headers = header1+header2

planet_data1 = data1[1:]
planet_data2 = data2[1:]
#adding both planet datas
planet_data =[]
x = 0
y = 1

for i in planet_data1:
    sum= planet_data1[x]+planet_data2[y]
    planet_data.append(sum)
    x = x+1
    y = y+2

with open("merged_Data.csv", "w") as f: 
    csvwriter = csv.writer(f) 
    csvwriter.writerow(headers) 
    csvwriter.writerows(planet_data)