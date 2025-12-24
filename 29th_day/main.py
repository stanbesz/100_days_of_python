import tkinter
from tkinter import messagebox
import random
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def find_password():
    website_name = website_entry.get()

    dict_names = {}

    if len(website_name)==0:
        messagebox.showerror(title="Oops",message="Please fill website entry!")
    else:
        try:
            with open("29th_day\saved_logins.json","r") as file:
                #file.write(f"{website_name} | {username} | {password} \n")
                # Reading old data
                dict_names = json.load(file)
        except FileNotFoundError:
            messagebox.showerror(title="No Login Details",message="Currently there are no saved login details!")
        else:
            try:
                login_details = dict_names[website_name]
            except KeyError:
                messagebox.showerror(title="Website Not Found",message="Website Not Found!")
            else:
                messagebox.showinfo(title=website_name, message=f"Email:{login_details['email']}"
                           f"\n Password: {login_details['password']}")

def password_generator():
    if len(password_entry.get())>0:
        password_entry.delete(0,'end')

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    list_letters = [random.choice(letters) for _ in range(random.randint(8,10))]


    list_symbols = [random.choice(symbols) for _ in range(random.randint(2,4))]

    list_numbers = [random.choice(numbers) for _ in range(random.randint(2,4))]

    generated_password = list_letters+list_symbols+list_numbers

    newly_generated = generated_password
    random.shuffle(newly_generated)
    
    password_entry.insert(0,''.join(newly_generated))
    return newly_generated

# ---------------------------- SAVE PASSWORD ------------------------------- #
def clear_data():
    website_entry.delete(0,'end')
    password_entry.delete(0,'end')

def save():
    website_name = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website_name: {
            "email":username,
            "password":password,
        }
    }

    if len(website_name)==0 or len(username)==0 or len(password)==0:
        messagebox.showerror(title="Oops",message="Please fill every entry!")
    else:
        is_ok = messagebox.askokcancel(title=website_name,message=f"These are the detailed entered:\n Email:{username}"
                           f"\n Password: {password} \n Is it okay to save?")

        if is_ok:
            data = {}
            try:
                with open("29th_day\saved_logins.json","r") as file:
                    #file.write(f"{website_name} | {username} | {password} \n")
                    # Reading old data
                    data = json.load(file)

            except FileNotFoundError:
                with open("29th_day\saved_logins.json","w") as file:
                    #Saving updated data
                    json.dump(new_data,file,indent=4)
                    print(new_data)
            else:
                with open("29th_day\saved_logins.json","r") as file:
                    #file.write(f"{website_name} | {username} | {password} \n")
                    data.update(new_data)
                with open("29th_day\saved_logins.json","w") as file:
                    #Saving updated data
                    json.dump(data,file,indent=4)
                    print(data)

            clear_data()
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = tkinter.Canvas(width=200,height=200,highlightthickness=0)
lock_image = tkinter.PhotoImage(file="29th_day\logo.png")
canvas.create_image((100,100),image=lock_image)
canvas.grid(row=0,column=1)

website_label = tkinter.Label(text="Website:",fg="black",font=("Times New Roman",12))
website_label.grid(column=0,row=1)
website_entry = tkinter.Entry(width=35)
website_entry.grid(row=1,column=1)
search_button = tkinter.Button(text="Search",width=14,command = find_password)
search_button.grid(row=1,column=2)

username_label = tkinter.Label(text="Email/Username:",fg="black",font=("Times New Roman",12))
username_label.grid(column=0,row=2)
username_entry = tkinter.Entry(width=53)
username_entry.insert(0,"saleksan@gmail.com")
username_entry.grid(row=2,column=1,columnspan=2)

password_label = tkinter.Label(text="Password:",fg="black",font=("Times New Roman",12))
password_label.grid(column=0,row=3)
password_entry = tkinter.Entry(width=35)
password_entry.grid(row=3,column=1)
password_button = tkinter.Button(text="Generate Password",command=password_generator)
password_button.grid(row=3,column=2)

add_button = tkinter.Button(text="Add",width=45,command=save)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()