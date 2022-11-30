# Adapted from https://www.tutorialspoint.com/python/tk_messagebox.htm
# to work with tkinter on PyCharm.
# Compare the two if you want to know what I did
import tkinter as Tkinter
from tkinter import messagebox as tkMessageBox

# Add main window
wnd_main = Tkinter.Tk()

# hello function
def callback_sayhello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

# Add buttons
btn_1 = Tkinter.Button(wnd_main, text = "Say Hello", command = callback_sayhello)
btn_1.pack()

#Dispaly the window
wnd_main.mainloop()