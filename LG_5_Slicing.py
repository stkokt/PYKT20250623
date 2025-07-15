# Aufgabe 1: Die folgende Liste enthält 80 Elemente. Nutze List- Slicing, um 
#            a) die erste Hälfte auszugeben.
#            b) die letzten 15 Elemente auszugeben.
#            c) die mittleren 40 Elemente auszugeben.
#            d) die letzte Hälfte rückwärts auszugeben. 

big_list =[41, 19, 21, 7, 18, 26, 25, 28, 24, 14, 
           17, 35, 18, 11, 19, 20, 44, 33, 7, 33, 
           7, 35, 5, 35, 46, 50, 9, 4, 41, 39,
           42, 39, 15, 35, 45, 44, 30, 49, 37, 25,
           2, 41, 1, 5, 12, 39, 23, 20, 28, 21,
           17, 39, 36, 18, 22, 49, 36, 4, 42, 16,
           35, 19, 47, 27, 23, 40, 9, 38, 49, 26,
           4, 29, 10, 43, 15, 12, 45, 47, 25, 34]

print("\nAufgabe 1a\n")

print(big_list[0:len(big_list)//2])

print("\nAufgabe 1b\n")

print(big_list[len(big_list)-15:])

print("\nAufgabe 1c\n")

print(big_list[len(big_list)//4:len(big_list)-len(big_list)//4])

print("\nAufgabe 1d\n")

print(big_list[len(big_list)-1:len(big_list)//2-1:-1])

# Aufgabe 2: Slice und konkatiniere die folgende Liste so,
#            dass sie sortiert ist und gebe sie aus.

liste = [5,4,3,2,1,10,9,8,7,6]

print("\nAufgabe 2\n")

liste_sorted = liste[4::-1] + liste[9:4:-1]
print(liste_sorted)

# print(sorted(liste))
# liste.sort()

# Aufgabe 3: Gebe die Quartalsumsätze kumuliert via List- Slicing aus.
#    	     Wer sich zutraut, benutzt dazu einen Loop.

print("\nAufgabe 3\n")

monatsumsatz = [100,200,300,400,500,600,700,800,900,1000,1100,1200]

Q1 = sum(monatsumsatz[0:3])
Q2 = sum(monatsumsatz[3:6])
Q3 = sum(monatsumsatz[6:9])
Q4 = sum(monatsumsatz[9:])

# print(f"Quartalsumsätze {Q1}, {Q2}, {Q3}, {Q4}")
 
s=0
e=3
for q in range(s,e+1):
    # print(s,e)
    print(f"Q{q+1}:",sum(monatsumsatz[s:e]))
    s+=3
    e+=3
    # if s>len(monatsumsatz)-1:
    #     break

# Aufgabe 4: Slice die Zeichenfolge der Variable 'shuffled'
#    	     so, dass sie lautet: hey ho let's go!

print("\nAufgabe 4\n")

shuffled = "hgeoy!s'tel"
print(shuffled[0:5:2], shuffled[0:4:3], shuffled[len(shuffled)-1:len(shuffled)-6:-1], shuffled[1:6:2])
print(shuffled[0:5:2], shuffled[0:4:3], shuffled[-1:-6:-1], shuffled[1:6:2])

# Aufgabe 5:

liste1 = [1,2,3,5,60,7,5,12,50,4,5,6]

# Aufgabe 5a: Slice die Liste1 in einem Loop durch Verschieben
#             des Start- Parameters so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<100)             <
#  |x ->| | | | | | | | | | |stop|

print("\nAufgabe 5a\n")

for x in range(len(liste1)):
    # 1. Iteration: [0:]
    # 2. Iteration: [1:] usw.
    if sum(liste1[x:])<100:
        print(liste1[x:])
        break

# Aufgabe 5b: Slice die Liste1 in einem Loop durch Verschieben
#             des Stop- Parameters so, dass die Summe der restlichen
#             Liste den Wert 100 gerade unterschritten hat. 
#             Der Loop soll dann abgebrochen und die gekürzte 
#             Liste ausgegeben werden.

# >            (<100)            <
#  |start| | | | | | | | | | |<-x|

print("\nAufgabe 5b\n")

for x in reversed(range(len(liste1))):
    # 1. Iteration: [:12]
    # 2. Iteration: [:11] usw.
    if sum(liste1[:x])<100:
        print(liste1[:x])
        break

# Aufgabe 5c: Slice die Liste1 in einem Loop durch Verschieben
#             der Start- und Stop- Parameter so, dass die Summe der restlichen
#             Liste kleiner 100 ist. Der Loop soll dann abgebrochen und die 
#             gekürzte Liste ausgegeben werden.

# >            (<100)           <
#  |x->| | | | | | | | | | |<-x|

print("\nAufgabe 5c\n")

for x in range(len(liste1)):
    # 1. Iteration: [0:12-0]
    # 2. Iteration: [1:12-1] usw.
    if sum(liste1[x:len(liste1)-x])<100:
        print(liste1[x:len(liste1)-x])
        break
