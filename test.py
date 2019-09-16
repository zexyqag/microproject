from functools import partial
import random

from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
currentDice = 4  # value of the current dice

img = ImageTk.PhotoImage(Image.open("d4.png"))  # opening an initial image

buttons = {0, 4, 6, 8, 10, 12, 20}  # array for the amount dices

var = StringVar()
var.set("")

var2 = StringVar()
var2.set("Current dice is d4")


def rollTheDice():  # function for rolling the dice
    global currentDice
    if currentDice > 0:
        outcome = random.randrange(1, currentDice + 1)
    else:
        outcome = 0
    var.set("You rolled out a " + str(outcome) + " with a " + str(currentDice) + " sided dice")
    print("you rolled out a " + str(outcome) + " with a " + str(currentDice) + " sided dice")


mainWindow.title("Die roller")

result = Label(mainWindow, textvariable=var)
imagePanel = Label(mainWindow, image=img)  # a label for storing the image
whichDice = Label(mainWindow, textvariable=var2, bd=5)  # says which dice


def setCurrentDice(n):  # function for setting the dice
    global currentDice
    currentDice = n
    var2.set("Current dice is " + "D" + str(currentDice))
    name = "d" + str(n) + ".png"
    img2 = ImageTk.PhotoImage(Image.open(name))
    imagePanel.configure(image=img2)
    imagePanel.image = img2

    print("current dice is " + str(currentDice))


diceButton = Button(mainWindow, text="Roll the die", command=rollTheDice, bg="Brown", bd=6, activebackground="Grey",
                    height=3, width=10)

diceButton.pack(side=BOTTOM, fill="both")
whichDice.pack(side=BOTTOM, fill="both", expand="yes")
result.pack(side=BOTTOM, fill="both", expand="yes")
imagePanel.pack(side=LEFT, fill="both")

for x in buttons:  # for loop for creating and placing the dice buttons
    x = Button(mainWindow, text=x, bg="Orange", bd=6, activebackground="Grey", height=2, width=5,
               command=partial(setCurrentDice, x))
    x.pack(side=TOP, expand="yes")


mainWindow.mainloop()  # starting the window and all the widgets in it
