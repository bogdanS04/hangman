from tkinter import *
import pandas as pd
from random import choice

# Reading data

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")

current_card = {}


# Functions
def next_card():
    global current_card
    current_card = choice(to_learn)
    canvas.itemconfigure(language, text="French", fill="black")
    canvas.itemconfigure(word, text=current_card["French"], fill="black")
    canvas.itemconfigure(canvas_image, image=front_img)
    window.after(3000, flip_card)


def flip_card():
    global current_card
    canvas.itemconfigure(canvas_image, image=back_img)
    canvas.itemconfigure(language, text="English", fill="white")
    canvas.itemconfigure(word, text=current_card["English"], fill="white")


def answer_yes():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()

def answer_no():
    next_card()

# Configure GUI

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "bold")
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
# Creating canvas

canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
back_img = PhotoImage(file="images/card_back.png")
front_img = PhotoImage(file="images/card_front.png")
canvas_image = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="French", font=LANGUAGE_FONT, fill="black")
word = canvas.create_text(400, 263, text="word", font=WORD_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
right_image = PhotoImage(file="images/right.png")
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=right_image, highlightthickness=0, bd=0, command=answer_yes)
wrong_button = Button(image=wrong_image, highlightthickness=0, bd=0, command=answer_no)
right_button.grid(row=1, column=1)
wrong_button.grid(row=1, column=0)

# Playing continously

next_card()
window.mainloop()
