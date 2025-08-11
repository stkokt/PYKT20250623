# Lese die Datei Erwerbstaetige.csv ein

# Bilde die Ratio:
# Anteil der Land-, Forst- und Fischereiarbeiter sowie der Dienstleister an den Gesamtbeschäftigten.

# Recherchiere, wie du diese Ratios in eine CSV- Datei zurückschreiben kannst. 

import csv
# Einlesen einer CSV-Datei mit csv.DictReader
with open('Erwerbstaetige.csv', mode='r', newline='') as file:
    csv_dict_reader = csv.DictReader(file, delimiter=";")
    dataErwerb = list(csv_dict_reader)

#print(dataErwerb)

jahre = [ds['Jahr'] for ds in dataErwerb]
# print(jahre)

ratioLFF = [round(float(ds['LandForstFisch'].replace(" ",""))/float(ds['Insgesamt'].replace(" ","")),5) for ds in dataErwerb]
#print(ratioLFF)

ratioDL = [round(float(ds['DienstAll'].replace(" ",""))/float(ds['Insgesamt'].replace(" ","")),5) for ds in dataErwerb]
#print(ratioDL)

ratios = list(zip(jahre, ratioLFF, ratioDL))
#print(ratios)

ratiosDict = list({"Jahr": ds[0],"ratioLFF": ds[1],"ratioDL": ds[2]} for ds in ratios)

print(ratiosDict)
# Schreiben über DictWriter

with open("output_Dict.csv", mode='w', newline='') as file:
        csv_dict_writer = csv.DictWriter(file, fieldnames=ratiosDict[0].keys(), delimiter=";")
        csv_dict_writer.writeheader()
        for row in ratiosDict:
            csv_dict_writer.writerow(row)



