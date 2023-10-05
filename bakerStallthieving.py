import cv2 as cv
import numpy as np
import os
import time
from windowcapture import WindowCapture
from vision import Vision
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
# assume inventory is closed


def bakerStallthieving():
    for x in range(28):
        points = findSomethingBasic('bakerStallClickPoint.jpg', 0.8)
        moveToAndClick(points[0][0], points[0][1])
        time.sleep(3)
    
    emptyInventory()

    bakerStallthieving()

    

    


def moveToAndClick(x,y):
    pyautogui.moveTo(x, y, 1)
    pyautogui.click(x, y)

def close():
   root.destroy()
#    root.quit()



def findSomethingBasic(image, threshold=0.8):
    points = None  
    vision_thing.switchImage(image)
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, threshold, 'points')
    print(points)
    return points

def emptyInventory():
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 870)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 905)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 940)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 975)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 1010)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 1045)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1720, 1080)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 870)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 905)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 940)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 975)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 1010)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 1045)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1760, 1080)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 870)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 905)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 940)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 975)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 1010)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 1045)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1800, 1080)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 870)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 905)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 940)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 975)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 1010)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 1045)
    pyautogui.keyUp('shift')
    pyautogui.keyDown('shift')
    moveToAndClick(1840, 1080)
    pyautogui.keyUp('shift')


def testImage():
    vision_thing.switchImage('chocolateCake.jpg')
    # vision_thing.switchImage('fire.jpg')
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, .60, 'points')
    print("points: ", points)
    print("pointsLen: ", len(points))
    if len(points) > 1:
        points = points[0]
    
    # point = points[0]
    print("points: ", points)


def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startFishingButton = Button(root, text="Start bakerStallthieving", command=bakerStallthieving)
startFishingButton.pack()

testButton = Button(root, text="test image", command=testImage)
testButton.pack()

dropButton = Button(root, text="drop fish", command=emptyInventory)
dropButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()