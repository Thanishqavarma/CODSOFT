from tkinter import *
from tkinter import messagebox
import random

window = Tk()

window.title("Tic Tac Toe AI")
window.geometry("420x500")
window.config(bg="#f4f4f4")


board = ["", "", "", "", "", "", "", "", ""]


buttons = []


player = "X"
ai = "O"



title = Label(
    window,
    text="Tic Tac Toe AI",
    font=("Arial", 24, "bold"),
    bg="#f4f4f4"
)

title.pack(pady=20)





frame = Frame(window, bg="#f4f4f4")
frame.pack()





def check_winner(symbol):

    win_positions = [

        [0,1,2],
        [3,4,5],
        [6,7,8],

        [0,3,6],
        [1,4,7],
        [2,5,8],

        [0,4,8],
        [2,4,6]

    ]


    for combo in win_positions:

        if board[combo[0]] == symbol and board[combo[1]] == symbol and board[combo[2]] == symbol:
            return True

    return False





def ai_move():

    empty = []

    for i in range(9):

        if board[i] == "":
            empty.append(i)


    if len(empty) > 0:

        move = random.choice(empty)

        board[move] = ai

        buttons[move]["text"] = ai
        buttons[move]["fg"] = "red"


        if check_winner(ai):

            messagebox.showinfo("Game Over", "AI Wins!")
            reset_game()

        elif "" not in board:

            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()





def player_move(index):

    if board[index] == "":

        board[index] = player

        buttons[index]["text"] = player
        buttons[index]["fg"] = "blue"


        if check_winner(player):

            messagebox.showinfo("Game Over", "You Win!")
            reset_game()

        elif "" not in board:

            messagebox.showinfo("Game Over", "It's a Draw!")
            reset_game()

        else:

            ai_move()





def reset_game():

    global board

    board = ["", "", "", "", "", "", "", "", ""]


    for button in buttons:

        button["text"] = ""





for i in range(9):

    button = Button(

        frame,

        text="",
        width=8,
        height=4,

        font=("Arial", 22, "bold"),

        command=lambda i=i: player_move(i)

    )

    button.grid(row=i//3, column=i%3, padx=5, pady=5)

    buttons.append(button)





reset_btn = Button(

    window,

    text="Restart Game",

    font=("Arial", 14),

    bg="#007bff",
    fg="white",

    padx=20,
    pady=10,

    command=reset_game

)

reset_btn.pack(pady=25)





window.mainloop()
