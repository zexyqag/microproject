from functools import partial
from tkinter import Label
import random

from tkinter import *
from PIL import ImageTk, Image

mainWindow = Tk()
currentDice = 0  # value of the current dice


def setCurrentDice(n):  # function for setting the dice
    global currentDice
    currentDice = n
    print("current dice is " + str(currentDice))


def rollTheDice():  # function for rolling the dice
    global currentDice
    outcome = random.randrange(1, currentDice + 1)
    print("you rolled out a " + str(outcome) + " with a " + str(currentDice) + " dice")


mainWindow.title("Die roller")

buttons = {0, 4, 6, 8, 10, 12, 20} # array for the amount dices
i = 2 # a varaible for assigning widgets to the grid slots

name = Label(mainWindow, text="DICE ROLLER").grid(row=1, column=1)

img = ImageTk.PhotoImage(Image.open("dice.png")) # opening an image
imglabel = Label(mainWindow, image=img).grid(row=2, column=1, rowspan=10) # a label for storing the image

number = Entry(mainWindow, bd=5).grid(row=13, column=1) # entry bar

for x in buttons: # for loop for creating and placing the dice buttons
    x = Button(mainWindow, text=x, bg="Orange", bd=6, activebackground="Grey", height=2, width=5,
               command=partial(setCurrentDice, x)).grid(row=i,
                                                        column=2)
    i += 1

diceButton = Button(mainWindow, text="Roll the die", command=rollTheDice, bg="Brown", bd=6, activebackground="Grey",
                    height=3, width=10).grid(
    row=12, column=1)

mainWindow.mainloop() # starting the window and all the widgets in it
