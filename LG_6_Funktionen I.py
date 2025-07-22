# Aufgabe 1: Schreibe eine Funktion, die einen Münzwurf
#            simuliert und das Ergebnis ausgibt. Nutze dazu 
#            eine geeignete Methode des random- Moduls.

print("\nAufgabe 1\n")

import random

# Mögliche Varianten mit 'choice', 'randint' oder 'sample' 
# aus dem random- Modul
def flipcoin():
    return random.choice(["Kopf","Zahl"])

print(flipcoin())

def flipcoin_1():
    liste = ["Kopf","Zahl"]
    return liste[random.randint(0,1)]
    # oder:
    # return ["Kopf","Zahl"][random.randint(0,1)]

print(flipcoin_1())

import random
def flipcoin_2():
    return random.sample(["Kopf","Zahl"],1)[0]

print(flipcoin_2())

# Aufgabe 2: Schreibe eine Funktion, die mehrere Münzwurfe
#            simuliert und die Häufigkeit von Kopf und Zahl
#            ausgibt. Nutze dazu eine geeignete Methode des 
#            random- Moduls.

print("\nAufgabe 2\n")

# Variante 1
import random
def multiflipcoin(num):
    cnt = [0,0]
    for n in range(num):
        if random.choice(["Kopf","Zahl"]) == "Kopf":
            cnt[0] += 1
        else:
            cnt[1] += 1
    print(f"Kopf fiel {cnt[0]} mal, Zahl {cnt[1]} mal.")
    print(f"{"Kopf hat gewonnen" if cnt[0] > cnt[1] else "Zahl hat gewonnen" if cnt[1] > cnt[0] else "Gleichstand!"}")

multiflipcoin(10)

# Variante 2 mit List- Comprehension
import random
def multiflipcoin_1(num):
    cnt = [random.choice(["Kopf","Zahl"]) for n in range(num)]
    print(f"Kopf fiel {cnt.count("Kopf")} mal, Zahl {cnt.count("Zahl")} mal.")
    print(f"{"Kopf hat gewonnen" if cnt.count("Kopf") > cnt.count("Zahl") else "Zahl hat gewonnen" if cnt.count("Zahl") > cnt.count("Kopf") else "Gleichstand!"}")

multiflipcoin_1(10)

# Variante, wenn nur interessiert, ob Kopf oder Zahl gewonnen hat.
def multiflipcoin_2(num):
    cnt = 0
    for n in range(num):
        if random.choice(["Kopf","Zahl"]) == "Kopf":
            cnt += 1
        else:
            cnt -= 1
    if cnt > 0:
        print("Kopf hat gewonnen.")
    elif cnt < 0:
        print("Zahl hat gewonnen.")
    else: 
        print("Gleichstand!")

multiflipcoin_2(10)

# Variante, wenn nur interessiert, ob Kopf oder Zahl gewonnen hat.
import random
def multiflipcoin_3(num):
    cnt = [1 if random.choice(["Kopf","Zahl"]) == "Kopf" else -1 for n in range(num)]
    if sum(cnt) > 0:
        print("Kopf hat gewonnen.")
    elif sum(cnt) < 0:
        print("Zahl hat gewonnen.")
    else: 
        print("Gleichstand!")

multiflipcoin_3(10)

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

# Variante 1
# Implementierung mit Liste oder Tuple als Parameter
def linearFunktion(p1:list|tuple, p2:list|tuple):
    # m = (y2 - y1)/(x2 - x1)
    m = ((p2[1] - p1[1]) / (p2[0] - p1[0]))
    # Grundformel nach n umstellen
    # n = f(x) - mx
    n = p1[1] - m*p1[0]
    print(f"Die Formel der Geraden ist f(x) = {m}x + {n}. Die Y- Achse wird bei y = {n} geschnitten.")
    print(f"Die Formel der Geraden ist f(x) = {m}x {"+" if n>=0 else "-"} {abs(n)}. Die Y- Achse wird bei y = {n} geschnitten.")

linearFunktion((2,4), (1,0))

# Variante 2
# Implementierung mit Dictionary
points = {"x1": 0, "y1": 1, "x2": 1 , "y2": 2}
points2 = {"x1": 2, "y1": 1, "x2": 1 , "y2": -7}

