import tkinter as tk

player = True

def check():
    global segments
    # Erste Spalte
    if segments[0][0]['text'] + segments[0][1]['text'] + segments[0][2]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][0]['text'] + segments[0][1]['text'] + segments[0][2]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Zweite Spalte
    if segments[1][0]['text'] + segments[1][1]['text'] + segments[1][2]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[1][0]['text'] + segments[1][1]['text'] + segments[1][2]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Dritte Spalte
    if segments[2][0]['text'] + segments[2][1]['text'] + segments[2][2]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[2][0]['text'] + segments[2][1]['text'] + segments[2][2]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Erste Reihe
    if segments[0][0]['text'] + segments[1][0]['text'] + segments[2][0]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][0]['text'] + segments[1][0]['text'] + segments[2][0]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Zweite Reihe
    if segments[0][1]['text'] + segments[1][1]['text'] + segments[2][1]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][1]['text'] + segments[1][1]['text'] + segments[2][1]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Dritte Reihe
    if segments[0][2]['text'] + segments[1][2]['text'] + segments[2][2]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][2]['text'] + segments[1][2]['text'] + segments[1][2]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Erste Diagonale
    if segments[0][0]['text'] + segments[1][1]['text'] + segments[2][2]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][0]['text'] + segments[1][1]['text'] + segments[2][2]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
    # Zweite Diagonale
    if segments[0][2]['text'] + segments[1][1]['text'] + segments[2][0]['text']=="XXX":
        #print("player1 hat gewonnen")
        result.configure(text="Spieler 1 hat gewonnen")
        return True
    if segments[0][2]['text'] + segments[1][1]['text'] + segments[2][0]['text']=="OOO":
        #print("player2 hat gewonnen")
        result.configure(text="Spieler 2 hat gewonnen")
        return True
def on_button_click(event):
    global player
    global segments
    button = event.widget
    if player and button['text']==" " and button['state'] != 'disabled':
        button['text'] = "X"
        button.configure(bg="Blue")
        player = False
        result.configure(text="Spieler 2 ist an der Reihe")
    elif not player and button['text']==" " and button['state'] != 'disabled':
        button['text'] = "O"
        button.configure(bg="Red")
        player = True
        result.configure(text="Spieler 1 ist an der Reihe")
    if check():
        for row in segments:
            for column in row:
                column.configure(state='disabled')
    #print(f"Button-Name: {button.winfo_name()}")

def reset():
    global player
    global segments
    for row in segments:
            for column in row:
                column.configure(state='normal')
                column.configure(bg='White')
                column.configure(text=' ')
    player = True
    result.configure(text="Spieler 1 beginnt")

root = tk.Tk()

root.geometry("340x400")
root.title("Tic Tac Toe")
root.resizable(False,False)

gameframe = tk.Frame(root,bg="Black", border=1)
gameframe.place(x=18,y=48, width=302, height=302)
segments = [[tk.Button(gameframe, text=" ", name= str(ydim)+str(xdim), font=("Arial", 20, "bold"),bg="white") for xdim in range(3)] for ydim in range(3)]
newGame = tk.Button(root, text="Neues Spiel", command=reset)
newGame.place(x=135,y=10)
result = tk.Label(root,text="Spieler 1 beginnt", font=("Arial",10,"bold"))
result.place(relx= 0.1, y=370, relwidth=0.8)

for xdim in range(3):
    for ydim in range(3):
        segments[xdim][ydim].place(x=xdim*100+1, y=ydim*100+1, width=100,height=100)
        segments[xdim][ydim].bind("<Button-1>", on_button_click)



root.mainloop()