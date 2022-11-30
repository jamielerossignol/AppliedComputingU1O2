from tkinter import *
#Also include the messagebox library
from tkinter import messagebox

#Setup the Main Window
wndw_Main = Tk()
wndw_Main.title("Applied Computing")
wndw_Main.geometry('400x400')

#Function to dispaly a message box
def callback_hello():
    messagebox.showinfo("Hello Python", "Hello World")

# Create 2 buttons, both trigger the function, callback_hello when clicked
btnOne = Button(wndw_Main, text="One", command = callback_hello)
btnTwo = Button(wndw_Main, text="Two", command = callback_hello, bg="navy", fg="white",activebackground="#A0A0a0",activeforeground="navy" )
#Add buttons to the window
btnOne.pack()
btnTwo.pack()

#display the window
wndw_Main.mainloop()