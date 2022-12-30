from tkinter import *


def changeOnHover(button, colorOnHover, colorOnLeave):

    button.bind("<Enter>", func=lambda e: button.config(
        background=colorOnHover))

    button.bind("<Leave>", func=lambda e: button.config(
        background=colorOnLeave))


root = Tk()

myButton = Button(root,
                  text="On Hover - Background Change",
                  bg="yellow")
myButton.pack()

changeOnHover(myButton, "red", "yellow")

root.mainloop()
