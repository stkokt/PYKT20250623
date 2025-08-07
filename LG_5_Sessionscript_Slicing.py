# SLICING

# Allgemeine Syntax:
# folgt der Logik von range()

# start (Startindex)
# stop (Index, vor dem gestoppt wird)
# step (Schrittweite)

# Beispiele:
# iterable[1:5:2]   Index 1 bis inklusive Index 4 in 2er Schritten
# iterable[1:5]     Index 1 bis inklusive Index 4
# iterable[1::2]    Index 1 bis Ende in 2er Schritten
# iterable[:5]      Anfang bis inklusive Index 4
# iterable[:5:2]    Anfang bis inklusive Index 4 in 2er Schritten
# iterable[::-1]    rückwärts vom letzten Index bis inklusive des ersten

# WICHTIG:
# start, stop, step müssen Integerwerte sein

listeA = [1,2,3,4,5]
# print(listeA[:len(listeA)/2])     # so geht's nicht!
print(listeA[:int(len(listeA)/2)])  # das geht
print(listeA[:len(listeA)//2])      # und das auch.
# auch komplexe Ausdrücke möglich, aber unüblich
print(listeA[:len(listeA)//2 if len(listeA) % 2 == 0 else len(listeA)//2 + 1])


# Anwendbar auf folgende Objekte:
# Iterierbar und indexbasiert

# - Strings
# - Listen
# - Tupele
# - range()- Objekte
# - Bytearray (wird im Kurs aber nicht behandelt)

a_string = "HPayltlhoo_n"
print(a_string[0:-1:2] + a_string[1::2])

a_Tuple = 1,2,3,4,5
print(a_Tuple[2:])

a_range = range(1,51)
for num in a_range[0:10]:
    print(num, end=" ")