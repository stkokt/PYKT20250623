# Mutable/ Immutable
# Mutable sind folgende Datentypen
#
#   L = Listen
#   S = Sets
#   D = Dictionaries
#
# Bytearrays sind auch mutable, behandeln wir aber 
# in diesem Kurs nicht.
#
# ALLE ANDEREN DATENTYPEN SIND IMMUTABLE !


a = 10      # a wird mit 10 initialisiert
# Auf welche Speicherstelle schaut a?
print("RAM a = 10: ", id(a))    
a = 11      # Neuzuweisung a = 11
# Auf welche Speicherstelle schaut a nun? (andere!)
print("RAM a = 11: ", id(a))
b = 10      # b wird mit 10 initialisiert
# Auf welche Speicherstelle schaut b?
# Auf dieselbe, auf die a noch schaute, als 
# a noch 10 war.
print("RAM b = 10: ", id(b))

# Merke:
# Immutable sind Datentypen dann, wenn bei Wertänderung
# ein neues Speicherobjekt entsteht

# Listen sind z.B. mutable, weil sich die Speicherstelle
# für die Metainformationen nicht ändert, wenn sich 
# ihre Elemente ändern:
liste = [10,11]
print("RAM Liste Meta:",id(liste))
print(id(liste[0]))
print(id(liste[1]))
liste[0] = 12 # Wertänderung beim ersten Listenelement
# aber Speicherplatz der Metaebene unverändert:
print("RAM Liste Meta nach Veränderung:",id(liste))
print(liste[0])

# Tupele sind immutable

c = (10, 11)
#c[0] = 12   # Das geht nicht!

c1 = ([10, 11],11)
c1[0][0] = 12   # Das wiederum geht!
# Erklärung:
# Tupele sind zwar immutable, aber Listen nicht.
# Die im Tuple enthaltene Liste kann ich also ändern.
# Das Tuple ändert sich dabei nicht, weil sich die
# Speicheradressen der Tuple- Elemente nicht ändern
 
print(c1[0])

# Auch Strings sind immutable.
str_var = "text"
# Lesender Zugriff auf Elemente des Strings: Ja
print(str_var[0])
# aber schreibender Zugriff nicht erlaubt:
# str_var[0] = "n"
