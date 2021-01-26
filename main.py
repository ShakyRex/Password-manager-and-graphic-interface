from tkinter import *
from tkinter import messagebox
import random
from random import choice, randint, shuffle
import pyperclip as p

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [random.choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [random.choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [random.choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols

    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, f'{password}')
    p.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def get_data():
    website = website_entry.get()
    password = password_entry.get()
    username = username_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo("Missing data", message="you left some data out")

    else:

        # boolean output
        is_ok = messagebox.askokcancel(title=f"{website}", message=f"data entered:\nEmail: {username}\nPassword: "
                                                                   f"{password}\n is it ok? ")

        if is_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {username} | {password}\n")
            # clear up the field, everything form beginning to end
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = Canvas(width=200,
                height=200,
                highlightthickness=0)

logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

username_label = Label(text="Email/Username:")
username_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
# curser here by default
website_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2)

# 0 -> insert at the very beginning
username_entry.insert(0, "jack.federle@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button
generate_pass_button = Button(text="Generate Password", command=generate_password)
generate_pass_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=get_data)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
