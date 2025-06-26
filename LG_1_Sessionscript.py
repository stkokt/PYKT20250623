a = 10              # eine Variable vom Typ 'int' mit dem Wert 10
b = 3.14            # eine Variable vom Typ 'float' mit dem Wert 3.14
c = f"a ist {a}"    # eine Variable vom Typ 'str' mit dem Wert "a ist 10"
print(c)            # Ausgabe von c: "a ist 10"

print(type(c))      # Ausgabe des Typs von c: <class 'str'>

print(a.to_bytes()) # Anwendung einer Methode der Klasse 'int'
print(c.islower())  # Anwendung einer Methode der Klasse 'str'
print(int("01"))    # Konvertierung eines Strings zu einem Integer
# Das ist natürlich nur dann möglich, wenn der String zu einem Integer 
# umgewandelt werden kann. int("Bockwurstsalat") wirft euch einen Fehler

d = int()   # = float(), = str() # Initialisieren einer Variable ohne Wert
d = 3.5     # Wegen dynamischer Typisierung ist d jetzt vom Typ 'float'
print(type(d))
# Alle interpretierten Sprachen verwenden dynamische Typisierung
# Bei typenreinen Sprachen (also alle kompilierten Sprachen) ist das nicht so.
# Typisierung in C oder C++ : float d = 0.0;

d = int(d)  # Hier erfolgt keine Rundung, sondern die Nachkommastellen
            # werden einfach abgeschnitten
print(d)

# Sonderfall: 16 Nachkommastellen alle auf 9, Unschärfe- Fall
e = 1.9999_9999_9999_9999
e = int(e)  
print(e)    # Ausgabe: 2

f = a + b   # Wert der Addition von a und b wird in der Variablen f gespeichert.

a = 10
b = 3.14
g = "Hallo "
h = "lo"

# a + b geht
# a + g geht nicht
# a * g geht
# a / g geht nicht
# g - h geht nicht
# g * b geht nicht
# g + h geht
print(f)
# Merke: Operatoren sind immer kontextbezogen.
# Wenn sie für einen bestimmten Kontext von den 
# Python- Entwicklern nicht implementiert wurden,
# sind sie eben auch nicht verfügbar.
# Gibt dann eine Fehlermeldung, z.B. 'unsupported operand...'

# Eine gemeine Prüfungsfrage
print(3 * "3")
# a) 333    falsch, obwohl genau so in der Konsole zu sehen
# b) "333"  richtig, muss so gedeutet werden: Typ 'str', Wert 333 

i = 10
i = 10 + 1  # neue Wertzuweisung: i = 11
i += 1      # neue Wertzuweisung: i = 12

print(i)

# Membership Operatoren
# Es wird gefragt, ob "a" in "Hallo" enthalten ist. 
print("a" in "Hallo")       # True, weil a in Hallo enthalten
# Es wird gefragt, ob "a" nicht in "Hallo" enthalten ist.
print("a" not in "Hallo")   # False, weil a in Hallo enthalten
