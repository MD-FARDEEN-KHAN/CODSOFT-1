import tkinter as tk
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.board = [" "]*9
        self.current_player = "X"
        self.game_over = False
        self.create_board()
        self.draw_board()

    def create_board(self):
        self.buttons = []
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.master, text=" ", font=('Arial', 20), width=6, height=3,
                                command=lambda row=i, col=j: self.on_click(row, col))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(btn)

    def draw_board(self):
        for i in range(9):
            self.buttons[i].config(text=self.board[i])

    def on_click(self, row, col):
        if not self.game_over and self.board[row*3 + col] == " ":
            self.board[row*3 + col] = self.current_player
            self.draw_board()
            if self.check_winner():
                self.game_over = True
                self.show_winner()
            elif " " not in self.board:
                self.game_over = True
                self.show_draw()
            else:
                self.switch_player()
                self.ai_move()

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def ai_move(self):
        if not self.game_over:
            while True:
                move = random.randint(0, 8)
                if self.board[move] == " ":
                    self.board[move] = self.current_player
                    self.draw_board()
                    if self.check_winner():
                        self.game_over = True
                        self.show_winner()
                    elif " " not in self.board:
                        self.game_over = True
                        self.show_draw()
                    self.switch_player()
                    break

    def check_winner(self):
        lines = [[0, 1, 2], [3, 4, 5], [6, 7, 8],
                 [0, 3, 6], [1, 4, 7], [2, 5, 8],
                 [0, 4, 8], [2, 4, 6]]

        for line in lines:
            if self.board[line[0]] == self.board[line[1]] == self.board[line[2]] != " ":
                return True
        return False

    def show_winner(self):
        winner = self.current_player
        if winner == "X":
            winner = "Human"
        else:
            winner = "AI"
        label = tk.Label(self.master, text=f"{winner} wins!", font=('Arial', 20))
        label.grid(row=3, columnspan=3)

    def show_draw(self):
        label = tk.Label(self.master, text="It's a draw!", font=('Arial', 20))
        label.grid(row=3, columnspan=3)

def main():
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()

if __name__ == "__main__":
    main()