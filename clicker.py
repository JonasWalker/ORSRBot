import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

pyautogui.click()

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# should be center of guy
# x,y = 900, 490

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

# initialize the WindowCapture class
wincap = WindowCapture('RuneLite - Its xMythic2')
# initialize the Vision class
vision_thing = Vision('fishingSpot.jpg')

# vision_thing = Vision('fullInventoryOfCookedFish.jpg')

# start fishing process
# assume inventory is empty (exept rod and feathers)
# assume inventory is closed---


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