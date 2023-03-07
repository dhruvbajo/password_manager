from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="oops!", message="PLEASE MAKE SURE U DIDN'T LEAVE ANY BOX EMPTY")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered:\nEmail:{email}\nPassword:{password}\n"
                                               f"IS IT OKAY TO SAVE??")
        if is_ok:
            with open("data.csv", "a") as data_file:
                data_file.write(f"{website},{email},{password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", padx=5, pady=10)
website_label.grid(column=0, row=1,padx=20)

email_label = Label(text="Email/Username:", padx=5, pady=10)
email_label.grid(column=0, row=2)

password_label = Label(text="Password:", padx=5, pady=10)
password_label.grid(column=0, row=3)

website_input = Entry(width=45)
website_input.grid(column=1, row=1, columnspan=2, pady=10)
website_input.focus()

email_input = Entry(width=45)
email_input.grid(column=1, row=2, columnspan=2, pady=10)
email_input.insert(0, "dhruvbajoria0@gmail.com")

password_input = Entry(width=27)
password_input.grid(column=1, row=3, pady=10)

generate_password = Button(text="Generate Password", command=generate)
generate_password.grid(column=2, row=3)

add = Button(text="Add", width=44, padx=5, command=save)
add.grid(column=1, row=4, columnspan=2, pady=10)

window.mainloop()
