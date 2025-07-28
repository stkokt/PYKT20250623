def pwgenSimple(pwLength:int, ausschluss:str="")->str:
    """
    @param pwLength: Integerzahl für die Anzahl der auszugebenen Zeichen
    @param ausschluss: (optional) Zeichen, die nicht enthalten sein sollen
    @return: Zufällige Zeichenkette
    """
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    from random import sample 
    pwPool=list(set(ascii_lowercase + ascii_uppercase + digits + punctuation) - set(ausschluss))
    # print(sorted(pwPool))     # nur einkommentieren, um den Zeichenpool zu sehen
    return "".join(sample(pwPool, pwLength))    # Sampleliste wird in einen leeren String gejoint

def generate():
    lbl_PW.configure(text = pwgenSimple(int(in_AnzahlZeichen.get()), in_Ausschluss.get()))

def copyClipboard():
    lbl_PW.clipboard_clear()
    lbl_PW.clipboard_append(lbl_PW.cget('text'))

import tkinter as tk

root = tk.Tk()

root.title("Passwortgenerator")
root.geometry("400x400")
root.resizable(False,False)

# Create Widgets

lbl_AnzahlZeichen = tk.Label(master = root, text = "Anzahl Zeichen", font=("Arial Black",10),bg='RED')
in_AnzahlZeichen = tk.Entry(master=root)
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

lbl_AnzahlZeichen.place(x=30, y=30)
in_AnzahlZeichen.place(x=200, y=30, width=150)
lbl_Ausschluss.place(x=30, y=80)
in_Ausschluss.place(x=200, y=80, width=150)
btn_Gen.place(x=30, y=130)
btn_Copy.place(x=200, y=130)
lbl_PW.place(relx=0.1, y=200, relwidth=0.8)

root.bind('<Return>', lambda event: generate())
root.bind('<Alt-Return>', lambda event: copyClipboard())

root.mainloop()