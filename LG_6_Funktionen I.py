# Aufgabe 1: Schreibe eine Funktion, die einen Münzwurf
#            simuliert und das Ergebnis ausgibt. Nutze dazu 
#            eine geeignete Methode des random- Moduls.

print("\nAufgabe 1\n")

import random

def flipcoin():
    return random.choice(["Kopf","Zahl","Kante","Gulli"])

print(flipcoin())

def flipcoin_1():
    liste = ["Kopf","Zahl","Kante","Gulli"]
    return liste[random.randint(0,3)]
    # oder:
    # return ["Kopf","Zahl","Kante","Gulli"][random.randint(0,3)]

print(flipcoin_1())

# Aufgabe 2: Schreibe eine Funktion, die mehrere Münzwurfe
#            simuliert und die Häufigkeit von Kopf und Zahl
#            ausgibt. Nutze dazu eine geeignete Methode des 
#            random- Moduls.

print("\nAufgabe 2\n")



# Aufgabe 3: Schreibe eine Funktion, die zwei Punkte als Argumente übernimmt, welche
#            Koordinaten für eine Gerade in einem Koordinatensystem darstellen.
#            Also z.B. als Dictionary: {"x1": 0, "y1": 1, "x2": 1 , "y2": 2}
#            Berechne hieraus den Y- Achsenabschnitt und die Formel der linearen Funktion.
#            Grundformel: f(x) = mx + n
#            m = (y2 - y1)/(x2 - x1)
#            n ist der Y- Achsenabschnitt.
#            Zur Prüfung deines Ergebnisses:
#            https://www.mathepower.com/lineare_funktionen.php

print("\nAufgabe 3\n")

# Implementierung mit Liste oder Tuple als Parameter
def linearFunktion_1(p1:list|tuple, p2:list|tuple):
    # m = (y2 - y1)/(x2 - x1)
    m = (p2[1] - p1[1] / p2[0] - p1[0])
    # Grundformel nach n umstellen
    # n = f(x) - mx
    n = p1[1] - m*p1[0]
    print(f"Die Formel der Geraden ist f(x) = {m}x + {n}. Die Y- Achse wird bei y = {n} geschnitten.")
    print(f"Die Formel der Geraden ist f(x) = {m}x {"+" if n>=0 else "-"} {abs(n)}. Die Y- Achse wird bei y = {n} geschnitten.")

linearFunktion_1((5,7), (-2,3))



# Aufgabe 4: Schreibe eine Funktion, die als Argument ein 
#            Dictionary von Vornamen und Nachnamen übernimmt.
#            Gebe mit dieser Funktion die Namen in der Form aus:
#            "Hallo, ich bin [Vorname] [Nachname]."

print("\nAufgabe 4\n")

namen = {"Kater": "Garfield", "Räuber":"Hotzenplotz", "Pipi":"Langstrumpf"}

def whoAmI(names:dict):
    for k,v in names.items():
        print(f"Hallo, ich bin {k} {v}.")

whoAmI(namen)


# Aufgabe 5: Schreibe eine Funktion, die als Argument ein 
#            Dictionary von Waren und deren Preise übernimmt.
#            Die Funktion soll den Gesamtpreis zurückgeben.

print("\nAufgabe 5\n")

produkte = {"Milch": 1.0, "Butter": 3.5, "Brot":2.99, "Äpfel":1.98,"Kaffee":6.99}

def sumValues(elems:dict):
    print("Gesamtpreis der Waren", sum(elems.values()))

sumValues(produkte)

# Aufgabe 6: Schreibe eine Funktion, die aus folgendem
#            Dictionary 'leute' das Durchschnittsalter errechnet.

print("\nAufgabe 6\n")

leute = {"Kerstin": 50, "Manfred": 65, "Lilly": 25}

def avgValues(elems:dict):
    print(f"Durchschnittsalter der Personen: {(sum(elems.values())/len(elems)):.2f}")

avgValues(leute)

# Aufgabe 7: Schreibe eine Funktion, die aus dem Dictionary 'leute'
#            die älteste ermittelt und ausgibt.

print("\nAufgabe 7\n")

for k,v in leute.items():
    if v == max(leute.values()):
        print(f"Die älteste Person ist {k} mit {v} Jahren.")



# Aufgabe 8: Schreibe die Funktion aus Aufgabe 7 so um,
#            dass sie mehrere Personen ausgeben kann, die
#            alle das höchste Alter haben, aber nur eine 
#            Person, sollte diese die älteste sein.

print("\nAufgabe 8\n")

leute2 = {"Kerstin": 50, "Manfred": 65, "Lilly": 25, "Egon" : 65, "Ida" : 55}




# Aufgabe 9:  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
#             und dieses zurück gibt.
#             Next Level: Es sollen bestimmte Zeichen ausgeschlossen werden.

print("\nAufgabe 9\n")



# Aufgabe 10: Schreibe einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
#             aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
#             übernimmt und ein entsprechendes Passwort zurück gibt.
#             Next Level: Es sollen bestimmte Zeichen ausgeschlossen werden.

print("\nAufgabe 10\n")

