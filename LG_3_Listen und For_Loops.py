# Listen- Methoden:
"""
 1  append(self, object, /)
 |      Hängt ein Objekt an das Ende der Liste.
 |
 2  clear(self, /)
 |      Entfernt alle Elemente aus der Liste.
 |
 3  copy(self, /)
 |      Gibt eine flache Kopie der Liste zurück.
 |
 4  count(self, value, /)
 |      Gibt die Anzahl des Auftretens eines Wertes zurück.
 |
 5  extend(self, iterable, /)
 |      Erweitert die Liste durch Anhängen der Elemente eines iterierbaren Objekts.
 |
 6  index(self, value, start=0, stop=9223372036854775807, /)
 |      Gibt den ersten Index eines Wertes zurück.
 |
 |      Wirft einen ValueError, wenn der Wert nicht vorhanden ist.
 |
 7  insert(self, index, object, /)
 |      Fügt ein Objekt vor einem Index ein.
 |
 8  pop(self, index=-1, /)
 |      Entfernt einen Wert an einem Index und gibt diesen zurück (default: letzter Wert).
 |
 |      Wirft IndexError, wenn die Liste leer ist oder der Index außerhalb der Liste liegt.
 |
 9  remove(self, value, /)
 |      Entfernt das erste Auftreten eines Wertes.
 |
 |      Wirft ValueError, wenn dieser Wert nicht vorhanden ist.
 |
 10 reverse(self, /)
 |      Kehrt die Liste um. *IN PLACE*
 |
 11 sort(self, /, *, key=None, reverse=False)
 |      Sortiert die Liste in aufsteigender Reihenfolge. *IN PLACE*
 |
 |      Ist eine key- Funktion gegeben, wird diese auf die Listenelemente angewandt.
 |
 |      Das Reverse- Flag kann gesetzt werden, um absteigend zu sortieren.

"""

listeA = [15, 7, 39, 13, 41, 21, 20, 4, 13, 
          16, 40, 28, 45, 12, 19, 10, 28, 36, 
          48, 14, 30, 3, 37, 26, 21, 1, 33, 33, 10, 11]

# Aufgabe 1: 
# Durchlaufe die Liste A mit einem For- Loop und gebe sie damit aus.

print("\nAufgabe 1\n")
for zahl in listeA:
    print(zahl, end = ",")
print()

# Aufgabe 2: 
# Gebe nur das erste und das letzte Element der Liste A aus.

print("\nAufgabe 2\n")
print(f"Erstes Element: {listeA[0]}, letztes Element: {listeA[-1]}")

# Aufgabe 3: 
# Gebe nur die geradzahligen Elemente der Liste A aus.

print("\nAufgabe 3\n")
for zahl in listeA:
    if zahl % 2 == 0:
        print(zahl, end = ",")
print()

# Aufgabe 4: 
# Ermittle und gebe aus, wieviele Elemente die Liste A enthält.

print("\nAufgabe 4\n")
print("Anzahl der Elemente in listeA:",len(listeA))

# Aufgabe 5: 
# Zähle die geraden und die ungeraden Zahlen und gebe die jeweilige Anzahl aus.
# Erhöhter Schwierigkeitsgrad: Nutze dafür nur eine(!) Zählvariable.

print("\nAufgabe 5\n")

liste_cnt = [0,0]

for num in listeA:
    if num % 2 == 0:
        liste_cnt[0]+=1
    else:
        liste_cnt[1]+=1
print(f"Anzahl der geraden Zahlen: {liste_cnt[0]}")
print(f"Anzahl der ungeraden Zahlen: {liste_cnt[1]}")

# Will man nur wissen, ob es mehr gerade oder ungerade Zahlen gibt:

liste_cnt2 = 0

for num in listeA:
    if num % 2 == 0:
        liste_cnt2 += 1
    else:
        liste_cnt2 -= 1

print(liste_cnt2) 
# 0:     gleiche Anzahl von geraden und ungeraden Zahlen
# > 0:   mehr gerade Zahlen
# < 0:   mehr ungerade Zahlen


# Aufgabe 6: 
# Gebe das größte und das kleinste Element der Liste A aus, 
# sowie die Summe und den Durchschnitt aller Listenelemente.

print("\nAufgabe 6\n")

