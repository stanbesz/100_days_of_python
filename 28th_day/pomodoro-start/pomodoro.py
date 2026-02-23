import tkinter
from math import floor
from playsound import playsound
from tkinter import messagebox
import requests
from datetime import datetime
import time
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
pause_active = False
first_setup = True
counter = 0
PIXEL_USERNAME = "saleksan"
PIXEL_TOKEN = "scoobydoobiedoojijklajklljkvjkhhjkjkhl"
GRAPH_ID = "graphfloat"
PIXELA_ENDPOINT = "https://pixe.la/v1/users"
graph_config = {
    "id":GRAPH_ID,
    "name":"Coding practice",
    "unit":"minutes/seconds",
    "type":"float",
    "color":"ajisai",
    "timezone":"Europe/Sofia",
}
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    global reps
    reps = 0
    canvas.itemconfig(timer_text,text="00:00")
    check_marks.config(text="")
    title_label.config(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))

# ---------------------------- PAUSE MECHANISM ------------------------------- #

def pause_timer():
    global pause_active,first_setup
    if not pause_active:
        pause_active = True
    else:
        pause_active = False

    first_setup = False

# --------------------------- PAUSE LOGIC ------------------------------------ #
def pause_logic():
    global reps,pause_active,timer,first_setup

    pause_count = False

    if not first_setup:
        if pause_active:
            pause_buttion.config(text="Continue")
            title_label.config(text="Pause",fg=PINK)
            pause_count = True
        else:
            pause_buttion.config(text="Pause")
            title_label.config(text="Work",fg=GREEN)

    return pause_count
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
# ----------------------------- Close Logic ----------------------------------#
def post_results():
    global counter
    headers = {"X-USER-TOKEN":PIXEL_TOKEN}

    today = datetime.now()

    pixel_endpoint = f"{PIXELA_ENDPOINT}/{PIXEL_USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

    minutes = floor(counter/60)
    seconds=counter%60
    pixel_config = {
        "quantity":f"{minutes}.{seconds}",
        }
    max_retries = 10
    retry_delay = 2  # seconds (initial delay)
    attempt = 0

    while attempt < max_retries:
        try:
            response = requests.post(
                url=pixel_endpoint,
                json=pixel_config,
                headers=headers,
                timeout=10
            )

            if response.status_code == 200:
                print("Success:", response.content)
                break
            # Required due to Pixela giving 25% for each post request to not succeed
            elif response.status_code == 503:
                attempt += 1
                print(f"503 received. Retrying in {retry_delay} seconds... (Attempt {attempt})")
                time.sleep(retry_delay)
                retry_delay *= 2  # exponential backoff

            else:
                print(f"Request failed with status {response.status_code}: {response.content}")
                break

        except requests.exceptions.RequestException as e:
            attempt += 1
            print(f"Request error: {e}. Retrying in {retry_delay} seconds... (Attempt {attempt})")
            time.sleep(retry_delay)
            retry_delay *= 2

    else:
        print("Max retries reached. Request failed.")

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        post_results()
        window.destroy()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps,pause_active,timer,first_setup,counter
    minutes = floor(count/60)
    seconds=count%60
    
        
    check_marks_count = int(reps/2 + 1 if reps%2==1 else 0)
    if seconds<10:
        seconds=f"0{seconds}"

    canvas.itemconfig(timer_text,text=f"{minutes}:{seconds}")
    
    if count>0:
        if pause_logic():
            timer = window.after(1000,count_down,count)
        else:
            timer = window.after(1000,count_down,count-1)
            counter+=1
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

pause_buttion = tkinter.Button(text="Pause",highlightthickness=0,command=pause_timer)
pause_buttion.grid(column=1,row=2)

reset_button = tkinter.Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(column=2,row=2)

check_marks=tkinter.Label(font=(FONT_NAME,10,"bold"),fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()