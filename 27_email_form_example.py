from tkinter import *
from tkinter import messagebox, StringVar

def clicked():
    email_address = ent_email.get()
    messagebox.showinfo("Email Added", email_address)

# USER INTERFACE LAYOUT
#=================================================================================
root = Tk() # required to create a window in which other widgets are placed
root.title("Email Form")

btn_add = Button(root, text="Add", command=clicked)
btn_add.grid(column=1, row=1, sticky=W, padx=5, pady=5)

ent_email = Entry(root, width=10)
ent_email.grid(column=2, row=1, sticky=W, padx=5, pady=5)

# the Close button is created and placed here.
# The destroy method (i.e. root.destroy) is causes the Window to close
Button(root, text="Close", command=root.destroy).grid(column=2, row=3, sticky=W, padx=5, pady=5)


# the mainloop() is required to make the program event driven
root.mainloop()
# END OF THE USER INTERFACE LAYOUT
#=================================================================================