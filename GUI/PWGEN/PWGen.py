def pwgenPro(lows:int, caps:int, nums:int, specs:int=0, ausschluss:str="")->str:
    """
    @param lowLetters: Anzahl der Kleinbuchstaben
    @param capLetters: Anzahl der Großbuchstaben
    @param numbers: Anzahl der Zahlen
    @param specChar: Anzahl der Sonderzeichen
    @param ausschluss: (optional) Zeichen, die nicht enthalten sein sollen
    @return: Zufällige Zeichenkette
    """
    from random import sample, shuffle
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    lowLetters=sample(list(set(ascii_lowercase)-set(ausschluss)), lows)
    capLetters=sample(list(set(ascii_uppercase)-set(ausschluss)), caps)
    numbers=sample(list(set(digits)-set(ausschluss)), nums)
    specChar=sample(list(set(punctuation)-set(ausschluss)), specs)
    pw=[]
    pw.extend(lowLetters+capLetters+numbers+specChar)
    shuffle(pw)
    return "".join(pw)

# Variante Sven: event=None

def generate(event=None):
    lbl_PW.configure(text = pwgenPro(int(in_AnzahlKlein.get()), int(in_AnzahlGross.get()), int(in_AnzahlZahlen.get()), int(in_AnzahlSonder.get()), in_Ausschluss.get()))

def copyClipboard(event=None):
    lbl_PW.clipboard_clear()
    lbl_PW.clipboard_append(lbl_PW.cget('text'))

import tkinter as tk

root = tk.Tk()

root.title("Passwortgenerator")
root.geometry("400x400")
root.resizable(False,False)

# Create Widgets

lbl_AnzahlKlein = tk.Label(master = root, text = "Anzahl Kleinbuchstaben", font=("Arial Black",10),bg='RED')
in_AnzahlKlein = tk.Entry(master=root)
lbl_AnzahlGross = tk.Label(master = root, text = "Anzahl Großbuchstaben", font=("Arial Black",10),bg='RED')
in_AnzahlGross = tk.Entry(master=root)
lbl_AnzahlZahlen = tk.Label(master = root, text = "Anzahl Zahlen", font=("Arial Black",10),bg='RED')
in_AnzahlZahlen = tk.Entry(master=root)
lbl_AnzahlSonder = tk.Label(master = root, text = "Anzahl Sonderzeichen", font=("Arial Black",10),bg='RED')
in_AnzahlSonder = tk.Entry(master=root)

lbl_Ausschluss = tk.Label(master = root, text = "Ausschlusszeichen", font=("Arial Black",10),bg='RED')
in_Ausschluss = tk.Entry(master = root)
btn_Gen = tk.Button(master = root, text = "Generiere", font=("Arial Black",10), command=generate)
lbl_PW = tk.Label(master = root, text = "Passwort", font=("Arial Black",10),bg='RED')
btn_Copy = tk.Button(master = root, text = "Kopiere", font=("Arial Black",10), command=copyClipboard)

# Layout Widgets
# pack()- Manager

# lbl_AnzahlZeichen.pack(pady=10)
# in_AnzahlZeichen.pack()
# lbl_Ausschluss.pack(pady=10)
# in_Ausschluss.pack()
# btn_Gen.pack(pady=10)
# lbl_PW.pack()
# btn_Copy.pack(pady=10)

# grid()- Manager

# lbl_AnzahlZeichen.grid(row=0, column=0, padx=10, pady=10)
# in_AnzahlZeichen.grid(row=0, column=1, padx=10, pady=10)
# lbl_Ausschluss.grid(row=1, column=0, padx=10, pady=10)
# in_Ausschluss.grid(row=1, column=1, padx=10, pady=10)
# btn_Gen.grid(row=2, column=0, padx=10, pady=10)
# btn_Copy.grid(row=2, column=1, padx=10, pady=10)
# lbl_PW.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# place()- Manager

lbl_AnzahlKlein.place(x=30, y=30)
in_AnzahlKlein.place(x=220, y=30, width=150)
lbl_AnzahlGross.place(x=30, y=80)
in_AnzahlGross.place(x=220, y=80, width=150)
lbl_AnzahlZahlen.place(x=30, y=130)
in_AnzahlZahlen.place(x=220, y=130, width=150)
lbl_AnzahlSonder.place(x=30, y=180)
in_AnzahlSonder.place(x=220, y=180, width=150)
lbl_Ausschluss.place(x=30, y=230)
in_Ausschluss.place(x=220, y=230, width=150)
btn_Gen.place(x=30, y=280)
btn_Copy.place(x=200, y=280)
lbl_PW.place(relx=0.1, y=330, relwidth=0.8)

root.bind('<Return>', generate)
root.bind('<Alt-Return>', copyClipboard)

root.mainloop()