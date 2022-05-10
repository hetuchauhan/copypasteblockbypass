from pynput.keyboard import Key, Controller
from threading import Timer
import win32clipboard
import time
import tkinter as tk


def hello():
    from pynput.keyboard import Key, Controller
    global mstlst4

    for word in mstlst4:

        for letter in word:

            keyboard = Controller()
            keyboard.press(letter)
            keyboard.release(letter)

        import keyboard

for i in range(1):
    time.sleep(1)
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData()
    win32clipboard.CloseClipboard()

    print("ok")
    mstlst = data

    mstlst1 = mstlst.replace("Address","\n")
    mstlst2 = mstlst1.replace("Phone numbers", "\n")
    mstlst3 = mstlst2.replace("Phone number", "\n")
    mstlst4 = mstlst3.replace("Fax ","Fax: ")
    print(mstlst3)
    '''
    window = tk.Tk()
    '''
    t = Timer(2.0,hello)
    print("ok")
    t.start() # after 30 seconds, "hello, world" will be printed
