# Aufgabe:
# Implementiere die Funktion "flaecheninhalt"
# Bekommt die Funktion ein Argument übergeben, berechnet sie den Flächeninhalt eines Quadrats
# Bekommt die Funktion zwei Argumente übergeben, berechnet sie den Flächeninhalt eines Rechtecks
# Bekommt die Funktion mehr als zwei oder keine Argumente übergeben, gibt sie eine Fehlermeldung aus
# Hinweis: Verwende die Möglichkeit Argumente als Listen zu übergeben

# Lösung: Anfang
def flaecheninhalt(*zahlen: tuple):
    match len(zahlen):
        case 1:
            return zahlen[0] * zahlen[0] # zahlen[0]**2
        case 2:
            return zahlen[0] * zahlen[1]
        case _:
            return "Bitte nur ein oder zwei Argumente angeben!"
# Lösung: Ende

print(flaecheninhalt(2,"Hallo"))

def flaecheninhalt1(*zahlen: tuple):
    number = False
    for zahl in zahlen:
        #if type(zahl) == int or type(zahl) == float:
        if type(zahl) in (int,float):
            number = True
        else:
            number = False
            break
    if not number:
        return "Mindestens ein Argument ist keine Zahl."
    else:
        match len(zahlen):
            case 1:
                return zahlen[0] * zahlen[0]
            case 2:
                return zahlen[0] * zahlen[1]
            case _:
                return "Bitte nur ein oder zwei Argumente angeben!"

# Variante_Stephan

def flaecheninhalt2(*seiten):
    anzahl = len(seiten)
    
    if anzahl == 1:
        seite = seiten[0]
        return seite * seite
    elif anzahl == 2:
        return seiten[0] * seiten[1]
    else:
        raise ValueError("Die Funktion erwartet genau 1 (Quadrat) oder 2 (Rechteck) Argumente.")


# Beispielaufrufe:
print(flaecheninhalt2(12))          # gibt 144 aus
print(flaecheninhalt(12, 10))      # gibt 120 aus
print(flaecheninhalt1(12, 10.0))
print(flaecheninhalt(12, 10, 20)) # gibt einen Fehler aus
print(flaecheninhalt1(12, "10")) 