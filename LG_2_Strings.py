# Gegeben seien die Zeichenketten (Strings) 'unsinn' und 'kauderwelsch'.
# Löse die folgenden Aufgaben mit Hilfe der Builtin- Funktionen
# und / oder der Methoden des Datentyps 'str'.

# Referenz der Builtin Funktionen:
# https://docs.python.org/3/library/functions.html

# Referenz der String- Methoden:
# https://docs.python.org/3/library/stdtypes.html#string-methods


unsinn = "MaxUndMoritz,DickUndDoof...vonPontiusBisPilatusIckLoof"
kauderwelsch ="FCMQDICXLTJRE7YFBXZDCAVHNBVNFWLRELOOFBJHBVAWEUGJPJMYJS"

# 1. Wieviele Zeichen enthält die Variable 'unsinn'?

print("\nAufgabe 1\n")
print(len(unsinn))

# 2. Enthalten die Variablen 'unsinn' und 'kauderwelsch' 
#    gleichviele Zeichen?

print("\nAufgabe 2\n")
print(len(unsinn)==len(kauderwelsch))

# 3. Beim wievielten Buchstaben der Variable 'unsinn' 
#    beginnt die Zeichkette 'Bis'?

print("\nAufgabe 3\n")
print(unsinn.find("Bis") + 1)

# 4. Wie oft kommt das Wort 'Und' in der Variable 'unsinn' vor?

print("\nAufgabe 4\n")
print(unsinn.count("Und"))

# 5. In der Variable 'kauderwelsch' kommt der Buchstabe 'V'
#    dreimal vor. An welchen Indizes?

print("\nAufgabe 5\n")
V_firstIndex = kauderwelsch.find("V")
V_secondIndex = kauderwelsch.find("V", V_firstIndex + 1)
V_thirdIndex = kauderwelsch.find("V", V_secondIndex + 1)

print(f"Erster Index: {V_firstIndex}, zweiter Index: {V_secondIndex}, dritter Index: {V_thirdIndex}")

# 6. Kommt die Zeichenkette 'loof' unabhängig von
#    Groß- oder Kleinschreibweise in beiden Variablen vor?

print("\nAufgabe 6\n")
print("loof" in unsinn.lower())
print("loof" in kauderwelsch.lower())

# 7. Ist das 13. Zeichen (Index 13) von 'kauderwelsch' eine Zahl?

print("\nAufgabe 7\n")
print(kauderwelsch[13].isalnum())

# 8. Multipliziere das Zeichen aus Aufgabe 7 mit 3. Das Ergebnis
#    soll 21 sein.

print("\nAufgabe 8\n")
print(int(kauderwelsch[13]) * 3)

# 9. Ersetze alle Vorkommen des Buchstaben 'B' in der Variable 'kauderwelsch' mit '8'.

print("\nAufgabe 9\n")
kauderwelsch = kauderwelsch.replace("B","8")
print(kauderwelsch)

# 10. Finde eine geignete Methode, um die Variable 'unsinn' an den
#     drei Punkten ('...') in zwei Teile zu trennen.

print("\nAufgabe 10\n") 
print(unsinn.split("..."))

# Zusatzaufgaben:
# Z1: Beginnt die zweite Hälfte der Variablen 'unsinn' mit 'von'?

print("\nZusatzaufgaben\n")
print("\nZ1\n")

print(len(unsinn)/2 == unsinn.find("von")) 

# Z2: Finde drei Wege, um zu zeigen, dass die Zeichenkette 'oo'
#     schreibweisenunabhängig sowohl in der Variable 'unsinn' 
#     als auch in der Variable 'kauderwelsch' vorkommt.

print("\nZ2\n")
print(bool(kauderwelsch.lower().count("oo")) and bool(unsinn.lower().count("oo")))
print(kauderwelsch.lower().find("oo")>=0 and unsinn.lower().find("oo")>=0)
print("oo" in kauderwelsch.lower() and "oo" in unsinn.lower())

