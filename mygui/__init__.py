# LGRID
import os
from tkinter import *


def lgrid(self, text, gridcol, gridrow, **args):
    """  Label Maker
    Example :
        lgrid(root,'text to enter',0,0,**args)

    Where root is the instance of tkinter ,
    'Text to enter' is just that,
    0,0 is the column and row to place them"""
    lbl = Label(self, text=text)
    lbl.grid(column=gridcol, row=gridrow, **args)
