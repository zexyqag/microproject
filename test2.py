from tkinter import *
from PIL import ImageTk, Image

root = Tk()
pressedOrNot = False
img = ImageTk.PhotoImage(Image.open("d4.png"))
panel = Label(root, image=img)


def callback():
    global pressedOrNot

    if pressedOrNot == False:
        img2 = ImageTk.PhotoImage(Image.open("d6.png"))
        panel.configure(image=img2)
        panel.image = img2
        print("hi i sucku")
        pressedOrNot = True

    elif pressedOrNot == True:
        panel.configure(image=img)
        panel.image = img
        pressedOrNot = False

diceButton = Button(root, text="Roll the die", command=callback)
diceButton.pack(side="bottom", fill="both", expand="yes")
panel.pack(side="bottom", fill="both", expand="yes")

root.bind("<Return>", callback)
root.mainloop()
