''' 
    MODIFYING WINDOWS IN TKINTER
    As earlier discussed, a simple window is created in python using tkinter in basically 2 lines
    Now when the window appears upon running the program, it has some things that can be modified, 
    like:
    - the height, width,
    - the title,
    - the title icon at the top left

    Note: Anything written between the instantiation of the Tk() class (the window) and the displaying of the 
         window affects the window. and anything written after the mainloop will not be renderred.
'''

from tkinter import *

window = Tk()
# Let's change the dimensions of the window, that is the width and height. 
# This is done using the geometry method
# The arguments are (Width x Height) in quotation marks 
window.geometry("600x500")

# Now let's change the title of the window from its default title tk to anything we want.
# This can be done by using the title method, and setting the title to that which we want
window.title("Maximus First GUI window")

# So now we can modify the icon that is at the top left of the window
# near the title. for this to be done, we need to convert the image file that we want to use into
# A photoImage, since tkinter recognises only that.
icon = PhotoImage(file='Windows\pic.png')
window.iconphoto(True,icon)

window.config(background="blue")

window.mainloop()


# Note that for the images I tried the jpeg format and the PhotoImage() class doesn't recognise that format