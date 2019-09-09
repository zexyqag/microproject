from tkinter import Label

from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
mainWindow.title("Die roller")

buttons = {0, 4, 6, 8, 10, 12, 20}
i = 2

name = Label(mainWindow, text="DICE ROLLER").grid(row=1, column=1)

img = ImageTk.PhotoImage(Image.open("dice.png"))
imglabel = Label(mainWindow, image=img).grid(row=2, column=1, rowspan=10)

dieButton = Button(mainWindow, text="Roll the die").grid(row=12, column=1)
number = Entry(mainWindow, bd=5).grid(row=13, column=1)



for x in buttons:
    x = Button(mainWindow, text=x).grid(row=i, column=2)
    i += 1

mainWindow.mainloop()
