import tkinter as tk
import random
# Function to start/restart the game
def start_game():
    global secret_number, attempts
    secret_number = random.randint(1,100)
    attempts = 0
    result_label.config(text="Game started! Make your Guess.", fg="Black")
    entry.delete(0,tk.END)

# function to check guess
def check_guess():
    global attempts
    try:
        guess = int(entry.get())
        attempts += 1
        if guess < secret_number:
            result_label.conf(text=f"Too low Attempts: {attempts}", fg="blue")
        elif guess > secret_number:
            result_label.conf(text=f"Too high Attempts: {attempts}", fg="orange")
        else:
            result_label.conf(text=f" Correct! The number was {secret_number} in {attempts} tries", fg="green")
    except ValueError:
        result_label.config(text="Please enter a valid number.", fg="red")

    entry.delete(0, tk.END)

# Main Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x250")

# Title
title_label = tk.Label(root, text="Guess a number between 1 and 100", font=("Arial",14,"bold"))
title_label.pack(pady=5)

# Entry 
entry = tk.Entry(root, font=("Arial", 12))
entry.pack(pady=5)

# Buttons
submit_button = tk.Button(root, text="Submit Guess", command=start_game, font=("Arial",12))
submit_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Game", command=start_game, font=("Arial",12))
reset_button.pack(pady=5)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 12) )
result_label.pack(pady=10)

# Start thr game first time
start_game()

# run loop
root.mainloop()