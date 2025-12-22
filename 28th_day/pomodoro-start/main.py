import tkinter
from math import floor
from playsound import playsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_time= WORK_MIN*60
    short_break_time = SHORT_BREAK_MIN*60
    long_break_time = LONG_BREAK_MIN*60
    if reps % 8 == 0:
        title_label.config(text="Long Break",fg=RED)
        count_down(long_break_time)
    elif reps % 2 == 0:
        title_label.config(text="Break",fg=PINK)
        count_down(short_break_time)
    elif reps % 2 == 1:
        title_label.config(text="Work",fg=GREEN)
        count_down(work_time)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    minutes = floor(count/60)
    seconds=count%60

    check_marks_count = int(reps/2 + 1 if reps%2==1 else 0)
    if seconds<10:
        seconds=f"0{seconds}"

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    
    if count>0:
        global timer
        timer = window.after(1000,count_down,count-1)
    else:
        check_marks.config(text="✔️"*check_marks_count)
        play_sound()
        start_timer()

def play_sound():
    playsound("28th_day\pomodoro-start\\timer_end.mp3")
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

title_label = tkinter.Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas = tkinter.Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomate_image = tkinter.PhotoImage(file="28th_day\pomodoro-start\\tomato.png")
canvas.create_image(100,112,image=tomate_image)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
#count_down(5)

start_button = tkinter.Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(column=0,row=2)

reset_button = tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=tkinter.Label(font=(FONT_NAME,10,"bold"),fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)
window.mainloop()