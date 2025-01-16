import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui


root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

# start headless arrow process
# assume feathers are in slot 1 of inventory
# assume arrow shafts are in slot 2 of inventory
def fletchHeadlessArrows():
    # click on feather
    points = [1719,869]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on arrow shaft
    points = [1762,868]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on button
    points = [263,1070]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(13)
    

    fletchHeadlessArrows()

# start willow long bow
# assume knife are in slot 1 of inventory
# assume willow logs are in the rest of the slots
def fletchWillowLongBows():
    # click on knife
    points = [1722,872]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on log
    points = [1768,869]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click long bow option
    points = [262,1075]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # wait 45 sec
    time.sleep(48)
    # click on bank
    points = [819,604]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # # click on slot 2
    points = [1766,873]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on willow logs
    points = [858,232]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on X
    points = [1055,125]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])    

    fletchWillowLongBows()


# start maple short bow
# assume knife are in slot 1 of inventory
# assume maple logs are in the rest of the slots
def fletchMapleShortBows():
    # click on knife
    points = [1722,872]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on log
    points = [1768,869]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click long bow option
    points = [151,1070]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # wait 45 sec
    time.sleep(48)
    # click on bank
    points = [819,604]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # # click on slot 2
    points = [1766,873]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on willow logs
    points = [660,232]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on X
    points = [1055,125]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])    

    fletchMapleShortBows()


# start maple long bow
# assume knife are in slot 1 of inventory
# assume maple logs are in the rest of the slots
def fletchMapleLongBows():
    # click on knife
    points = [1722,872]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on log
    points = [1768,869]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click long bow option
    points = [262,1075]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # wait 45 sec
    time.sleep(48)
    # click on bank
    points = [819,604]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # # click on slot 2
    points = [1766,873]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on willow logs
    points = [660,232]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # click on X
    points = [1055,125]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])    

    fletchMapleLongBows()


def close():
   root.destroy()
#    root.quit()


def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start Headless Arrows", command=fletchHeadlessArrows)
startButton.pack()

startButton = Button(root, text="Start Willow Long Bows", command=fletchWillowLongBows)
startButton.pack()

startButton = Button(root, text="Start Maple Short Bows", command=fletchMapleShortBows)
startButton.pack()

startButton = Button(root, text="Start Maple Long Bows", command=fletchMapleLongBows)
startButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()