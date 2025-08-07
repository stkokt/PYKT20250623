# REKURSION = die Funktion ruft sich bis zur Abbruchbedingung selbst auf.

# Einfache Ausgabefunktion
def sayHello_rekursiv(n):
    print("Hello")
    if n > 1:
       sayHello_rekursiv(n - 1)

sayHello_rekursiv(5)

print()

def sayHello_iterativ(n):
    for x in range(n):
        print("Hello")

sayHello_iterativ(5)

# Summe über Liste

def summe_rekursiv(liste:list): # [1,2,3,4,5]
    if len(liste) < 1:
        return 0
    else:
        return liste[0] + summe_rekursiv(liste[1:])
    # 1. Inkarantion: 1 + summe_rekursion([2,3,4,5])
    # 2. Inkarnation: 2 + summe_rekursion([3,4,5])
    # 3. Inkarnation: 3 + summe_rekursion([4,5])
    # 4. Inkarnation: 4 + summe_rekursion([5])
    # 5. Inkarnation: 5 + 0

print(summe_rekursiv([1,2,3,4,5]))

def summe_iterativ(liste:list):
    result = 0
    for x in liste:
        result += x
    return result

print(summe_iterativ([1,2,3,4,5]))

# Fakultät:  5! = 5*4*3*2*1 = 120

def fakultaet_rekursiv(n):
    print("Fakultät aufgerufen")
    if n == 0 or n == 1:
        return 1
    else:
        return n*fakultaet_rekursiv(n-1)

print(fakultaet_rekursiv(5))

def fakultaet_iterativ(n): # n=5
    result = 1
    for i in range(1, n + 1):   # range(1,6)
        result *= i
    return result

print(fakultaet_iterativ(5))

# Fibonacci Zahlen 1 1 2 3 5 8 13 21 34 55 usw.
def fibonacci_rekursiv(n):
    #print("fib aufgerufen")
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci_rekursiv(n-1) + fibonacci_rekursiv(n-2)
    
print(fibonacci_rekursiv(10))

def fibonacci_iterativ(n):
    if n == 0 or n == 1:
        return n
    a, b = 0,1 
    for _ in range(2, n+1):
        a, b = b, a + b 
    return b

print(fibonacci_iterativ(10))
            
# Potenz berechnen

def potenz_rekursiv(basis, exponent):
    #print("potenz")
    if exponent == 0:
        return 1
    else: return basis * potenz_rekursiv(basis, exponent - 1)

print(potenz_rekursiv(2,3))

def potenz_iterativ(basis, exponent):
    ergebnis = 1
    for _ in range(exponent):
        ergebnis *= basis
    return ergebnis

print(potenz_iterativ(2,3))