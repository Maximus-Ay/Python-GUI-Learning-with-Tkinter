'''
    To get started with GUI programming which stands for Graphical user interface, you need to import
    of tkinter module which is a module for building graphical user interfaces that come directly with python.
'''

'''
    Now to continue programming using tkinter, you need to be able to distinguish between windows and widgets.
    => A widget consists of GUI elements such as buttons, labels, text boxes and images
    => A window is a container that holds the different widgets
'''

'''
    To get started you need to able to first of all import the tkinter module as well as all it has to offer.
    Then to create a window and display it, there are two things that must be done

    1) You create an instance of the window class (Tk class) in tkinter (This is also known as Instantiation)
    2) You display the window by using the mainloop method
'''

from tkinter import * # This will import all the attributes and methods common to the tkinter module

# instantiation of the TK class
my_window = Tk()

# Displaying the window
my_window.mainloop()

# Running these two lines of code will create a default window in Tkinter
# It's as easy as that

