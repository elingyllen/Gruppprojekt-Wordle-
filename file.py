import tkinter as tk 
import random

Words = ["apple", "grape", "mango", "peach"]

Target_word = random.choice(Words)

Rows = 6
Cols = 5 

root =tk.Tk()
root.title("Wordle")

grid = []
def check_guess() :
    row = current_row[0]
    guess = ""

    for col in range(Cols) : 
        guess += grid[row][col].get().lower()

    if len(guess) != 5:
        return 
    
    for col in range(Cols) : 
        letter = guess[col]
        entry = grid[row][col]

        if letter == Target_word[col]:
            entry.config(bg="green", fg="white")
        elif letter in Target_word:
            entry.config(bg="gold", fg="black")
        else:
            entry.config(bg="gray", fg="white")

    current_row[0] += 1 

for r in range(Rows):
    row_entries = []
    for c in range(Cols):
        e = tk.Entry(root, width=4, font=("Helvetica", 24), justify="center")
        e.grid(row=r, column=c, padx=5, pady=5)
        row_entries.append(e)
    grid.append(row_entries)

current_row = [0]

submit_btn = tk.Button(root, text="Submit", command=check_guess)
submit_btn.grid(row=Rows, column=0, columnspan=Cols)

root.mainloop()
    


        