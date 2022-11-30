# Python Program to make a scrollable frame
# using Tkinter

from tkinter import *

def showStr(title, txt):
		
    # create root window
    root = Tk()
    root.title(title)
    root.configure(bg = 'bisque2')

    # create a horizontal scrollbar by
    # setting orient to horizontal
    h = Scrollbar(root, orient = 'horizontal')

    # attach Scrollbar to root window at
    # the bootom
    h.pack(side = BOTTOM, fill = X)

    # create a vertical scrollbar-no need
    # to write orient as it is by
    # default vertical
    v = Scrollbar(root)

    # attach Scrollbar to root window on
    # the side
    v.pack(side = RIGHT, fill = Y)
    

    # create a Text widget with 15 chars
    # width and 15 lines height
    # here xscrollcomannd is used to attach Text
    # widget to the horizontal scrollbar
    # here yscrollcomannd is used to attach Text
    # widget to the vertical scrollbar
    t = Text(root, width = 70, height = 25, wrap = NONE,
            xscrollcommand = h.set,
            yscrollcommand = v.set,
            font = ('arial', 15)
            )

    # insert some text into the text widget
    t.insert(END,txt)

    # attach Text widget to root window at top
    t.pack(side=TOP, fill=X)

    # here command represents the method to
    # be executed xview is executed on
    # object 't' Here t may represent any
    # widget
    h.config(command=t.xview)

    # here command represents the method to
    # be executed yview is executed on
    # object 't' Here t may represent any
    # widget
    v.config(command=t.yview)

    # the root window handles the mouse
    # click event
    root.mainloop()

# create an object to Scrollbar class
# showStr('ami ke\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
		
