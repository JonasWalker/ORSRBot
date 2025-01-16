import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")


def clicker():
    count = 0
    while True:
        time.sleep(.25)
        pyautogui.click()
        count+= 1
        if count == 720:
            break; 


def close():
   root.destroy()
#    root.quit()


startFishingButton = Button(root, text="clicker", command=clicker)
startFishingButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()