# PASS
def any_function():
    pass

# VERSCHACHTELTE FUNKTIONEN
def outerFunc(name):
    def innerFunc():
        return name
    print("Hallo", innerFunc())

outerFunc("Stefan")

# NAMENSRÄUME (SCOPES) (GÜLTIGKEITSBEREICHE)

x = 5

def scope():
    x = 10
    def glob():
        global x
        x += 1
        print("Aus glob(): ", x)
    glob()
    def nonloc():
        nonlocal x
        x += 1
        print("Aus nonloc(): ", x)
    nonloc()
    def loc():
        x = 15
        x += 1
        print("Aus loc(): ", x)
    #glob()
    #nonloc()
    loc()

#scope()

def eineFunktion():
    print(x) # lesender Zugriff auf globale Variable möglich, aber nicht zu empfehlen

eineFunktion()

def eineAndereFunktion():
    y = x   # x lässt sich zuweisen, weil lesender Zugriff besteht
    y *= 2
    print(y)

eineAndereFunktion()

# UNBENANNTE UND BENANNTE PARAMETER
# unbenannte Parameter = positional arguments

def house_planner(front_doors, windows, rooms, has_basement):
    print("Das zu bauende Haus hat:")
    print(str(front_doors) + " Haustüre(n).")
    print(f"{windows} Fenster")
    print("{} Räume".format(rooms, {}))
    #print("{} {} Räume".format(rooms, {})) # zeigt ein leeres Klammerpaar in der Ausgabe
    print("{} {raum} Räum(e)".format(10, raum=5))
    print(" und einen Keller" if has_basement else " und keinen Keller") # Ternären Operator

# normale (unbeannte/positionsabhänige) Parameter
#house_planner(2,10,5,True)
# house_planner(2,10,5,0)

# benannte Parameter
#house_planner(front_doors=1,windows=7, rooms=5, has_basement=True)
#house_planner(has_basement=True, windows=10,front_doors=2,rooms=5)

#house_planner(1,7,has_basement=True, rooms=5)
# house_planner(has_basement=True,1,7,5) # SyntaxError: positional argument follows keyword argument

customer_wishlist = [3,10,8,True]
#house_planner(*customer_wishlist)

customer_wishdict = {"rooms":3, "front_doors":1, "has_basement":True, "windows":7}

#house_planner(front_doors=customer_wishdict["front_doors"], windows=customer_wishdict["windows"], rooms=customer_wishdict['rooms'],has_basement=customer_wishdict['has_basement'])
house_planner(**customer_wishdict)

# ARGS UND KWARGS
# def multiply(n1, n2):
#     return n1 * n2

# def multiply(n1, n2, n3):
#     return n1 * n2 * n3

#multiply(5,6) # Aufruf mit 2 Argumenten nicht mehr möglich!

def multiply(*nums):
    if not nums:        
        return None  # or return 1, depending on the desired behavior for an empty input    
    a = 1    
    for _ in range(len(nums)):        
        a *= nums[_]    
    return a

#print(multiply())

print(multiply(10,2,3,4))

def quark(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for k,v in kwargs.items():
        print(f"{k} : {v}")

quark(kw1 = "Hallo", kw2 = "Stefan")


def varArgsKwargs(var, *args, **kwargs):
    '''
    Es muss nicht *args und **kwargs heißen, 
    wichtig sind die Sternchen.
    *args wird als Tupel interpretiert,
    **kwargs als Dictionary.
    '''
    print(f"Das ist die Variable: {var}.")
    print(f"Das ist das Args- Tupel: {args}")
    print(f"Das ist das Kwargs- Dictionary: {kwargs}")
    for value in kwargs.values():
        print(args[0] * value)

varArgsKwargs("Var", 5,"m",3.14, kwargs1 = "Hallo", kwargs2 = "Welt")

# LAMBDA
# kurze Funktion
def multi(a,b):
    return a*b

print(multi(10,5))

# kürzer
multi1 = lambda a,b: a*b

print(multi1(10,5))

# noch kürzer
print((lambda a,b: a*b)(10,5))


# FILTER UND MAP

liste = [1,2,3,4,5]

print(list(filter(lambda x: x>2,liste)))
print([x for x in liste if x > 2])

print(list(map(lambda x: x*2, liste)))
print([x*2 for x in liste])