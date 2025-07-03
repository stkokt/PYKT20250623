# Aufgabe 1: Setze folgenden Pseudocode in Python um:

"""
BEGIN

IF "Hast du Lust ins Kino zu gehen?" THEN
    IF "Ist ein guter Film im Kino?" THEN
        IF "Hast du genug Geld?" THEN
            "Gehe ins Kino!"
        ELSE
            "Spar etwas Geld und gehe ein anderes Mal."
        END IF
    ELSE
        "Warte, bis ein guter Film im Kino ist."
    END IF
ELSE
    IF "Hast du andere Pläne?" THEN
        "Mache deine anderen Pläne."
    ELSE
        IF "Ist das Wetter schön?" THEN
            "Gehe nach draußen und genieße das Wetter."
        ELSE
            "Bleibe zu Hause und entspanne dich."
        END IF
    END IF
END IF

END

"""

print("\nKino- Aufgabe\n")

kino = input("Hast du Lust ins Kino zu gehen? j/n\t")

"""
# Wenn man mehrere positive Antwortmöglichkeiten vorgeben will:
ja_antworten = "jJjaJaYesyes" # aber auch "es" funktioniert
# besser als Liste formulieren:
ja_antworten = ["j","J","ja","Ja","Yes","yes"]
if kino in ja_antworten
"""
if kino == "j":
    kino = input("Ist ein guter Film im Kino? j/n\t")
    if kino == "j":
        kino = input("Hast du genug Geld? j/n\t")
        if kino == "j":
            print("Geh ins Kino!")
        else: print("Spar etwas Geld und gehe ein anderes Mal.")
    else: print("Warte, bis ein guter Film im Kino ist.")
else:
    kino = input("Hast du andere Pläne? j/n\t")
    if kino == "j":
        print("Mache deine anderen Pläne.")
    else:
        kino = input("Ist das Wetter schön? j/n\t")
        if kino == "j":
            print("Gehe nach draußen und genieße das Wetter.")
        else: print("Bleibe zu Hause und entspanne dich.")

# Aufgabe 2: Löse die Rindvieh- Aufgabe.

janein=input("Funktioniert die Anlage? j/n\n")

if janein=="j":
    print("Fummel bloß nicht dran rum")
    print("Alles klar!")
else:
    janein=input("Hast du dran rumgespielt? j/n\n")
    if janein=="j":
        print("Du Rindvieh!")
        janein=input("Hat es jemand gemerkt? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Pfeiffe unauffällig 'La Paloma' und verschwinde!")
            print("Alles klar!")
    else:
        janein=input("Wird man dich verantwortlich machen? j/n\n")
        if janein=="j":
            print("Du armes Schwein!")
            janein=input("Kannst du jemandem die Schuld zuschieben? j/n\n")
            if janein=="n":
                print("Du armes Schwein!")
            else:
                print("Alles klar!")
        else:
            print("Kümmer dich nicht drum!")
            print("Alles klar!")
