import tkinter as tk
from tkinter import Button, Label, PhotoImage, messagebox
import random
import os

class TicTacToe(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tic Tac Toe')
        self.colour_win = 'lightgreen'
        self.normal_colour = 'white'
        self.mark = ['X', 'O']
        self.board_size = 14
        self.player_images = {
            'X': PhotoImage(file=os.path.join(os.getcwd(), 'Assets', 'X.png')),
            'O': PhotoImage(file=os.path.join(os.getcwd(), 'Assets', 'O.png')),
            '': None
        }
        self.blank_image = PhotoImage()
        self.player = random.choice(self.mark)

        self.label = Label(self, text=self.player + " turn", font=("futura", 20))
        self.label.pack(side='top')

        self.restart_button = Button(self, text='Restart', font=('futura', 12), command=self.restart)
        self.restart_button.pack(side='top')

        self.frame = tk.Frame(self, bg=self.normal_colour)
        self.frame.pack()

        self.buttons = []
        self.create_board()

    def create_board(self):
        for row in range(self.board_size):
            button_row = []
            for column in range(self.board_size):
                button = Button(self.frame, image=self.blank_image, text="", width=50, height=50,
                                command=lambda r=row, c=column: self.next_turn(r, c))
                button.grid(row=row, column=column)
                button_row.append(button)
            self.buttons.append(button_row)

    def restart(self):
        self.player = random.choice(self.mark)
        self.label.config(text=self.player + ' turn')
        self.frame.config(bg=self.normal_colour)
        for row in range(self.board_size):
            for column in range(self.board_size):
                self.buttons[row][column].config(image=self.blank_image, text="", command=lambda r=row, c=column: self.next_turn(r, c), state=tk.NORMAL)


    def next_turn(self, row, column):
        button = self.buttons[row][column]
        if button['text'] == "" and not self.check_winner():
            button.config(image=self.player_images[self.player], text=self.player)
            if self.check_winner():
                self.label.config(text=self.player + ' win')
                self.frame.config(bg=self.colour_win)
                messagebox.showinfo('Winner!', f"{self.player} wins!")
                for widget in self.frame.winfo_children():
                    widget.config(state=tk.DISABLED)
            else:
                self.player = self.mark[(self.mark.index(self.player) + 1) % len(self.mark)]
                self.label.config(text=self.player + ' turn')

    def check_winner(self):
        for row in range(self.board_size):
            for column in range(self.board_size - 4):
                if all(self.buttons[row][column + i]['text'] == self.buttons[row][column + i + 1]['text'] != '' for i in range(4)):
                    return True

        for column in range(self.board_size):
            for row in range(self.board_size - 4):
                if all(self.buttons[row + i][column]['text'] == self.buttons[row + 1 + i][column]['text'] != '' for i in range(4)):
                    return True

        for row in range(self.board_size - 4):
            for column in range(self.board_size - 4):
                if all(self.buttons[row + i][column + i]['text'] == self.buttons[row + 1 + i][column + 1 + i]['text'] != '' for i in range(4)):
                    return True

        for row in range(self.board_size - 4):
            for column in range(self.board_size - 1, 3, -1):
                if all(self.buttons[row + i][column - i]['text'] == self.buttons[row + 1 + i][column - 1 - i]['text'] != '' for i in range(4)):
                    return True

        if all(self.buttons[row][column]['text'] != '' for row in range(self.board_size) for column in range(self.board_size)):
            self.label.config(text='Tie!')
            return True

        return False

if __name__ == "__main__":
    app = TicTacToe()
    app.mainloop()
