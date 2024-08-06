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
myWindow.geometry("400x400")

# instantiating a label or creating an instance of a label
myLabel = Label(myWindow, text="Hello World")
myLabel.pack() # This will put it by default at the top center


myWindow.mainloop() 