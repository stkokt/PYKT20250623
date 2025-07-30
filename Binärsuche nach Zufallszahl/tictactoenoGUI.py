playfield = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

# spielfeld[zeile][spalte]
def show(p):
    for zeile in p:
        for spalte in zeile:
            print(spalte, end=" ")
        print()

def user_eingabe(p, zeile, spalte, user_id):
    if user_id == 1:
        p[zeile][spalte] = "X"
    elif user_id == 2:
        p[zeile][spalte] = "O"

# Spiel beginnt
for spieler_id in (1, 2, 1, 2, 1, 2):
    print(f"\n--- Spieler {spieler_id} ist am Zug ---")
    
    zeile = int(input("Bitte gib deine gewünschte Zeile ein (0-2): "))
    spalte = int(input("Bitte gib deine gewünschte Spalte ein (0-2): "))

    user_eingabe(playfield, zeile, spalte, spieler_id)
    
    print("\nAktuelles Spielfeld:")
    show(playfield)