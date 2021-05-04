BACKGROUND_COLOR = "#B1DDC6"

import pandas
import random
from tkinter import *
word = "wow"

# ------------------------------- CSV HANDLING --------------------------------- #
words = pandas.read_csv("data/french_words.csv")
words_list_french = words['French'].to_list()
words_list_english = words["English"].to_list()

words_dict = words.to_dict('dict')

random_num = random.randint(0, 100)



# ------------------------------- FRONT CARD ----------------------------------- #
def front_card():
    global timer_text
    
    canvas.create_image(405, 263, image=front_card_import)
    canvas.grid(row=0, column=0,columnspan=2)
    canvas.create_text(400,150,font=("ariel", 48, "italic"), text="French")
    canvas.create_text(400, 260, font=("david", 50, "bold"), text=words_dict["French"][random_num])

    timer_text = canvas.create_text(400, 100, text="5")
    
    count_down(5)



# ------------------------------- TIMER ---------------------------------------- #
def count_down(count):
    
    canvas.itemconfig(timer_text, text=count)
    
    if count > 0:
        time = window.after(1000, count_down, count-1)
    else:
        card_flip()
        
    
# ------------------------------- BACK CARD ------------------------------------- #
def card_flip():
    canvas.create_image(400,263 , image=back_card)
    canvas.create_text(400,150,font=("ariel", 48, "italic"), text="English")
    canvas.create_text(400, 260, font=("david", 50, "bold"), text=words_dict["English"][random_num])

# --------------------------------------USER UI --------------------------------- #

window = Tk()
window.config(bg="#B1DDC6",padx=20,pady=10)
window.title("flash card game")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_card_import = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=810, height=526, bg="#B1DDC6", highlightthickness=0)


front_card()

right_button = Button(image=right_img, highlightthickness=0)
right_button.grid(row=1, column=0)

wrong_button = Button(image=wrong_img, highlightthickness=0)
wrong_button.grid(row=1, column=1)

window.mainloop()
