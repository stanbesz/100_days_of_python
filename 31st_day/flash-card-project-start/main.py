import tkinter
from tkinter import messagebox
import pandas
import random
#-------------------------------Logic--------------------------#
try:
    french_words = pandas.read_csv("31st_day\\flash-card-project-start\data\\words_to_learn.csv")
except FileNotFoundError:
    french_words = pandas.read_csv("31st_day\\flash-card-project-start\data\\french_words.csv")

french_map = french_words.to_dict(orient="records")
words_to_learn = french_map
print(type(french_map))
chosen_word:dict = {}

def learned_word():
    if len(words_to_learn)>0:
        words_to_learn.remove(chosen_word)
    else:
        messagebox.showinfo(title="Congratulations!",message="Completed learning list!")
        window.destroy()
    next_card()

def next_card():
    global chosen_word,flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(french_map)
    chosen_word = random_word

    canvas.itemconfig(word_text,text=chosen_word["French"],fill="black")
    canvas.itemconfig(title_text,text="French",fill="black")
    canvas.itemconfig(canvas_image,image=flash_front)
    flip_card()

def show_english():
    canvas.itemconfig(word_text,fill="white",text=chosen_word["English"])
    canvas.itemconfig(title_text,fill="white",text="English")
    canvas.itemconfig(canvas_image,image=flash_back)

def flip_card():
    global flip_timer
    flip_timer = window.after(3000,func=show_english)

def on_closing():
    really_quit = messagebox.askokcancel("Quit","Do you want to quit?")

    if really_quit:
        words_to_learn_df = pandas.DataFrame(words_to_learn)
        words_to_learn_df.to_csv("31st_day\\flash-card-project-start\data\words_to_learn.csv",index=False)
        window.destroy()
#---------------------------------UI---------------------------#
BACKGROUND_COLOR = "#B1DDC6"

window = tkinter.Tk()
window.title("Flashcards")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

canvas = tkinter.Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
flash_front = tkinter.PhotoImage(file="31st_day\\flash-card-project-start\images\card_front.png")
flash_back = tkinter.PhotoImage(file="31st_day\\flash-card-project-start\images\card_back.png")
canvas_image = canvas.create_image(400,263,image=flash_front)
title_text = canvas.create_text(400,150,text="Title",font=('Ariel',40,"italic"))
word_text = canvas.create_text(400,263,text="Word",font=('Ariel',60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

false_image = tkinter.PhotoImage(file="31st_day\\flash-card-project-start\images\wrong.png")
right_image = tkinter.PhotoImage(file="31st_day\\flash-card-project-start\images\\right.png")
false_button = tkinter.Button(image=false_image,highlightthickness=0,command=next_card)
right_button = tkinter.Button(image=right_image,highlightthickness=0,command=learned_word)
false_button.grid(row=1,column=0)
right_button.grid(row=1,column=1)

flip_timer = window.after(3000,func=flip_card)
next_card()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()
#---------------------------------UI---------------------------#