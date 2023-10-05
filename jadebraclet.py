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
# assume inventory is closed---


def craftJadeBraclets():
    # click on furnance
    points = [1367,412]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)
    # click on braclet in menu
    points = [718,577]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(25)
    # click on bank booth
    points = [462,797]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)
    # click on jade braclet
    points = [1787,871]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # time.sleep(1)
    # click on silver bar
    points = [904,199]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # time.sleep(1)
    # click on jade
    points = [951,200]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # repeat

    craftJadeBraclets()




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


startFishingButton = Button(root, text="Start Jade Braclet", command=craftJadeBraclets)
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