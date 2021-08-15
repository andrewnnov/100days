import tkinter

window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)

# label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24))
my_label.pack()


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
button.pack()

# Entry
input = tkinter.Entry(width=20)
input.pack()








window.mainloop()




