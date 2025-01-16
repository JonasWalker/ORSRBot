import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")


def superheat():
    count = 0
    while(True):
        # click on superheat
        pyautogui.moveTo(1808, 930, 1)
        pyautogui.click(1808, 930, 1)
        # click on iron ore
        pyautogui.moveTo(1851, 1085, 1)
        pyautogui.click(1851, 1085, 1)

        count += 1
        if count == 28:
            break

    # click on bank booth
    pyautogui.moveTo(882, 610, 1)
    pyautogui.click(882, 610, 1)

    # click on iron ingot
    pyautogui.moveTo(1762, 873, 1)
    pyautogui.click(1762, 873, 1)

    # click on iron ore
    pyautogui.moveTo(805, 691, 1)
    pyautogui.click(805, 691, 1)
    
    # click on bank X
    pyautogui.moveTo(1059, 118, 1)
    pyautogui.click(1059, 118, 1)

    # repeat
    superheat()

def close():
   root.destroy()
#    root.quit()

def zoom():    
    time.sleep(3)
    pyautogui.scroll(-2500)

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start Superheat iron", command=superheat)
startButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()

clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()