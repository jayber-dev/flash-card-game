BACKGROUND_COLOR = "#B1DDC6"

import pandas
import random
from tkinter import *

score = 0
rand_num = 100

# ------------------------------- CSV HANDLING --------------------------------- #
words = pandas.read_csv("data/french_words.csv")

words_english_list = words['English'].to_list()
words_french_list = words['French'].to_list()

print(words_english_list)
print(words_french_list)



# ------------------------------- RIGHT BUTTON --------------------------------- #
def right_button():
    global score
    global rand_num
    rand_num -= 1
    score += 1 
    front_card()
    canvas.create_text(400, 340, text=f"score : {score} ", font=("david", 16 ,"bold"))
    words_english_list.remove(random_num)
    words_french_list.remove(random_num)
    

    
# ------------------------------- WRONG BUTTON --------------------------------- #
def wrong_button():
    front_card()
    canvas.create_text(400, 340, text=f"score : {score} ", font=("david", 16 ,"bold"))
# ------------------------------- FRONT CARD ----------------------------------- #
def front_card():
    global timer_text
    global random_num
    global right_button

    
    right_button.config(state="disabled")

    wrong_button.config(state="disabled")
    random_num = random.randint(0, rand_num)

    canvas.create_image(405, 263, image=front_card_import)
    canvas.grid(row=0, column=0,columnspan=2)
    canvas.create_text(400,150,font=("ariel", 48, "italic"), text="French")
    canvas.create_text(400, 260, font=("david", 50, "bold"), text=words_french_list[random_num])
    canvas.create_text(400, 340, text=f"score : {score} ", font=("david", 16 ,"bold"))

    timer_text = canvas.create_text(400, 100,font=("ariel",16,"bold"), text="5")
    
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
    right_button.config(state="active")
    wrong_button.config(state="active")
    canvas.create_image(400,263 , image=back_card)
    canvas.create_text(400,150,font=("ariel", 48, "italic"), text="English")
    canvas.create_text(400, 260, font=("david", 50, "bold"), text=words_english_list[random_num])
    canvas.create_text(400, 340, text=f"score : {score} ", font=("david", 16 ,"bold"))
# --------------------------------------USER UI --------------------------------- #

window = Tk()
window.config(bg="#B1DDC6",padx=20,pady=10)
window.title("flash card game")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
front_card_import = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=810, height=526, bg="#B1DDC6", highlightthickness=0)
canvas.create_text(400, 340, text=f"score : {score} ", font=("david", 16 ,"bold"))

wrong_button = Button(image=wrong_img, highlightthickness=0, command=wrong_button)
wrong_button.grid(row=1, column=1)

right_button = Button(image=right_img, highlightthickness=0, command=right_button)
right_button.grid(row=1, column=0)

front_card()




window.mainloop()
