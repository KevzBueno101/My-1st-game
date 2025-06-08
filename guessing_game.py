import os
import sys
import random
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

# Initialize the main window
root = Tk()
root.geometry("800x600")
root.title("Guessing Game")

# Set the application icon
icon_path = resource_path("puzzle_icon.ico")
try:
    root.iconbitmap(icon_path)
except Exception as e:
    print(f"Error setting icon: {e}")

# Set the background image
bg_image_path = resource_path("assets/bg.jpg")
try:
    image = Image.open(bg_image_path)
    photo = ImageTk.PhotoImage(image)
    background_label = Label(root, image=photo)
    background_label.image = photo  # Keep a reference
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"Error loading background image: {e}")

# Initialize game variables
secret_num = random.randint(1, 10)
attempt = 0

def game():
    global attempt
    try:
        userguess = int(guess_ent.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid integer between 1 and 10.")
        return

    attempt += 1

    if userguess == secret_num:
        messagebox.showinfo("Congratulations!", f"You've guessed the secret number in {attempt} attempts!\n\n🎉🎉👏👏")
    elif abs(secret_num - userguess) <= 2:
        retry = messagebox.askretrycancel("Close Guess", f"You're very close! \nAttempts: {attempt}")
        if not retry:
            root.quit()
    else:
        retry = messagebox.askretrycancel("Try Again", f"Sorry, that's not correct.\n Attempts: {attempt}")
        if not retry:
            root.quit()

def restart_game():
    global secret_num, attempt
    secret_num = random.randint(1, 10)
    attempt = 0
    guess_ent.delete(0, END)
    messagebox.showinfo("Game Restarted", "The game has been reset. Try guessing the new number!")

# Create and place widgets
label = Label(root, text="Welcome to Guessing Game!", font=("Helvetica", 34), fg='white', bg="#06202B")
label.pack(pady=100)

ins = Label(root, text='Guess my secret number between 1 to 10 🙈', font=('Arial Italic', 20), fg='white', bg="#06202B")
ins.pack()

guess_ent = Entry(root, justify=CENTER, highlightcolor='orange',
                  highlightbackground='grey', highlightthickness=2, width=15, font=('Helvetica', 15))
guess_ent.pack(pady=20)

start_btn = Button(root, text='Enter Guess', font=('Helvetica', 15), fg='white', bg="#06202B", width=15, command=game)
start_btn.pack()

restart_btn = Button(root, text='Restart', font=('Helvetica', 15), fg='white', bg="#06202B", width=15, command=restart_game)
restart_btn.pack(pady=75)

root.mainloop()
