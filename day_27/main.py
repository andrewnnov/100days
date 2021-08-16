import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.grid(row=0, column=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New text"
my_label.config(text="New Text")

# button


# def button_clicked():
#     print("I got clicked")
#     my_label.config(text="Button Got Clicked")
#
#
# button = tkinter.Button(text="Click me", command=button_clicked)
# button.pack()

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)


button = tkinter.Button(text="Click me", command=button_clicked)
button.grid(row=1, column=1)


button2 = tkinter.Button(text="Click me too", command=button_clicked)
button2.grid(row=0, column=2)


# Entry
input = tkinter.Entry(width=20)
input.grid(row=2, column=3)








window.mainloop()




