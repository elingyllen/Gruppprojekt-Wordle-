# importera tkinter som GUI
import tkinter as tk 
import random

# Skapa lista med ordval + randomisera vilket ord som blir valt
Words = ["APPLE", "GRAPE", "MANGO", "PEACH"]
Target_word = random.choice(Words)

# Skapa rutnät där man gissar orden
Rows = 6
Cols = 5 

root = tk.Tk()
root.title("Wordle")

grid = []
current_row = [0]

def check_guess():
    global Target_word
    
    row = current_row[0]
    guess = ""

    if row >= Rows:
        return

    # Göra gissningen
    for col in range(Cols): 
        guess += grid[row][col].get().upper()

    if len(guess) != 5:
        return 
    
    # Kolla bokstäver
    for col in range(Cols): 
        letter = guess[col]
        entry = grid[row][col]

        if letter == Target_word[col]:
            entry.config(bg="green", fg="white")
        elif letter in Target_word:
            entry.config(bg="gold", fg="black")
        else:
            entry.config(bg="gray", fg="white")

    # Om man gissar rätt → aktivera Next-knappen
    if guess == Target_word:
        next_btn.config(state="normal")

    current_row[0] += 1 

    # Om man använt alla försök → aktivera också Next-knappen
    if current_row[0] == Rows:
        next_btn.config(state="normal")


def next_word():
    global Target_word
    
    Target_word = random.choice(Words)
    current_row[0] = 0

    # Rensa alla rutor
    for r in range(Rows):
        for c in range(Cols):
            grid[r][c].delete(0, tk.END)
            grid[r][c].config(bg="white", fg="black")

    # Stäng av knappen igen
    next_btn.config(state="disabled")


# Skapa rutnät
for r in range(Rows):
    row_entries = []
    for c in range(Cols):
        entry = tk.Entry(root, width=4, font=("Helvetica", 24), justify="center")
        entry.grid(row=r, column=c, padx=5, pady=5)
        row_entries.append(entry)
    grid.append(row_entries)


submit_btn = tk.Button(root, text="Submit", command=check_guess)
submit_btn.grid(row=Rows, column=0, columnspan=Cols)

# Next Word-knapp (börjar avstängd)
next_btn = tk.Button(root, text="Next Word", command=next_word, state="disabled")
next_btn.grid(row=Rows+1, column=0, columnspan=Cols)

root.mainloop()
