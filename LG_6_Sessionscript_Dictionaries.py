"""
DIE METHODEN DER DICTIONARIES


clear()                 Entfernt alle Elemente aus dem Dictionary.
copy()	                Erstellt eine flache Kopie des Dictionaries.
fromkeys()	            Erstellt ein neues Dictionary mit Schlüsseln aus seq und dem Wert value (Standardmäßig None).
get()	                Gibt den Wert für den angegebenen Schlüssel zurück. Wenn der Schlüssel nicht vorhanden ist, wird default zurückgegeben (Standardmäßig None).
items()	                Gibt eine Ansicht der (Schlüssel, Wert)-Paare des Dictionaries zurück.
keys()	                Gibt eine Ansicht der Schlüssel des Dictionaries zurück.
pop()	                Entfernt den Schlüssel und gibt den entsprechenden Wert zurück. Wenn der Schlüssel nicht vorhanden ist, wird default zurückgegeben (Standardmäßig wird ein KeyError ausgelöst).
popitem()	            Entfernt und gibt ein beliebiges (Schlüssel, Wert)-Paar aus dem Dictionary zurück. Löst einen KeyError aus, wenn das Dictionary leer ist.
setdefault()	        Gibt den Wert für den angegebenen Schlüssel zurück. Wenn der Schlüssel nicht vorhanden ist, wird er mit dem Wert default eingefügt und zurückgegeben (Standardmäßig None).
update()	            Aktualisiert das Dictionary mit den (Schlüssel, Wert)-Paaren aus other, überschreibt bestehende Schlüssel.
values()	            Gibt eine Ansicht der Werte des Dictionaries zurück.
"""
# Dictionaries sind mutable

person = ["Robert", 50, "12345 Berlin"] # Person als Liste
person1 = {}    # =dict()
person1 = {"Name":"Robert", "Alter":50, "Adresse": "12345 Berlin"} # Person als Dictionary
person2 = person1.copy()
# Person 2 erhält alle Items der Person 1, ist aber eine eigenständige Kopie.

print("Name von Person 1:",person1["Name"])
print("Name von Person 2:",person2["Name"])
# Alternativ mit der get()- Methode:
print("Name von Person 2 mittels .get():", person2.get("Name"))

person1["Name"] = "Roberta" # Diese Änderung passiert in Person 2 nicht, da Kopie

print("Name von Person 2 nach Änderung des Namen von Person 1:",person2["Name"])

person3 = {}
person3 = person3.fromkeys(person1) # Person 3 erhält alle Keys, aber nicht die Values von Person 1
print(person3)

# .fromkeys() kann auch zum Entfernen von Duplikaten aus Listen verwendet werden:
liste1 = [1,1,4,2,1,2]
print(set(liste1)) # Entfernt zwar Duplikate, aber sortiert die Werte auch

print(list({}.fromkeys(liste1))) # Das entfernt Duplikate und beibehält die Reihenfolge

print(person1.items())
# Ausgabe: dict_items([('Name', 'Roberta'), ('Alter', 50), ('Adresse', '12345 Berlin')])

for key, value in person1.items():
    print(key, value, sep=" -> ")

# Ausgabe:
"""
Name -> Roberta
Alter -> 50
Adresse -> 12345 Berlin
"""

# Der Value zu einem Key wird überschrieben, weil es den Key bereits gibt.
person1.update({"Name": "Hans"}) 

print(person1.values()) # Ausgabe der Values

# Hier wird eine neues Key:Value Paar angelegt, weil es den Key noch nicht gibt:
person1.update({"Straße": "Bahnhofstr."}) 

print(person1.items())

# Ein beliebiges Key,Value Paar wird aus dem Dict enfernt und der Value zurückgegeben,
# um ihn z.B. in einer Variablen zu speichern
print(person1.popitem())    

# Hier wird ein bestimmtes Key,Value Paar aus dem Dict enfernt und der Value zurückgegeben,
# um ihn z.B. in einer Variablen zu speichern
print(person1.pop("Name"))
print(person1.keys()) # Ausgabe der Keys des Dictionaries

person1.clear() # Löschung aller Einträge des Dictionaries
print("Alle Einträge gelöscht:", person1)