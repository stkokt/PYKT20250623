liste = [5,6,7,8,9]

for index, elem in enumerate(liste):
    print(f"am Index {index}: {elem}")

print()

liste2= [5,5,6,5,7,9]
starten=0
for elem in liste2:
    print(f"am Index {liste2.index(elem, starten)}: {elem}")
    starten += 1


dictionary = {"Name":"Paul", "Alter":40, "Beruf":"Schlosser"}
# print(dictionary["Name"])
# print(list(dictionary.values())[0])
# print(list(dictionary.keys())[0])

# for k,v in dictionary.items():
#     if k == "Alter":
#         print(f"{k} : {v}")

dictionary.update({"Alter":31})
#print(dictionary)

dictionary.update({"PLZ":12345})
##print(dictionary)

print(dictionary.get("Stadt"))
# print(dictionary["Stadt"])    # wirft Fehlermeldung

dictionary.setdefault("region", "Nordrhein-Westfalen") 
print(dictionary)


string = "Hallo Welt"
print(string[0:5:2])

for x in range(5):
    for y in range(2):
        print(x*y, end=" ")

print()

x = 0
while x < 5:
    y = 0
    while y < 2:
        print(x*y, end=" ")    
        y += 1
    x += 1

print()

liste = [1,2,3]
def manipulation(input_liste):
     input_liste[1] = 4
     print(id(input_liste))
     return input_liste

print(id(liste))
print(id(manipulation(liste)))

def produkt(x, y, z):
     print(x - (y * z))
produkt(5,z=4,y=2)


zahlen_liste = [1,2,3]
print(id(zahlen_liste))
zahlen_liste = [4,5,6]
print(id(zahlen_liste))
# print(id(zahlen_liste[::-1]))

print(max("berta", "bertax", "Johannes", "DieteR"))

#print("Hallo, ich bin {} {}".format("Stefan"))

person = {"nachname": "Dieter",
                "vorname": "Ute",
                "alter": 22,
                "ausweisnummer": 666
}
print(person["nachname"])


def funktion(*x,**y):

     print(len(x))

     print(y["salz"])

funktion(x=1,salz=True)

def func(x, y=1):
    return x*y

print(func(10))
print(func(10,2))

listeA = []
listeA.append([1,2,3])
print(listeA)
listeA.extend("123")
print(listeA)
listeA.remove("1")
print(listeA)

print(list(range(1,6)).pop(3))

liste = list(range(6))

liste.pop(3)

liste.extend([3,4,3])

liste.remove(3)

del liste[:3]
print(liste)

class meineKlasse():
    cnt = 0
    def __init__(self, name):
        self._name = name
    def hallo(self):
        print(f"Hallo {self._name}")

peter = meineKlasse("Peter")
peter.hallo()
susi = meineKlasse("Susi")
susi.hallo()

print