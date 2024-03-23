from tkinter import Tk, Button, Label, PhotoImage
import random
import tkinter as tk
import os
from tkinter import messagebox

colour_win = 'lightgreen'
normal_colour = 'white'

def restart():
    global player
    player = random.choice(mark)
    label.config(text=player + ' turn')
    for row in range(board_size):
        for column in range(board_size):
            buttons[row][column].config(image=blank_image, text="")
            buttons[row][column].config(command=lambda r=row, c=column: next_turn(r, c))

def next_turn(row, column):
    global player
    if buttons[row][column]['text'] == "" and not check_winner():
        buttons[row][column].config(image=player_images[player], text=player, command=lambda: None)
        if check_winner():
            label.config(text=player + ' win')
            frame.config(bg=colour_win)
            messagebox.showinfo('Winner!')
            for widget in frame.winfo_children():
                widget.config(state=tk.DISABLED)
        else:
            player = mark[(mark.index(player) + 1) % len(mark)]
            label.config(text=player + ' turn')

def check_winner():
    # check row
    for row in range(board_size):
        for column in range(board_size - 4):
            if all(buttons[row][column + i]['text'] == buttons[row][column + i + 1]['text'] != '' for i in range(4)):
                return True
    # check column
    for column in range(board_size):
        for row in range(board_size - 4):
            if all(buttons[row + i][column]['text'] == buttons[row + 1 + i][column]['text'] != '' for i in range(4)):
                return True
    # check top-left to bottom-right
    for row in range(board_size - 4):
        for column in range(board_size - 4):
            if all(buttons[row + i][column + i]['text'] == buttons[row + 1 + i][column + 1 + i]['text'] != '' for i
                   in range(4)):
                return True
    # check top-right to bottom-left
    for row in range(board_size - 4):
        for column in range(board_size - 1, 3, -1):
            if all(buttons[row + i][column - i]['text'] == buttons[row + 1 + i][column - 1 - i]['text'] != '' for i
                   in range(4)):
                return True
    if all(buttons[row][column]['text'] != '' for row in range(board_size) for column in range(board_size)):
        label.config(text='Tie!')
        return True
    return False


root = Tk()
root.title('Tic Tac Toe')

mark = ['X', 'O']
player = random.choice(mark)

board_size = 14

buttons = [[None for _ in range(20)] for _ in range(20)]

label = Label(text=player + " turn", font=("futura", 20))
label.pack(side='top')

restart_button = Button(text='Restart', font=('futura', 12), command=restart)
restart_button.pack(side='top')

frame = tk.Frame(root, bg=normal_colour)
frame.pack()

# load ảnh
player_images = {
    'X': PhotoImage(file=os.path.join(os.getcwd(), 'Assets', 'X.png')),
    'O': PhotoImage(file=os.path.join(os.getcwd(), 'Assets', 'O.png')),
    '': None  # kh hình
}

# hình ảnh trống để xóa
blank_image = PhotoImage()

# drawing board
for row in range(board_size):
    for column in range(board_size):
        buttons[row][column] = Button(frame, image=blank_image, text="", width=50, height=50,
                                       command=lambda r=row, c=column: next_turn(r, c))
        buttons[row][column].grid(row=row, column=column)

root.mainloop()
