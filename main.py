from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)

    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    website = website_entry.get()
    email = user_email.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email:": email,
            "password:": password,
        }
    }

    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.askokcancel(title="Oops!", message="Please don't leave any fields empty!")
    else:
        try:
            with open('data.json', 'r') as fh:
                # Reading old data
                data = json.load(fh)

        except FileNotFoundError:
            with open('data.json', 'w') as fh:
                json.dump(new_data, fh, indent=4)

        else:
            # Updating old data with new data
            data.update(new_data)

            with open('data.json', 'w') as fh:
                # Saving updated Data
                json.dump(data, fh, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            
# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as fh:
            data = json.load(fh)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
             email = data[website]["email:"]
             password = data[website]["password:"]
             messagebox.showinfo(title=website, message=f"Email:   {email}\nPassword:   {password}")
                
        else:
            messagebox.showinfo(title="Oops!", message="No details for the website exist")


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# ---------------------------- LABELS ------------------------------- #

web_label = Label(text="Website:")
web_label.grid(row=1, column=0)

user_label = Label(text="Email/Username:")
user_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# ---------------------------- ENTRIES ------------------------------- #

website_entry = Entry(width=30)
website_entry.grid(row=1, column=1, columnspan=1)
website_entry.focus()

user_email = Entry(width=49)
user_email.grid(row=2, column=1, columnspan=2)
user_email.insert(0, "allan.ascencio@gmail.com")

password_entry = Entry(width=30)
password_entry.grid(column=1, row=3)

# ---------------------------- BUTTONS ------------------------------- #

button = Button(text="Generate Password", command=password_gen)
button.grid(column=2, row=3)

button = Button(text="Add", width=30, command=save_data)
button.grid(column=1, row=4, columnspan=2)

button = Button(text="Search", width=15, command=find_password)
button.grid(column=2, row=1)

window.mainloop()