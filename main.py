from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_gen():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    if len(website_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.askokcancel(title="Oops!", message="Please don't leave any fields empty!")
    else:
         is_ok = messagebox.askokcancel(title=f"{website_entry.get()}", message=f"There are the details entered \nEmail: {user_email.get()} "
                                f"\nPassword: {password_entry.get()} \nIs it ok to save?")

         if is_ok:
             with open('data.txt', 'a') as fh:
                 fh.write(f"{website_entry.get()} | {user_email.get()} | {password_entry.get()}\n")
                 clear_text()
    
def clear_text():
    website_entry.delete(0, END)
    password_entry.delete(0, END)


#---------------------------- UI SETUP ------------------------------- #


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

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()


user_email = Entry(width=35)
user_email.grid(row=2, column=1, columnspan=2)
user_email.insert(0, "allan.ascencio@gmail.com")


password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


# ---------------------------- BUTTONS ------------------------------- #

button = Button(text="Generate Password", command=password_gen)
button.grid(column=2, row=3)

button = Button(text="Add", width=36, command=save_data)
button.grid(column=1, row=4, columnspan=2)

window.mainloop()