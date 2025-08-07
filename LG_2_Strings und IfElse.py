# 2_Strings und IfElse



# Aufgabe 1: Prüfe, ob eine String- Variable Text enthält
#            oder leer ist. Gebe eine entsprechende Rückmeldung aus.

print("\nAufgabe 1\n")

text1 = "\t"
text2 = "Hallo"

# Variante 1: Whitespaces werden nicht berücksichtigt.
if text1.isspace(): # Prüfung auf Whitespaces (auch Leerzeichen oder TAB)
    print("String enthält keine Zeichen.")
else:
    print("String enthält Zeichen.")

# Variante 2: Whitespaces werden berücksichtigt.
if text1:   # Prüfung, ob Länge > 0. Besser: if len(text1)>0
    print("String enthält Zeichen")
else:
    print("String enthält keine Zeichen")
    

# Aufgabe 2: Prüfe eine String- Variable. Enthält sie
#            nur Kleinbuchstaben, soll der String umgewandelt 
#            werden, sodass jedes Wort mit einem Großbuchstaben
#            beginnt.

print("\nAufgabe 2\n")

text3 = "Lorem ipsum dolor sit amet"
text4 = "sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat"

if text3.islower():
    text3 = text3.title()

print(text3)

if text4.islower():
    text4 = text4.title()

print(text4)

# Aufgabe 3: Prüfe eine Anrede darauf, ob sie mit "Frau" oder "Herr"
#            beginnt.

print("\nAufgabe 3\n")

anrede1 = "Frau Müller"
anrede2 = "Herr Schmidt"
#print(anrede1.find("Frau")>=0)
print("Frau" in anrede1.split())

if anrede1.startswith("Frau"):
    print(f"{anrede1} ist weiblich.")
else:
    print(f"{anrede1} ist männlich.")

if anrede2.startswith("Frau"):
    print(f"{anrede2} ist weiblich.")
else:
    print(f"{anrede2} ist männlich.")

# Aufgabe 4: Gebe einen vollständigen Namen ein (Vor- und Zuname) und
#            prüfe, ob er mit 'Schmidt' endet.

print("\nAufgabe 4\n")

name = input("Gebe deinen vollständigen Namen ein:\n")

if name.endswith("Schmidt"):
    print("Du bist ein Schmidt!")
else:
    print("Du bist kein Schmidt!")

# Aufgabe 5: Prüfe folgenden String, ob er die Zeichenkette 'amet' enthält.

print("\nAufgabe 5\n")

lorem = "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam."

if lorem.find("amet") >= 0:
    print("String enthält die Zeichenkette 'amet'.")
else:
    print("String enthält die Zeichenkette 'amet' nicht.")

# Aufgabe 6: Prüfe einen String darauf, ob er die Struktur einer 
#            Email- Adresse darstellt. 
#            Mindestbedingung: Ein '@' muss enthalten sein.
#            Weiterführend: Enthält einen Punkt nach dem '@'.

print("\nAufgabe 6\n")

mail = "stefan.koschnik@mein-karrieretutor.de"

# Mindestbedingung:

if '@' in mail:
    print("Gültige Mailadresse.")
else:
    print("Keine gültige Mailadresse.")

# Weiterführend:

if '@' in mail:
    mail_suffix = mail.split("@")[1]
    if mail_suffix.count(".") == 1:
        print("Gültige Mailadresse.")
else:
    print("Keine gültige Mailadresse.")

# Aufgabe 7: Simuliere eine PIN- Eingabe (4- stellig). Prüfe, 
#            ob die Eingabe nur aus Ziffern besteht.

print("\nAufgabe 7\n")

pin = input("Gebe deine PIN ein:\n")

if pin.isdigit() and len(pin) == 4:
    print("PIN- Format ist gültig.")
else:
    print("Ungültiges PIN- Format!")

# Aufgabe 8: Bestimme die Anzahl der Sätze in folgendem String.

print("\nAufgabe 8\n")

lorem2 = """Lorem ipsum dolor sit amet, consetetur sadipscing elitr, 
        sed diam nonumy eirmod tempor invidunt ut labore et dolore 
        magna aliquyam erat, sed diam voluptua. At vero eos et accusam 
        et justo duo dolores et ea rebum. Stet clita kasd gubergren, 
        no sea takimata sanctus est Lorem ipsum dolor sit amet."""

print(f"Der String 'lorem2' besteht aus {lorem2.count(".")} Sätzen.")

# Aufgabe 9: Entferne die Sternchen aus folgendem String.

print("\nAufgabe 9\n")

sternchen = "**Lorem ipsum* dolor**"

print(sternchen.replace("*",""))
# Die strip- Methode entfernt nur die führenden und nachfolgenden *.
print(sternchen.strip("*"))

# Aufgabe 10: Löse die Rindvieh- Aufgabe.
