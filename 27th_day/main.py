import tkinter
import turtle

window = tkinter.Tk()
window.title("My first GUI Program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

# #Label 
my_label = tkinter.Label(text="I Am a Label", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)

my_label["text"]="New text"
my_label.config(text="New Text")

#Button
def button_clicked(message="New Text"):
    print(input.get())
    if input.get():
        message = input.get()
    my_label.config(text=message)

button = tkinter.Button(text="Click Me",command=button_clicked)
button.grid(column=1,row=1)

button = tkinter.Button(text="New Button",command=button_clicked)
button.grid(column=2,row=0)

#Entry
input=tkinter.Entry(width=10)
# input.pack() - Cannot have pack and grid at the some time. Once we use grid we can only use grid
input.grid(column=3,row=2)
msg = input.get()
print("Entry:",msg)

button.config(command=button_clicked)

window.mainloop()

