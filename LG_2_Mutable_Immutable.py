# Mutable/ Immutable
# Mutable sind folgende Datentypen
#   L = Listen
#   S = Sets
#   D = Dictionaries

a = 10 
print("RAM a = 10: ", id(a))
a = 11
print("RAM a = 11: ", id(a))
b = 10
print("RAM b = 10: ", id(b))

liste = [10,11] # "text"
print("RAM Liste Meta:",id(liste))
print(id(liste[0]))
print(id(liste[1]))
liste[0] = 12
print("RAM Liste Meta nach Veränderung:",id(liste))
print(liste[0])
c = ([10, 11],11)
c[0][0] = 12
print(c[0])

str_var = "text"
print(str_var[0])
str_var[0] = "n"