print(f"Größtes Element der Liste: {max(listeA)}")
print(f"Kleinstes Element der Liste: {min(listeA)}")
print(f"Summe aller Elemente der Liste: {sum(listeA)}")
print(f"Durchschnitt aller Element der Liste: {round(sum(listeA)/len(listeA), 2)}")

# Andere Variante:

print("\nAlternative mit Variablen\n")

maxVal = 0
minVal = listeA[0]
sumVal = 0
lenList = 0

for num in listeA:
    if num > maxVal:
        maxVal = num
    if num < minVal:
        minVal = num
    sumVal += num
    lenList += 1

print(f"Größtes Element der Liste: {maxVal}")
print(f"Kleinstes Element der Liste: {minVal}")
print(f"Summe aller Elemente der Liste: {sumVal}")
print(f"Durchschnitt aller Element der Liste: {round(sumVal/lenList, 2)}")

# Aufgabe 7: 
# Schreibe die liste_of_5 so, dass statt einer durch 5 teilbaren 
# Zahl aus liste_0_100 eine Liste eingefügt wird, die alle bis dorthin
#  durch 5 teilbaren Zahlen enthält. Also: [[0],1,2,3,4,[0,5],6,7,8,9,[0,5,10]...

liste_0_100 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
liste_of_5 = []

print("\nAufgabe 7\n")

tmp_list = []
for num in liste_0_100:
    if num % 5 == 0:
        tmp_list.append(num)
        liste_of_5.append(tmp_list.copy())
    else:
        liste_of_5.append(num)

print(liste_of_5)

# Aufgabe 8: Personen innerhalb einer Liste suchen
"""
Vorgegeben:

Liste mit Namen

Hinweis:
for-Schleife
if-Bedingung
String-Methode: startwith(...)
Variablen

Aufgabenteil a:
Eingabe: Exakter Name
Ausgabe: Alle Einträge die passen
Aufgabenteil b:
Eingabe: Anfang eines Namens
Ausgabe: Alle Einträge die passen
Aufgabenteil c:
Eingabe: Anfang eines Namens
Ausgabe: Maximal die ersten drei passenden Einträge
Aufgabenteil d:
Eingabe: Ein Nachname
Ausgabe: Index des Listenelements
-----------------------------
"""
namen = ["Levi Schneider","Lina Schmitt","Emil Weber","Liam Fischer","Lia Krause",
         "Emilia Hartmann","Anton Meyer","Theo Wagner","Emma Koch","Paul Becker",
         "Leano Schulz","Elias Richter","Jakob Hofmann","Ella Herrmann",
         "Ida Schröder","Samuel Braun","Laura Stein"]

suche_a = "Paul Becker"
suche_b = "Li"
suche_c = "L"
suche_d = "Schröder"

print("\nAufgabe 8\n")
gefunden = False
# Aufgabenteil a
for name in namen:
    if name==suche_a:
        print(f"Name '{suche_a}' gefunden")
        gefunden = True
if gefunden == False:
    print(f"Name '{suche_a}' nicht gefunden")

# Aufgabenteil b
for name in namen:
    if name.startswith(suche_b):
        print(f"Name beginnend mit '{suche_b}' gefunden: {name}")
        gefunden = True
if gefunden == False:
    print(f"Name beginnend mit '{suche_b}' nicht gefunden")

# Aufgabenteil c
search2list=[]
for name in namen:
    if name.startswith(suche_c):
        search2list.append(name)
for name in search2list[0:3]:
    print(name, end=", ")

print()
# Aufgabenteil d
for index, name in enumerate(namen):
    if name.endswith(suche_d):
        print(f"Name wurde gefunden am Index {index}.")

# Aufgabe 9:
# Berechne das Reziproke (den Kehrwert) der Brüche in der Liste 'brueche'.
# Gebe die Werte aus. Im Fall einer Division durch null gebe 'DIV 0' aus.

brueche = ["1/4", "3/2", "0/5", "23/100"]

print("\nAufgabe 9\n")

for bruch in brueche:
    strlist_bruch = bruch.split("/")
    if strlist_bruch[0] != "0":
        print(int(strlist_bruch[1])/int(strlist_bruch[0]))
    else: print("DIV 0")

# Aufgabe 10:
# Durchlaufe die Zahlenliste und berechne Summe und Durchschnitt
# bis zum jeweiligen Index. Also:
# 1. Iteration: Summe = 15, Durchschnitt = 15
# 2. Iteration: Summe = 61, Durchschnitt = 30.5
# usw.
 
