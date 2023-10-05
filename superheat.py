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

def findSomethingBasic(image, threshold=0.8):
    points = None  
    vision_thing.switchImage(image)
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, threshold, 'points')
    print(points)
    return points

def testImage():
    vision_thing.switchImage('firemaking/startingSpot.jpg')
    # vision_thing.switchImage('fire.jpg')
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, .80, 'points')
    print("points: ", points)
    print("pointsLen: ", len(points))
    if len(points) > 1:
        points = points[0]
    
    # point = points[0]
    print("points: ", points)

def zoom():    
    time.sleep(3)
    pyautogui.scroll(-2500)

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startFishingButton = Button(root, text="Start Superheat iron", command=superheat)
startFishingButton.pack()

testButton = Button(root, text="test image", command=testImage)
testButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()