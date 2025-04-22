import tkinter as tk
from tkinter import messagebox
import random

score = 0
comp_score = 0
disp = None
root = None


def decide(num):
    global score
    comp_gen = random.randint(1, 6)

    if comp_gen == num:
        messagebox.showinfo("Out", f"You got out!\nFinal Score: {score}\nBetter luck next time.")
        restart_game()
    else:
        score += num
        update_display()
        check_winner()


def update_display():
    disp.delete(0, tk.END)
    disp.insert(0, str(score))


def check_winner():
    if score >= comp_score:
        messagebox.showinfo("Congratulations", f"You won the match!\nYour Score: {score}\nTarget: {comp_score}")
        restart_game()


def number_click(num):
    decide(num)


def restart_game():
    global root
    root.destroy()
    # Restart game after 1 second (1000 ms)
    root = tk.Tk()
    root.withdraw()
    root.after(1000, start_game)


def start_game():
    global root, disp, comp_score, score
    score = 0
    comp_score = random.randint(20, 60)

    root = tk.Tk()
    root.title("Virtual Cricket")
    root.geometry("600x400")
    root.configure(bg="#141414")
    root.resizable(False, False)

    # Title
    title_label = tk.Label(root, text="Virtual Cricket", font=("Verdana", 24), bg="#333333", fg="white")
    title_label.pack(pady=10)

    # Target
    target_label = tk.Label(root, text=f"Target Score: {comp_score}", font=("Verdana", 20), bg="#333333", fg="white")
    target_label.pack(pady=5)

    # Display score
    disp = tk.Entry(root, font=("Verdana", 20), justify="center", bd=2)
    disp.insert(0, str(score))
    disp.pack(pady=10)

    # Buttons 1-6
    button_frame = tk.Frame(root, bg="#141414")
    button_frame.pack(pady=10)

    for i in range(1, 7):
        btn = tk.Button(
            button_frame, text=str(i), font=("Segoe", 20), width=4,
            bg="#333333", fg="white", command=lambda x=i: number_click(x)
        )
        btn.grid(row=0, column=i-1, padx=5)

    # Batting label
    action_label = tk.Label(root, text="Choose your run", font=("Segoe", 18), bg="#141414", fg="orange")
    action_label.pack(pady=10)

    root.mainloop()


start_game()
