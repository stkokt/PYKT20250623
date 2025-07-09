# 1. List- Comprehensions
# 2. Modul- Importe

# LIST COMPREHENSION (LC)

# Eine Liste der Zahlen von 1 bis 100
# als for- Loop
liste_1_100 = []
for zahl in range(1,101):
    liste_1_100.append(zahl)

# als LC
liste_1_100 = [zahl for zahl in range(1,101)]

print("Zahlen von 1 bis 100:",liste_1_100,"\n")

# Eine Liste des Doppelten aller Zahlen von 1 bis 100
liste_mal2_1_100 = [zahl*2 for zahl in range(1,101)]

print("Zahlen verdoppelt:",liste_mal2_1_100,"\n")

# Eine Liste von Tupelen, jeweils die Zahl und die Zahl+5
liste_tupel = [(zahl, zahl+5) for zahl in range(1,101)]

print("Tupele:",liste_tupel,"\n")

# Eine Liste der geraden Zahlen von 1 bis 100
liste_gerade_1_100 = []

# als for- Loop
for zahl in range(1,101):
    if zahl % 2 == 0:
        liste_gerade_1_100.append(zahl)

# als LC
liste_gerade_1_100 = [zahl for zahl in range(1,101) if zahl % 2 == 0]

print("Gerade Zahlen:",liste_gerade_1_100,"\n")

# Eine Liste der bedingter Ausgaben
# als for- Loop
liste_gerade_ungerade = []

for zahl in range(1,101):
    if zahl % 2 == 0:
        liste_gerade_ungerade.append("gerade")
    else:
        liste_gerade_ungerade.append("ungerade")

# als LC:
liste_gerade_ungerade = ["gerade" if zahl % 2 ==0 else "ungerade" for zahl in range(1,101)]

print("Auswertung Gerade/ Ungerade:",liste_gerade_ungerade,"\n")

# Erweiterung der Bedingung mit elseif
listeZahlenbereich = [0,1,-1,5,-4,0]

# Auswertung per for- Loop
listeÜberUnterNull = []

for zahl in listeZahlenbereich:
    if zahl > 0:
        listeÜberUnterNull.append("positiv")
    elif zahl < 0:
        listeÜberUnterNull.append("negativ")
    else:
        listeÜberUnterNull.append("null")

# print(listeÜberUnterNull)

# Auswertung per LC
listeZahlenbereich = [0,1,-1,5,-4,0]
listeÜberUnterNull = ["positiv" for zahl in listeZahlenbereich if zahl>0 ]
listeÜberUnterNull = ["positiv" if zahl>0 
                      else "negativ" if zahl < 0 # im Prinzip ein elif
                      else "null" 
                      for zahl in listeZahlenbereich]
print("Auswertung Über/Unter/Gleich 0",listeÜberUnterNull,"\n")

# MODUL- IMPORTE

# import random     # import des gesamten Moduls
# print(randint(0, 20))

from random import randint, sample  # Import einzelner Modul- Funktionen

print(randint(0, 20))

# help("modules") # listet alle installierten Module auf
# help("time")    # gibt die Dokumantation des Moduls 'time' aus