from functools import partial
from tkinter import Label
import random

from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
currentDice = 0  # value of the current dice
var = StringVar()
var.set("")
var2 = StringVar()
var2.set("")


def setCurrentDice(n):  # function for setting the dice
    global currentDice
    currentDice = n
    var2.set("Current dice is " + str(currentDice))
    print("current dice is " + str(currentDice))


def rollTheDice():  # function for rolling the dice
    global currentDice
    outcome = random.randrange(1, currentDice + 1)
    var.set("You rolled out a " + str(outcome) + " with a " + str(currentDice) + " sided dice")
    print("you rolled out a " + str(outcome) + " with a " + str(currentDice) + " sided dice")


mainWindow.title("Die roller")

buttons = {0, 4, 6, 8, 10, 12, 20}  # array for the amount dices
i = 2  # a variable for assigning widgets to the grid slots

name = Label(mainWindow, textvariable=var).grid(row=12, column=1)

img = ImageTk.PhotoImage(Image.open("dice.png"))  # opening an image
imglabel = Label(mainWindow, image=img).grid(row=2, column=1, rowspan=10)  # a label for storing the image

dice = Label(mainWindow, textvariable=var2, bd=5).grid(row=1, column=1)  # says which dice

for x in buttons:  # for loop for creating and placing the dice buttons
    x = Button(mainWindow, text=x, bg="Orange", bd=6, activebackground="Grey", height=2, width=5,
               command=partial(setCurrentDice, x)).grid(row=i,
                                                        column=2)
    i += 1

diceButton = Button(mainWindow, text="Roll the die", command=rollTheDice, bg="Brown", bd=6, activebackground="Grey",
                    height=3, width=10).grid(
    row=13, column=1)

mainWindow.mainloop()  # starting the window and all the widgets in it