def linearFunktion_1(coord:dict):
    # m = (y2 - y1)/(x2 - x1)
    m = (coord["y2"] - coord["y1"]) / (coord["x2"] - coord["x1"])
    # Grundformel nach n umstellen
    # n = f(x) - mx
    n = coord["y1"] - m*coord["x1"]
    print(f"Die Formel der Geraden ist f(x) = {m}x + {n}. Die Y- Achse wird bei y = {n} geschnitten.")
    print(f"Die Formel der Geraden ist f(x) = {m}x {"+" if n>=0 else "-"} {abs(n)}. Die Y- Achse wird bei y = {n} geschnitten.")

linearFunktion_1(points2)

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

def oldest(elems:dict):
    for k,v in elems.items():
        if v == max(elems.values()):
            print(f"Die älteste Person ist {k} mit {v} Jahren.")

oldest(leute)

# Aufgabe 8: Schreibe die Funktion aus Aufgabe 7 so um,
#            dass sie mehrere Personen ausgeben kann, die
#            alle das höchste Alter haben, aber nur eine 
#            Person, sollte diese die älteste sein.

print("\nAufgabe 8\n")

leute2 = {"Kerstin": 50, "Manfred": 65, "Lilly": 25, "Egon" : 65, "Ida" : 65}

# Variante 1
def oldest2(crowd:dict):
    maxKey = []
    maxVal = 0
    for k,v in crowd.items():
        if v > maxVal:
            maxKey.clear()
            maxKey.append(k)
            maxVal = v
        elif v == maxVal:
            maxKey.append(k)
    if len(maxKey) > 1:
        #print(f"{("".join(str(maxKey).split()).strip("[]")).replace("'", "")} sind die Ältesten.")
        #print(*maxKey, "sind die Ältesten.")
        print(", ".join(maxKey[0:-1]),"und",maxKey[-1], "sind die Ältesten mit", maxVal, "Jahren.")
    else:            
        print(f"{maxKey} ist am ältesten mit", maxVal, "Jahren.")

oldest2(leute2)

# Variante 2
def oldest3(crowd:dict):
    maxKey = []
    for k,v in crowd.items():
        if v == max(crowd.values()):
            maxKey.append(k)
    if len(maxKey) > 1:
        print(", ".join(maxKey[0:-1]),"und",maxKey[-1], "sind die Ältesten mit", max(crowd.values()), "Jahren.")
    else:            
        print(f"{maxKey} ist am ältesten mit", max(crowd.values()), "Jahren.")

oldest3(leute2)

# Variante 3
def oldest4(crowd:dict):
    maxKey = [person for person, age in crowd.items() if age == max(crowd.values())]
    if len(maxKey) > 1:
        print(", ".join(maxKey[0:-1]),"und",maxKey[-1], "sind die Ältesten mit", max(crowd.values()), "Jahren.")
    else:            
        print(f"{maxKey} ist am ältesten mit", max(crowd.values()), "Jahren.")

oldest4(leute2)

# Aufgabe 9:  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
#             und dieses zurück gibt.
#             Next Level: Es sollen bestimmte Zeichen ausgeschlossen werden.

print("\nAufgabe 9\n")

def pwgenSimple(pwLength:int, ausschluss:str="")->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @return: Zufällige Zeichenkette
    """
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    from random import sample 
    pwPool=list(set(ascii_lowercase + ascii_uppercase + digits + punctuation) - set(ausschluss))
    #print(sorted(pwPool))     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

#print(pwgenSimple(20))
print(pwgenSimple(20, ";.@A12"))

# Aufgabe 10: Schreibe einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
#             aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
#             übernimmt und ein entsprechendes Passwort zurück gibt.
#             Next Level: Es sollen bestimmte Zeichen ausgeschlossen werden.

print("\nAufgabe 10\n")


def pwgenPro(lows:int, caps:int, nums:int, specs:int=0, ausschluss:str="")->str:
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(list(set(ascii_lowercase)-set(ausschluss)), lows)
    capLetters=sample(list(set(ascii_uppercase)-set(ausschluss)), caps)
    numbers=sample(list(set(digits)-set(ausschluss)), nums)
    specChar=sample(list(set(punctuation)-set(ausschluss)), specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

print(pwgenPro(2,3,4,4,";.@a12"))
print(pwgenPro(2,3,4,4))