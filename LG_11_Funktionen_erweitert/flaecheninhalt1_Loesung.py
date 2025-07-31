# Aufgabe:
# Implementiere die Funktion "flaecheninhalt_rechteck", die den Flächeninhalt eines Rechtecks berechnet.
# Ein Beispielaufruf der Funktion ist vorgegeben und ist unveränderlich.

# Lösung: Anfang
def flaecheninhalt_rechteck(seite_a,seite_b):
    return seite_a * seite_b
# Lösung: Ende

# Variante 1
def flaecheninhalt_rechteck1(**seiten):
    produkt = 1
    for value in seiten.values():
        produkt *= value
    return produkt

# Variante_Stephan

def flaecheninhalt_rechteck2(**kwargs):
    seite_a = kwargs['seite_a']
    seite_b = kwargs['seite_b']
    return seite_a * seite_b

# Beispielaufruf:
print(flaecheninhalt_rechteck(seite_a=12, seite_b=17)) # gibt 204 aus
print(flaecheninhalt_rechteck1(seite_a=12, seite_b=17)) # gibt 204 aus
print(flaecheninhalt_rechteck2(seite_a=12, seite_b=17)) # gibt 204 aus