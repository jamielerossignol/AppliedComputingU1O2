from tkinter import *

#Setup window
wndw_main = Tk()
wndw_main.title("Grid Layout")

#Craete a label, then add it to the window
lbl_00 = Label(wndw_main, text="r0,c0")
lbl_00.grid(row=0,column=0)
lbl_01 = Label(wndw_main, text="r0,c1")
lbl_01.grid(row=0, column=1)
lbl_10 = Label(wndw_main, text="r1,c0").grid(row=1,column=0)
lbl_11 = Label(wndw_main, text="r1,c1").grid(row=1,column=1)
lbl_21 = Label(wndw_main, text="r2,c1").grid(row=2,column=1)

#display the window
wndw_main.mainloop()