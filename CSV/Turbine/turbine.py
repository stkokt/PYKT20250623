import csv

csv_file = open('10m.csv', 'r')
csv_reader = csv.reader(csv_file, delimiter=";")
turbinedata = []
# next(csv_reader)
for line in csv_reader:
    turbinedata.append(line)
csv_file.close()

headers = turbinedata.pop(0)
turbine1 = [[float(elem) for elem in line] for line in turbinedata]
#print(turbine1)

with open('turbinedata.csv', "x", newline="") as newCSV:
    csv_schreiber = csv.writer(newCSV)
    csv_schreiber.writerow(headers)
    csv_schreiber.writerows(turbine1)

import csv
csv_dict_list = []
with open("10m.csv", "r") as csv_datei:
    csv_dict_leser = csv.DictReader(csv_datei, delimiter=";")
    for zeile in csv_dict_leser:
        csv_dict_list.append(zeile)

#print(csv_dict_list)

with open("turbinedata_dict.csv", "x", newline="") as csv_dict:
    #headerList = ["Wind Speed"...]
    csv_dict_schreiber = csv.DictWriter(csv_dict, fieldnames=csv_dict_list[0].keys(), delimiter = ";")
    csv_dict_schreiber.writeheader()
    csv_dict_schreiber.writerows(csv_dict_list)

 