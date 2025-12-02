import tkinter

window = tkinter.Tk()
window.title("Mile to Km Converter")
window.minsize(width=200,height=100)
window.config(padx=20,pady=20)

# #Label 
label_miles = tkinter.Label(text="Miles", font=("Arial",12))
label_miles.grid(column=2,row=0)

label_km = tkinter.Label(text="Km", font=("Arial",12))
label_km.grid(column=2,row=1)

label_result = tkinter.Label(text="0", font=("Arial",12))
label_result.grid(column=1,row=1)

equal_label = tkinter.Label(text="is equal to", font=("Arial",12))
equal_label.grid(column=0,row=1)

input=tkinter.Entry(width=10)
input.grid(column=1,row=0)

def convert_miles():
    miles = float(input.get())
    kms = miles*1.609
    label_result.config(text=round(kms,2))

button = tkinter.Button(text="Calculate",command=convert_miles)
button.grid(column=1,row=2)

window.mainloop()