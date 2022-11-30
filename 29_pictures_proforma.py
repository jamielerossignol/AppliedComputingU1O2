# Import Libraries
#=================================================================================
from tkinter import *           # tkinter windows library
from PIL import Image,ImageTk   # for resizing the logo, required "pillow" to be installed via pip

# Declare Variables
#=================================================================================
# N / A

# Define Functions
#=================================================================================
# N / A

# USER INTERFACE LAYOUT
#=================================================================================
window_root = Tk() # Add the Main Window
window_root.title("Images")
window_root.geometry("420x110")

img_one = Image.open("dice.png") # Open an image
img_one = img_one.resize((200,100), Image.ANTIALIAS) # Resize an image
photo_img_one = ImageTk.PhotoImage(img_one) # Allows the displaying off images
image_label_one = Label(window_root,image=photo_img_one) #Attached the image to a Label,
# but could also include buttons, canvases, and text widgets
image_label_one.grid(column=1, row=1, columnspan=2, padx=5, pady=5) #columnspan spreads image across 2 columns

# Same as above, but for image 2
img_two = Image.open("deadline.jpg")
img_two = img_two.resize((200,100), Image.ANTIALIAS)
photo_img_two = ImageTk.PhotoImage(img_two)
image_label_two = Label(window_root,image=photo_img_two)
image_label_two.grid(column=3, row=1, columnspan=2,padx=5, pady=5) #columnspan spreads image across 2 columns

window_root.mainloop() # Activiate the main Window loop

# END OF THE USER INTERFACE LAYOUT
#=================================================================================