# Aufgabe 1:  Schreibe eine Funktion zur Ermittlung, ob ein Jahr ein Schaltjahr ist.

print("\nAufgabe 1\n")

def schaltjahr():
    year = int(input("Gebe eine Jahreszahl ein:\n"))
    schalt = True if year%400==0 or (year%4==0 and year%100!=0) else False
    if schalt:
        print(f"{year} ist ein Schaltjahr.")
    else: 
        print(f"{year} ist kein Schaltjahr.")
    return schalt

schaltjahr()

# Aufgabe 2:  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: 
#             einen Zahlenwert und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang 
#             oder Fläche zu verstehen ist. Radius soll dabei als Defaultwert eingestellt sein. Die 
#             Funktion soll dann die jeweils restlichen Werte ausgeben.

print("\nAufgabe 2\n")

# Variante 1
def kreis(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            d=2*val
            a=pi*val**2
            u=pi*2*val
            print(f"Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "d":
            r=val/2
            a=(pi*val**2)/4
            u=pi*val
            print(f"Radius: {round(r, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")
        case "a":
            r=sqrt(val/pi)
            d=2*r
            u=pi*2*r
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Umfang: {round(u, 2)}")
        case "u":
            r=val/(2*pi)
            d=2*r
            a=pi*r**2
            print(f"Radius: {round(r, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}")

kreis(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche

# Variante 2
def kreis1(val:int|float, mod:str="r")->None:    # Argument "mod" ist per default mit "r" für Radius belegt
    '''
    mod bezeichnet, welchen Wert die übergebene 
    Variable darstellt
    Radius="r"      Durchmesser="d"
    Fläche="a"      Umfang="u"
    '''
    from math import pi, sqrt   # Import der Mathebibliothek für PI und Wurzelziehen

    radius = 0

    match mod:  # die verschiedenen Berechnungen in Abhängigkeit vom Modus
        case "r":
            radius = val
        case "d":
            radius = val/2
        case "a":
            radius = sqrt(val/pi)
        case "u":
            radius = val/(2*pi)

    d=2*radius
    a=pi*radius**2
    u=pi*2*radius
    print(f"Radius: {round(radius, 2)}, Durchmesser: {round(d, 2)}, Flaeche: {round(a, 2)}, Umfang: {round(u, 2)}")

kreis1(10)       # Aufruf der Funktion mit nur einem Argument (default=Radius)
kreis1(20, "a")  # Aufruf mit zwei Argumenten, erster Wert gilt als Fläche



# Aufgabe 3: Schreibe eine Funktion, die als Argument ein 
#            verschachteltes Dictionary von Schülern und 
#            deren Noten in einzelnen Fächern übernimmt.
#            Die Funktion soll den Notendurchschnitt jedes 
#            Schülers und jedes Fachs zurückgeben.
#            Next Level: 
#            Schreibe die Funktion so, dass die Schüler unterschiedliche
#            und unterschiedlich viele Unterrichtsfächer haben können.

print("\nAufgabe 3\n")

schulnoten = {
    "Max": {"Mathe": 2.5, "Deutsch": 1.2, "Englisch": 3.4},
    "Lena": {"Mathe": 1.5, "Deutsch": 2.4, "Englisch": 1.8},
    "Tom": {"Mathe": 3.3, "Deutsch": 3.0, "Englisch": 2.8}
}

schulnoten2 = {
    "Max": {"Mathe": 2.5, "Deutsch": 1.2, "Englisch": 3.4},
    "Lena": {"Musik": 1.5, "Deutsch": 2.4, "Englisch": 1.8},
    "Tom": {"Mathe": 3.3, "Deutsch": 3.0, "Englisch": 2.8, "Physik": 1.8}
}

# Variante 1 (mit Hilfs- Dictionary)
def avgGrades(grades:dict):
    class_notes = {}
    for student, notes in grades.items():
        #print(grades.items())
        print(f"Der Notendurchschnitt von {student} ist {round(sum(notes.values())/len(notes.values()),1)}.")
    for topic in grades.values():         
        class_notes.update(topic)
    class_list = [[fach, 0, 0] for fach in class_notes.keys()]
    for classes in grades.values():
        for a_class, grade in classes.items():
            for topic in class_list:
                if a_class == topic[0]:
                    topic[1] += grade
                    topic[2] +=1
    #print(class_notes, class_list, sep="\n")
    for topic in class_list:
        print(f"{topic[0]} hat einen Notendurchschnitt von {round(topic[1]/topic[2],1)}.")

avgGrades(schulnoten2)

# Variante 2 (mit Hilfs- Set)
def avgGrades(grades:dict):
    class_notes = set()
    for student, notes in grades.items():
        #print(grades.items())
        print(f"Der Notendurchschnitt von {student} ist {round(sum(notes.values())/len(notes.values()),1)}.")
    for topic in grades.values():         
        class_notes.update(topic)
    print(class_notes)
    class_list = [[fach, 0, 0] for fach in class_notes]
    for classes in grades.values():
        for a_class, grade in classes.items():
            for topic in class_list:
                if a_class == topic[0]:
                    topic[1] += grade
                    topic[2] +=1
    #print(class_notes, class_list, sep="\n")
    for topic in class_list:
        print(f"{topic[0]} hat einen Notendurchschnitt von {round(topic[1]/topic[2],1)}.")

avgGrades(schulnoten2)

# Aufgabe 4: Schreibe eine Funktion, die zwei Zahlen als Argumente 
#            übernimmt, miteinander multipliziert und das Produkt 
#            zurückgibt. Schreibe anschließend eine weitere gleichnamige Funktion, die
#            drei Zahlenargumente übernimmt. Prüfe, ob nun die 
#            Funktion noch mit zwei Argumenten aufgerufen werden kann.

print("\nAufgabe 4\n")

def multiply(n1, n2):
    return n1 * n2

def multiply(n1, n2, n3):
    return n1 * n2 * n3

# multiply(5,6) # Aufruf mit 2 Argumenten nicht mehr möglich!

# Aufgabe 5: Schreibe eine Funktion, die als Argumente zwei Listen
#            übernimmt. Die eine Liste soll Artikelnummern enthalten,
#            die andere die dazugehörigen Waren. Die Funktion soll ein
#            Dictionary zurückgeben mit den Artikelnummer als Schlüssel
#            und den Waren als Wert.
#            Tipp: Beschäftige dich mit der Builtin- Funktion zip().

print("\nAufgabe 5\n")

artnr = [1000,1001,1002,1003,1004]
waren = ["Milch","Butter", "Brot", "Äpfel","Kaffee"]
#print(zip(artnr,waren))    # In das reine zip- Objekt kann nicht eingesehen werden.
# Aber mit einer Konvertierung geht's.
#print(dict(zip(artnr,waren)))

# Variante 1
def nrArt(nr:list, name:list):
    targetDict = {}
    for pair in zip(nr,name):
        targetDict.update({pair[0]:pair[1]})
    return targetDict

print(nrArt(artnr, waren))

# Variante 2 (kürzer)
def nrArt1(nr:list, name:list):
    return dict(zip(artnr,waren))

print(nrArt1(artnr, waren))

# Aufgabe 6: Schreibe ein Konsolenmenü, mit dem du zwischen den ersten 
#            beiden Funktionen wählen kannst. 

print("\nAufgabe 6\n")

mod = ""
while mod != "x":
    print("1:   Schaltjahr      2:  Kreis       x:  Beenden")
    mod = input("Gebe den Menüpunkt ein\n")
    match mod:
        case "1":
            schaltjahr()
        case "2":
            var1 = float(input("Gebe einen Zahlenwert ein:\n"))
            var2 = input("Wofür steht der Zahlenwert? " \
            "r=Radius, d=Durchmesser, a=Fläche, u=Umfang\n")
            kreis1(var1, var2)
        case "x":
            break
        case _:
            print("Falschen Menüindex eingegeben!")
            continue