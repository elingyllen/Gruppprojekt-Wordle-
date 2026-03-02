import tkinter as tk
from tkinter import messagebox
import random

# grupp för ord
WORDS = ["peach", "death"]
TARGET = random.choice(WORDS)

# konstanter (rader etc.)
ROWS = 6
COLS = 5

root = tk.Tk()
root.title("Wordle")
root.resizable(False, False)

grid = []
current_row = 0
game_over = False


# ----------- SPELLOGIKEN (BEHÖVER INTE ÄNDRAS TROR JAG...) --------------

def submit_guess(event=None):
    global current_row, game_over

    if game_over:
        return

    guess = "".join(grid[current_row][c].get().lower() for c in range(COLS))

    if len(guess) != 5:
        return

    # grejen som kollar om man har flera bokstäver i TARGET och hanterar färgerna korrekt
    remaining = {}
    for ch in TARGET:
        remaining[ch] = remaining.get(ch, 0) + 1

    colors = ["gray"] * COLS

    # första passet (gröna) kollar om bokstaven är på rätt plats och minskar kvarvarande bokstäver
    for c in range(COLS):
        if guess[c] == TARGET[c]:
            colors[c] = "green"
            remaining[guess[c]] -= 1

    # andra passet (gula) kollar om bokstaven finns kvar i TARGET och inte redan har använts av en grön
    for c in range(COLS):
        if colors[c] == "green":
            continue
        if remaining.get(guess[c], 0) > 0:
            colors[c] = "gold"
            remaining[guess[c]] -= 1

    # lägger färgerna korrekt (JÄVLIGT VIKTIGT ATT DETTA KOMMER EFTER GRÖNA PASSEN)
    for c in range(COLS):
        entry = grid[current_row][c]
        entry.config(
            state="disabled",
            disabledbackground=colors[c],
            disabledforeground="white"
        )

    # WINNNER WINNER CHICKEN DINNER YALLA
    if guess == TARGET:
        game_over = True
        messagebox.showinfo("You Win!", f"You guessed the word: {TARGET.upper()}")
        return

    current_row += 1

    # om man fuckar upp alla rader
    if current_row == ROWS:
        game_over = True
        messagebox.showinfo("Game Over", f"The word was: {TARGET.upper()}")
        return

    # går automatiskt till nästa rad
    for c in range(COLS):
        grid[current_row][c].config(state="normal")
    grid[current_row][0].focus_set()


# ----------- INPUT (alltså knappar o skit) --------------

def handle_key(event, r, c):
    global current_row

    if game_over or r != current_row:
        return "break"

    # jävligt najs fix som gör att man kan trycka enter i vilken ruta som helst i raden och det kommer submit:a gissningen
    if event.keysym == "Return":
        submit_guess()
        return "break"

    # samma fast med backspace (går till förra lådan och tar bort)
    if event.keysym == "BackSpace":
        if grid[r][c].get() == "" and c > 0:
            grid[r][c-1].focus_set()
        return

    # ditto
    if event.char.isalpha():
        grid[r][c].delete(0, tk.END)
        grid[r][c].insert(0, event.char.lower())

        if c < COLS - 1:
            grid[r][c+1].focus_set()

        return "break"

    return "break"


# ----------- GRID (alltså lådorna) --------------

for r in range(ROWS):
    row_entries = []
    for c in range(COLS):
        e = tk.Entry(
            root,
            width=4,
            font=("Helvetica", 28, "bold"),
            justify="center",
            relief="solid",
            bd=2
        )
        e.grid(row=r, column=c, padx=5, pady=5)
        e.bind("<Key>", lambda event, r=r, c=c: handle_key(event, r, c))
        row_entries.append(e)
    grid.append(row_entries)

# inaktiverar alla rader utom den första
for r in range(ROWS):
    for c in range(COLS):
        state = "normal" if r == 0 else "disabled"
        grid[r][c].config(state=state)

grid[0][0].focus_set()

root.bind("<Return>", submit_guess)

root.mainloop()