zahlen = [15,46,13,24,78,94,34,67,59,82]

print("\nAufgabe 10\n")

n_elem = 0
sum_elems = 0

for zahl in zahlen:
    n_elem += 1
    sum_elems += zahl
    print(f"Summe: {sum_elems}, Durchschnitt: {(sum_elems/n_elem):.2f}")

# Aufgabe 11:
# In 'message encoded' ist eine ASCII- verschlüsselte Botschaft versteckt.
# Dekodiere die Botschaft und gebe sie aus.

message_encoded = [80, 121, 116, 104, 111, 110, 32, 105, 115, 116, 32, 116, 111, 108, 108, 33]

print("\nAufgabe 11\n")

# Variante 1
message_decoded = []
for letter in message_encoded:
    message_decoded.append(chr(letter))
print("".join(message_decoded))

# Variante 2
message_decoded = "".join(list(chr(b) for b in message_encoded))
print(message_decoded)

# Aufgabe 12
# Gebe den folgenden Satz ohne Vokale aus.

satz = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam."

print("\nAufgabe 12\n")

# Variante 1
no_vocals = []
for char in satz:
    if char not in "aeiou":
        no_vocals.append(char)

print("".join(no_vocals))

# Variante 2
for char in satz:
    if char not in "aeiou":
        print(char, end="")
print()

# Aufgabe 13
# Zähle die Vokale und Konsonanten pro Wort in dem Satz aus Aufgabe 4.
# Gebe das Ergebnis in der Form aus:
# "Das Wort Lorem enthält 2 Vokale und 3 Konsonanten."

print("\nAufgabe 13\n")

satz_split = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam.".split(" ")

for wort in satz_split:
    vokale = 0
    konsonanten = 0
    for char in wort:
        if char.isalpha():
            if char in "aeiou":
                vokale += 1
            else:
                konsonanten += 1
    print(f"Das Wort {wort} enthält {vokale} {"Vokal" if vokale == 1 else "Vokale"} und {konsonanten} Konsonanten.")

# Aufgabe 14
# Ordne die Liste 'schule' nach Klassenstärke.

schule = [["1. Klasse",21],["2. Klasse",19],["3. Klasse",22],["4. Klasse",24],["5. Klasse",23],
          ["6. Klasse",20],["7. Klasse",27],["8. Klasse",26],["9. Klasse",28],["10. Klasse",25]]

print("\nAufgabe 14\n")

# Variante 1
anzahl = []
schule_sorted = []

for klasse in schule:
    anzahl.append(klasse[1])

anzahl.sort()

for num in anzahl:
    for klasse in schule:
        if klasse[1] == num:
            schule_sorted.append(klasse)

print(schule_sorted)

# Variante 2 mit Lambda- Funktion (lernt ihr noch kennen)
schule1 = [["1. Klasse",21],["2. Klasse",19],["3. Klasse",22],["4. Klasse",24],["5. Klasse",23],
          ["6. Klasse",20],["7. Klasse",27],["8. Klasse",26],["9. Klasse",28],["10. Klasse",25]]

schule1.sort(key=lambda x: x[1])
print(schule1)

# Aufgabe 15:
# Gebe zunächst die Angebotsliste aus. Simuliere dann einen Einkauf,
# indem du die entsprechenden Warennummern per Eingabe einer kommagetrennten
# Liste. Gebe anschließend einen Kassenzettel aus mit den einzelnen
# Warenposten und des Gesamtpreises.

waren = [["1: Milch", 1],["2: Möhren", 1.99],["3: Butter", 2.2],["4: Käse", 3.4],
         ["5: Lachs", 10.99],["6: Brot", 2.0],["7: Tabak", 6.0],["8: Sekt", 5.6]]
 
print("\nAufgabe 15\n")

print("Warenliste")
for ware in waren:
    print(f"{ware[0]} - {ware[1]} Euro")

einkaufsliste = "1,5,8".split(",") #input("Gebe die Warenummern für deine Einkaufsliste kommagetrennt ein.\n").split(",")
warenkorb = []

for ware in einkaufsliste:
    warenkorb.append(waren[int(ware)-1])

gesamtpreis = 0

print("\nKassenzettel")
for ware in warenkorb:
    print(f"{ware[0].split(": ")[1]}: {ware[1]} Euro")
    gesamtpreis += ware[1]
print(f"Summe: {gesamtpreis} Euro")

 