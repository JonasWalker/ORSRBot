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


def oakFiremaking():
    points = findSomethingBasic('firemaking/startingSpot.jpg', 0.7)  
    points = points[0]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)

    oakLogsPoints = findSomethingBasic('firemaking/OakLogInInventory.jpg', 0.7)
    tinderBoxPoints = findSomethingBasic('firemaking/tinderBoxInInventory.jpg', 0.7) 
    tinderBoxPoints = tinderBoxPoints[0]

    for oakLogPoint in oakLogsPoints:
        pyautogui.moveTo(tinderBoxPoints[0], tinderBoxPoints[1], 1)
        pyautogui.click(tinderBoxPoints[0], tinderBoxPoints[1])

        pyautogui.moveTo(oakLogPoint[0], oakLogPoint[1], 1)
        pyautogui.click(oakLogPoint[0], oakLogPoint[1])
        time.sleep(3)

    
    bankBoothPoints = findSomethingBasic('firemaking/bankBooth.jpg', 0.7)
    bankBoothPoints = bankBoothPoints[0]
    pyautogui.moveTo(bankBoothPoints[0]+15, bankBoothPoints[1], 3)
    pyautogui.click(bankBoothPoints[0]+15, bankBoothPoints[1])
    time.sleep(14)

    # get more wood
    oakLogBankSpotPoints = findSomethingBasic('firemaking/OakBankSlot.jpg', 0.8)
    oakLogBankSpotPoints = oakLogBankSpotPoints[0]
    pyautogui.moveTo(oakLogBankSpotPoints[0], oakLogBankSpotPoints[1], 1)
    pyautogui.click(oakLogBankSpotPoints[0], oakLogBankSpotPoints[1])
    time.sleep(1)

    # repeat
    oakFiremaking()

def willowFiremaking():
    points = findSomethingBasic('firemaking/startingSpot.jpg', 0.7)  
    points = points[0]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)

    oakLogsPoints = findSomethingBasic('firemaking/WillowLogInInventory.jpg', 0.7)
    tinderBoxPoints = findSomethingBasic('firemaking/tinderBoxInInventory.jpg', 0.7) 
    tinderBoxPoints = tinderBoxPoints[0]

    for oakLogPoint in oakLogsPoints:
        pyautogui.moveTo(tinderBoxPoints[0], tinderBoxPoints[1], 1)
        pyautogui.click(tinderBoxPoints[0], tinderBoxPoints[1])

        pyautogui.moveTo(oakLogPoint[0], oakLogPoint[1], 1)
        pyautogui.click(oakLogPoint[0], oakLogPoint[1])
        time.sleep(3)

    
    bankBoothPoints = findSomethingBasic('firemaking/bankBooth.jpg', 0.7)
    bankBoothPoints = bankBoothPoints[0]
    pyautogui.moveTo(bankBoothPoints[0]+15, bankBoothPoints[1], 3)
    pyautogui.click(bankBoothPoints[0]+15, bankBoothPoints[1])
    time.sleep(14)

    # get more wood
    oakLogBankSpotPoints = findSomethingBasic('firemaking/willowBankSlot.jpg', 0.8)
    oakLogBankSpotPoints = oakLogBankSpotPoints[0]
    pyautogui.moveTo(oakLogBankSpotPoints[0], oakLogBankSpotPoints[1], 1)
    pyautogui.click(oakLogBankSpotPoints[0], oakLogBankSpotPoints[1])
    time.sleep(1)

    # repeat
    willowFiremaking()




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
    vision_thing.switchImage('firemaking/OakBankSlot.jpg')
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

def goToPoint():
    vision_thing.switchImage('firemaking/OakBankSlot.jpg')
    # vision_thing.switchImage('fire.jpg')
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, .80, 'points')
    print("points: ", points)    
    point = points[0]
    print("points: ", points)

    pyautogui.moveTo(point[0], point[1], 1)
    pyautogui.click(point[0], point[1])

    


startFishingButton = Button(root, text="Start Oak firemaking", command=oakFiremaking)
startFishingButton.pack()

startFishingButton = Button(root, text="Start Willow firemaking", command=willowFiremaking)
startFishingButton.pack()

testButton = Button(root, text="test image", command=testImage)
testButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()

pointButton = Button(root, text="go to point", command=goToPoint)
pointButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()