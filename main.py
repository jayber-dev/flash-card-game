BACKGROUND_COLOR = "#B1DDC6"

import pandas
from tkinter import *

# ------------------------------- FRONT CARD ----------------------------------- #



# ------------------------------- BACK CARD ------------------------------------- #




# --------------------------------------USER UI --------------------------------- #

window = Tk()
window.config(bg="#B1DDC6")
# right_img = PhotoImage(file="/images/right.png")
# wrong_img = PhotoImage(file="/images/wrong.png")
front_card_import = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800,height=526)

canvas.create_image(400, 263, image=front_card_import)
canvas.grid(row=0,column=0)

 

window.mainloop()

