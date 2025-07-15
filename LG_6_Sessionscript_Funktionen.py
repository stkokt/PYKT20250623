# FUNKTIONEN

# Schlüsselwort: def

def eineFunktion(params):   # Funktionskopf: def + name + Klammern + evt. Parameter in den Klammern
    print(params)           # Funktionskörper: Funktionsalgorithmus (mit oder ohne return)

eineFunktion((1,2,3))


def zweiteFunktion(params):
    print(params)
    return params
    print("Hallo") # Toter Code, kann nicht mehr erreicht werden wegen return in Zeile davor

print(zweiteFunktion("Welt"))

def dritteFunktion(param1, param2): # Mehrere Parameter kommagetrennt
    print(param1)
    return param2

var3 = dritteFunktion("Hallo", "Welt")

print(var3)

# Doc- Strings zur internen Dokumentation der Funktion

def vierteFunktion(param1:int|float, param2:int|float) -> int|float: # Type Annotations (Type Hints)
    # Doc String als Mouseover- Effekt
    """
    @brief: Gibt die Summe zweier Zahlenargumente zurück.
    @param1: Eine Zahl
    @param2: Eine Zahl
    @return: Summe der Zahlen
    @see: Eine im Kontext wichtige Funktion
    """
    return param1 + param2

# Type Annotations erzwingen nichts. Obwohl mit int|float getaggt,
# können auch Strings übergeben werden
var4 = vierteFunktion("Hallo", " Welt")

print(var4)

# Type Annotations in der Parameterbeschreibung haben aber
# den positiven Nebeneffekt, dass man die Methoden der Datenklasse
# im Funktionskörper mit dem Punkt- Operator angezeigt bekommt.
def fünfteFunktion(param:str):
    print(param.startswith("Hallo"))

fünfteFunktion("Hallo Welt") # Ausgabe: True

