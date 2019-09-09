from tkinter import Label

from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
mainWindow.title("Die roller")

buttons = {0, 4, 6, 8, 10, 12, 20}
i = 2


def random(numbers):
    print(numbers)


name = Label(mainWindow, text="DICE ROLLER").grid(row=1, column=1)

img = ImageTk.PhotoImage(Image.open("dice.png"))
imglabel = Label(mainWindow, image=img).grid(row=2, column=1, rowspan=10)

dieButton = Button(mainWindow, text="Roll the die", bg="Brown", bd=6, activebackground="Grey", height=3, width=10).grid(
    row=12, column=1)
number = Entry(mainWindow, bd=5).grid(row=13, column=1)

for x in buttons:
    x = Button(mainWindow, text=x, bg="Orange", bd=6, activebackground="Grey", height=2, width=5, command=random(x)).grid(row=i,
                                                                                                                  column=2)
    i += 1

mainWindow.mainloop()
