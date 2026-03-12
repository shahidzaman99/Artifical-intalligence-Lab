import tkinter as tk
from tkinter import messagebox

# Initial board
board = [
    ['_', '_', '_'],
    ['_', '_', '_'],
    ['_', '_', '_']
]

current_player = 'x'

# -------- Evaluation Function --------
def evaluate(board):

    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != '_':
            if board[row][0] == 'x':
                return 10
            else:
                return -10

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '_':
            if board[0][col] == 'x':
                return 10
            else:
                return -10

    # Check diagonal 1
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '_':
        if board[0][0] == 'x':
            return 10
        else:
            return -10

    # Check diagonal 2
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '_':
        if board[0][2] == 'x':
            return 10
        else:
            return -10

    return 0


# -------- Button Click --------
def click(row, col):

    global current_player

    if board[row][col] == '_':

        board[row][col] = current_player
        buttons[row][col]["text"] = current_player.upper()

        score = evaluate(board)

        if score == 10:
            messagebox.showinfo("Game Over", "Player X Wins")
            reset()

        elif score == -10:
            messagebox.showinfo("Game Over", "Player O Wins")
            reset()

        elif all(board[i][j] != '_' for i in range(3) for j in range(3)):
            messagebox.showinfo("Game Over", "Game Draw")
            reset()

        else:
            if current_player == 'x':
                current_player = 'o'
            else:
                current_player = 'x'


# -------- Reset Game --------
def reset():

    global board, current_player

    board = [
        ['_', '_', '_'],
        ['_', '_', '_'],
        ['_', '_', '_']
    ]

    current_player = 'x'

    for i in range(3):
        for j in range(3):
            buttons[i][j]["text"] = ""


# -------- GUI --------
root = tk.Tk()
root.title("Tic Tac Toe - AI Lab")

buttons = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):

        buttons[i][j] = tk.Button(
            root,
            text="",
            font=("Arial", 30),
            width=5,
            height=2,
            command=lambda r=i, c=j: click(r, c)
        )

        buttons[i][j].grid(row=i, column=j)


# Reset Button
reset_button = tk.Button(root, text="Reset Game", font=("Arial", 14), command=reset)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

root.mainloop()