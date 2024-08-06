'''
    LABELS IN TKINTER
    => first you create your window, as we have been doing since.
    => Next you instantiate the your label, using the Label class.
    => Now within the constructor of the Label class, the first thing you pass in is the name
       of your window, you created. then every other thing that follows are known as options and they 
       help you modify the label as you want.
    => Now after this, the label will not be found on the window, by default, you need to use methods that
       help you place the labels on the window. There are basically three of them, (the pack(), place() and grid())

       We will only study the pack for this
'''

from tkinter import *

myWindow = Tk()
# instantiating a label or creating an instance of a label, 
# whatever is within the Label constructor can be used to modify the label
# It is always good practice to separate them on different lines for clarity

icon = PhotoImage(file='Windows\\pic.png')
myLabel = Label(myWindow, 
                text="Hello World", # This is for the text of the label
                fg="green", # This is for the foreground or the color of the text
                font=("Times New Romans",40,"bold"), # This is for the font
                bg="black", # This is for the background color
                relief="raised", # This has to do with the border style
                bd=10, # Now this has to do with the border width
                padx=10, # This has to do with the padding. x here means left and right
                pady=10, # This has to do with the padding. y here stands for top and bottom
                #image=icon, Was commented because the image size is too big to be contained in the label
                compound='bottom'
                )


myLabel.pack() # This will put it by default at the top center


myWindow.mainloop() 

# You can add an image, but as usual you have to first convert it into a photo Image as we have always been doing