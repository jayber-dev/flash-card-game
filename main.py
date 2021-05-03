BACKGROUND_COLOR = "#B1DDC6"

import pandas
from tkinter import *
word = "wow"
# ------------------------------- FRONT CARD ----------------------------------- #


# ------------------------------- BACK CARD ------------------------------------- #


# --------------------------------------USER UI --------------------------------- #

window = Tk()
window.config(bg="#B1DDC6",padx=20,pady=10)
window.title("flash card game")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_card_import = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=810, height=526, bg="#B1DDC6", highlightthickness=0)

canvas.create_image(405, 263, image=front_card_import)
canvas.grid(row=0, column=0,columnspan=2)
canvas.create_text(400,150,font=("ariel", 48, "italic"), text="french")
canvas.create_text(400, 260, font=("david", 50, "bold"), text=word)

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
