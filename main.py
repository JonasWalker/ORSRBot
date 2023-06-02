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


def fishing():
    points = findFishingSpot()        
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(15)

    print("Looking if still fishing")
    points = findSomethingBasic('youCantCarryAnymoreFish.jpg', 0.7)
    if points == []:
        print("still need to fish")
        fishing()
    else:
        print("Looking for fire")
        points = findFire()
        if points == []:
            print("Didnt find fire")
        pyautogui.moveTo(points[0], points[1], 1)
        pyautogui.click(points[0], points[1])
        time.sleep(5)            

        print("Cooking first fish")
        pyautogui.press('space')
        while(True):
            time.sleep(5)
            points = findSomethingBasic('notCooking.jpg', 0.7)
            if points != []:
                break

        print("Looking for fire")
        points = findFire()
        pyautogui.moveTo(points[0], points[1], 1)
        pyautogui.click(points[0], points[1])
        time.sleep(3)

        print("Cooking second fish. If any")
        pyautogui.press('space')
        while(True):
            time.sleep(5)
            points = findSomethingBasic('notCooking.jpg', 0.7)
            if points != []:
                break

        print("Dropping inventory")
        emptyInventoryOfCookedFish()

    fishing()




def close():
   root.destroy()
#    root.quit()


def findFire():
    points = None
    while(True):
        vision_thing.switchImage('fire.jpg')
        screenshot = wincap.get_screenshot()
        points = vision_thing.find(screenshot, 0.70, 'points')
        if(points != []):
            break
        
    print(points)
    return points[0]

def findFishingSpot():
    points = None  
    while(True):
        vision_thing.switchImage('fishingSpot2.jpg')
        screenshot = wincap.get_screenshot()
        points = vision_thing.find(screenshot, 0.70, 'points')
        if(points != []):
            break 
    print(points[0])
    return points[0]

def findSomethingBasic(image, threshold=0.8):
    points = None  
    vision_thing.switchImage(image)
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, threshold, 'points')
    print(points)
    return points

def emptyInventoryOfCookedFish():
    pyautogui.press('F1')
    points = findSomethingBasic('cookedSalmon.jpg', .90)
    print("point: ", points)
    for point in points:
        pyautogui.moveTo(point[0], point[1], .5)
        pyautogui.keyDown('shift')
        pyautogui.click(point[0], point[1])
        pyautogui.keyUp('shift')

    points = findSomethingBasic('cookedTrout.jpg', .90)
    for point in points:
        pyautogui.moveTo(point[0], point[1], .5)
        pyautogui.keyDown('shift')
        pyautogui.click(point[0], point[1])
        pyautogui.keyUp('shift')

    print("empty inventory complete")
    pyautogui.press('F1')


def testImage():
    vision_thing.switchImage('notCooking.jpg')
    # vision_thing.switchImage('fire.jpg')
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, .70, 'points')
    print("points: ", points)
    print("pointsLen: ", len(points))
    if len(points) > 1:
        points = points[0]
    
    # point = points[0]
    print("points: ", points)

def testFishingSpot():
    vision_thing.switchImage('fishingSpot2.jpg')
    # vision_thing.switchImage('fire.jpg')
    screenshot = wincap.get_screenshot()
    points = vision_thing.find(screenshot, .8, 'points')
    print("points: ", points)
    print("pointsLen: ", len(points))
    if len(points) > 1:
        points = points[0]
    
    # point = points[0]
    print("points: ", points)

    emptyInventoryOfCookedFish()

def testFireSpot():
    points = findFire()
    print("Fire points: ", points)

def zoom():    
    time.sleep(3)
    pyautogui.scroll(-2500)

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startFishingButton = Button(root, text="Start fishing", command=fishing)
startFishingButton.pack()

testButton = Button(root, text="test image", command=testImage)
testButton.pack()

dropButton = Button(root, text="drop fish", command=emptyInventoryOfCookedFish)
dropButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

fishingSpotButton = Button(root, text="find fishing spot", command=testFishingSpot)
fishingSpotButton.pack()

fireSpotButton = Button(root, text="find fire spot", command=testFireSpot)
fireSpotButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()