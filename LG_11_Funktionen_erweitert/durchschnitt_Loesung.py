# Aufgabe:
# Implementiere die Funktion "durchschnitt", welche das arithmetische Mittel (den Durchschnitt) berechnet. 
# Die Funktion kann beliebig viele Zahlen übergeben bekommen.

# Lösung: Anfang
def durchschnitt(*nums):
    return sum(nums)/len(nums)
# Lösung: Ende

# Variante 2
def durchschnitt1(*nums):
    sum_nums = 0
    n_elems = 0
    for elem in nums:
        sum_nums += elem
        n_elems += 1
    return sum_nums/n_elems

# Beispielaufruf:
print(durchschnitt(1,2,3,4,5,6,7,8,9)) # gibt 5.0 aus
print(durchschnitt1(1,2,3,4,5,6,7,8,9)) # gibt 5.0 aus