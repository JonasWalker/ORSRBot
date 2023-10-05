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


def mining():
    count = 0
    while(True):
        print(count)
        # # click left spot
        pyautogui.moveTo(692, 917, 1)
        pyautogui.click(692, 917)
        time.sleep(5)
        # # wait 6 secs

        # # click right spot
        pyautogui.moveTo(1183, 396, 1)
        pyautogui.click(1183, 396)
        time.sleep(4)
        # wait 6 secs

        count += 1
        if count == 14:
            break

    emptyInventoryOfIronOre()
    mining()





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

def emptyInventoryOfIronOre():
    points = findSomethingBasic('mining/IronOreInInventory.jpg', .90)
    print("point: ", points)
    for point in points:
        pyautogui.moveTo(point[0], point[1], .5)
        pyautogui.keyDown('shift')
        pyautogui.click(point[0], point[1])
        pyautogui.keyUp('shift')

    print("empty inventory complete")


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


startMiningButton = Button(root, text="Start mining iron", command=mining)
startMiningButton.pack()

testButton = Button(root, text="test image", command=testImage)
testButton.pack()

dropButton = Button(root, text="drop iron ore", command=emptyInventoryOfIronOre)
dropButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()