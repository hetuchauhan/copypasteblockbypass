import sys
import os
from tkinter import *
import main

window=Tk()

window.title("Running Python Script")
window.geometry('150x30')

def run():
    os.system('txt.py')

btn = Button(window, text="Paste", bg="white", fg="red",command=run)
btn.grid(column=10, row=1)

window.mainloop()