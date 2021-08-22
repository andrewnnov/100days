from tkinter import *
from tkinter import messagebox


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    email_text = email_entry.get()
    website_text = website_entry.get()
    password_text = password_entry.get()

    if not website_text or not password_text:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty! ")
    else:
        is_ok = messagebox.askokcancel(title=website_text,
                                       message=f"These are the details entered: \nEmail: {email_text} "
                                               f"\nPassword {password_text} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as data:
                data.write(f"{website_text} | {email_text} | {password_text}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0, sticky=EW)

# label
website_label = Label(text="Website:")
website_label.grid(column=0, row=1, sticky=EW)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2, sticky=EW)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3, sticky=EW)

# Entries

website_entry = Entry(width=35)
website_entry.grid(column=1, row=1, columnspan=2, sticky=EW)
website_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2, sticky=EW)
email_entry.insert(0, "andrew@global.com")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3, sticky=EW)

# button

generate_password_button = Button(text="Generate Password")
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, sticky=W)


window.mainloop()