from tkinter import *

#Setup the Main Window
wndw_Main = Tk()
wndw_Main.title("Applied Computing")
wndw_Main.geometry('600x400')

#Creates an Entrybox for the form, and addes it to the form
enty_One = Entry(wndw_Main, bg="#e0e0e0", fg="black", font=("Arial Bold", 20))
enty_One.pack()

#display the window
wndw_Main.mainloop()