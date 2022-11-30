#Requires the PIP & Pillow Libraries install in PyCharm
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #for resizing the logo, required "pillow" to be installed via pip

from random import *
#import random  #this is required to be able to generate random numbers

root = Tk() # required to create a window in which other widgets are placed

root.title("Dice")

# it is not required to have a frame,as everything
# could go into the root window, but a frame is used as it supports
# "themed" functionality.
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)  #tell tk to expand and contract frame with window
root.rowconfigure(0, weight=1)  #tell tk to expand and contract frame with window

# resize the logo
img = Image.open("dice.png")
img = img.resize((200,100), Image.ANTIALIAS)
photoImg = ImageTk.PhotoImage(img)

# place the image
imageLabel = Label(mainframe,image=photoImg)
imageLabel.grid(column=2, row=1, columnspan=2) #columnspan spreads image across 2 columns

# The next few lines creates a Label widget and a special variable named - "throwsVar".
# "throwsVar" is a StringVar() and is assigned to the "textvariable" option.
# This method allow the text content of the label to be changed programmatically.
throwValueVar = StringVar()
throwValueVar.set("Number\nthrown\n")
ttk.Label(mainframe,textvariable=throwValueVar, relief="sunken").grid(column=1, row=1, sticky=W)

#=================================================================================
# Need to add the label with "number of throws for a six" in appropriate location
#=================================================================================


numOfThrows = 0
throwsVar = StringVar()
throwsVar.set(str(numOfThrows))
ttk.Label(mainframe, textvariable=throwsVar, relief="sunken").grid(column=3, row=2, sticky=W)


# this will process the click of the Go button
def clicked():
    global numOfThrows # global is use here so that the module variable is referenced
    #=================================================================================
    # Need to add necessary code to implement algorithm
    #=================================================================================
    throwValueVar.set("Number\nthrown\n")  # clear what is displayed
    dice = randint(1,6)
    throwValueVar.set(throwValueVar.get() + str(dice) + "\n")
    numOfThrows = 1
    # print dice result to textbox

    while dice != 6:
        dice = randint(1,6)
        numOfThrows = numOfThrows + 1
        throwValueVar.set(throwValueVar.get() + str(dice) + "\n")

    #Update num throws on form
    throwsVar.set(str(numOfThrows))

#=================================================================================
# Need to add a Button with text="Go" that calls the clicked procedure when clicked
#=================================================================================
ttk.Button(mainframe, text="Go", command=clicked).grid(column=2, row=3, sticky=W)

# the Close button is created and placed here.
# The destroy method (i.e. root.destroy) is causes the Window to close
ttk.Button(mainframe, text="Close", command=root.destroy).grid(column=3, row=3, sticky=W)

# adjusts appearance of all widgets in frame
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

# the mainloop() is required to make the program event driven
root.mainloop()