# LOOPS
# Das Wichtigste bei Loops: Abbruchbedingung!

# For_ Loop (range- based Loop)
liste = [1,2,3,4,5]
print(liste[-2]) # Zugriff über Index, auch negativ möglich
for zahl in liste: # Ausgabe über einen For- Loop
    print(zahl)

text = "Hallo"
for buchstabe in text: # Auch über str- Variablen lässt sich iterieren
    print(buchstabe)

# For- Loops ohne iterierbares Objekt
"""
z.B. in JAVA, C, C++:
for(int a = 0, a < 10, a++){}
"""
# In Python:
# range- Parameter
# (start, stop(bevor), step)
for zahl in range(1,6): # Die Zahlen von 1 - 5 
    print(zahl)

# Nur stop- Argument
for zahl in range(5): # Die Zahlen von 0 - 4 
    print(zahl)

# Mit step- Argument
for zahl in range(1,10,2): # Die Zahlen 1,3,5,7,9 
    print(zahl)

# Der While- Loop
# Kontrollvariable liegt außerhalb des Loops.
# Sie muss aber im Loop verändert werden, sonst ENDLOSSCHLEIFE !!

cnt = 1
while cnt <= 5:
    print(cnt)
    cnt += 1

# Die Schlüsselwörter 'break' und 'continue':
cnt = 1
# Gefährlich! Wenn cnt != 0, Gefahr einer ENDLOSSCHLEIFE.
# Auch 'while True:' ohne 'break' ENDLOSSCHLEIFE.
while cnt:  
    cnt += 1 # cnt wird verändert.
    if cnt == 3:
        continue # Aktueller Loop- Durchlauf wird abgebrochen.
    if cnt == 10:
        break # Der ganze Loop wird beendet.
    print(cnt)

# LISTEN

listeA = [10, 15.5, 100] # list()

# Listen können natürlich auch Listen als Element 
# enthalten, sogar sich selbst ;)

listeA.append(listeA)
print(listeA[3][3])
print(id(listeA))
print(id(listeA[3]))
print(id(listeA[3][3]))

entfernt = listeA.pop(3) # Wir entfernen die Liste wieder aus der Liste.
# listeA.pop(), also ohne Argument, in diesem Fall möglich: default = pop(-1)
print(listeA)
# pop() liefert den entfernten Wert zurück und kann einer Variablen zugewiesen werden.
print(entfernt) 

print(listeA)
listeA.reverse() # *IN_PLACE*, kein return, daher keine Neuzuweisung möglich
print(listeA)

# Listen können natürlich alle Datentypen gemischt enthalten.
# Dann aber Vorsicht, wenn Vergleichsoperatoren verwandt werden,
# wie z.B. in der Methode 'sort'.
# Hier käme es zu einem Fehler, wenn z.B. ein Element vom Typ 'str' wäre
# und die anderen vom Typ 'int' oder 'float'.
listeA.sort() # *IN_PLACE*, kein return, daher keine Neuzuweisung möglich
print(listeA)








