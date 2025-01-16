import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

def monkfish():

    # click on range
    points = [1610,589]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(7)

    # click on monkfish cook picture
    points = [254,1317]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(70)

    # click on bank
    points = [895,745]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(7)

    # click on bag icon
    points = [1338,995]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # click on raw monkfish
    points = [1320,423]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    monkfish()



def close():
   root.destroy()
#    root.quit()

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start monkfish", command=monkfish)
startButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()