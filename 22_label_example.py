from tkinter import *

#Setup window
wndw_main = Tk()
wndw_main.title("Labelled")
wndw_main.geometry('300x200')

#Craete a label, then add it to the window
lbl_one = Label(wndw_main, text="Hello \n hello 2", font=("Arial Bold", 20), bg="red", fg="white")
lbl_one.pack()

#display the window
wndw_main.mainloop()