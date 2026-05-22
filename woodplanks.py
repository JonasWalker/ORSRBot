import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

def mahoganyPlanks():

    # click on halfway point
    points = [2458,87]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(26)

    # click on sawmill guy
    points = [1616,731]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(8)

    # click on mahgonay plank
    points = [666,1243]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(2)

    # click on halfway point2
    points = [2301,206]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(26)

    # click on bank
    points = [1149,1199]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(8)

    # click on plank
    points = [2337,947]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # click on logs
    points = [838,219]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    mahoganyPlanks()



def close():
   root.destroy()
#    root.quit()

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start Mahogany Planks", command=mahoganyPlanks)
startButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()