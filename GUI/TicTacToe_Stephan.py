import tkinter as tk
from tkinter import messagebox
import random
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.current_player = "X"  # Spieler ist X
        self.vs_npc = True
        self.status_label = tk.Label(self.root, text=f"Spieler {self.current_player} ist dran", font=("Arial", 20))
        self.status_label.grid(row=3, column=0, columnspan=3)
        self.buttons = [None] * 9
        self.create_board()
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text=" ", font=("Arial", 40), width=5, height=2,
                               command=lambda i=i: self.click(i))
            button.grid(row=i // 3, column=i % 3)
            self.buttons[i] = button
    def click(self, index):
        if self.buttons[index]["text"] == " " and self.current_player == "X":
            self.make_move(index, "X")
            if self.check_game_over("X"):
                return
            self.current_player = "O"
            self.status_label.config(text="Computer denkt ...")
            self.root.after(500, self.npc_move)  # NPC-Zug mit Verzögerung
    def npc_move(self):
        empty_indices = [i for i, btn in enumerate(self.buttons) if btn["text"] == " "]
        # 1. Versuche zu gewinnen
        for index in empty_indices:
            self.buttons[index]["text"] = "O"
            if self.check_winner("O"):
                self.make_move(index, "O")
                if self.check_game_over("O"):
                    return
                self.current_player = "X"
                self.status_label.config(text=f"Spieler {self.current_player} ist dran")
                return
            self.buttons[index]["text"] = " "
        # 2. Verhindere Sieg des Spielers
        for index in empty_indices:
            self.buttons[index]["text"] = "X"
            if self.check_winner("X"):
                self.buttons[index]["text"] = " "
                self.make_move(index, "O")
                if self.check_game_over("O"):
                    return
                self.current_player = "X"
                self.status_label.config(text=f"Spieler {self.current_player} ist dran")
                return
            self.buttons[index]["text"] = " "
        # 3. Sonst zufällig
        if empty_indices:
            index = random.choice(empty_indices)
            self.make_move(index, "O")
            if self.check_game_over("O"):
                return
            self.current_player = "X"
            self.status_label.config(text=f"Spieler {self.current_player} ist dran")
    def npc_move(self):
        empty_indices = [i for i, btn in enumerate(self.buttons) if btn["text"] == " "]
        if empty_indices:
            index = random.choice(empty_indices)
            self.make_move(index, "O")
            if self.check_game_over("O"):
                return
            self.current_player = "X"
            self.status_label.config(text=f"Spieler {self.current_player} ist dran")
    def make_move(self, index, player):
        self.buttons[index]["text"] = player
        self.buttons[index].update()
    def check_game_over(self, player):
        if self.check_winner(player):
            messagebox.showinfo("Spiel beendet", f"{'Computer' if player == 'O' else 'Spieler'} ({player}) gewinnt!")
            self.reset()
            return True
        elif all(btn["text"] != " " for btn in self.buttons):
            messagebox.showinfo("Spiel beendet", "Unentschieden!")
            self.reset()
            return True
        return False
    def check_winner(self, player):
        wins = [
            [0,1,2], [3,4,5], [6,7,8],
            [0,3,6], [1,4,7], [2,5,8],
            [0,4,8], [2,4,6]
        ]
        return any(all(self.buttons[i]["text"] == player for i in combo) for combo in wins)
    def reset(self):
        for btn in self.buttons:
            btn["text"] = " "
        self.current_player = "X"
        self.status_label.config(text=f"Spieler {self.current_player} ist dran")
root = tk.Tk()
game = TicTacToe(root)
root.mainloop()