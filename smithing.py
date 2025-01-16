import cv2 as cv
import numpy as np
import os
import time
from windowcaptureNOTNEEDED import WindowCapture
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


def ironChest():

    # click on anvil
    points = [1334,504]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)

    # click on iron plate
    points = [782,563]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(15)

    # click bank booth
    points = [495,630]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)   

    # click on iron plate in inventory
    points = [1761,871]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # click on iron bar in bank
    points = [759,692]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(1)

    # repeat
    ironChest()

def smeltCannonBalls():
    # click on furnance
    points = [1367,410]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(6)
    # click on cannonball in menu
    points = [262,1080]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(75)
    # click on bank booth
    points = [454,815]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(6)
    # click on steel bar
    points = [1006,275]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    # time.sleep(1)
    # repeat
    smeltCannonBalls()



def close():
   root.destroy()
#    root.quit()

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startIronChestButton = Button(root, text="Start iron chest", command=ironChest)
startIronChestButton.pack()

startSmeltCannonBallsButton = Button(root, text="Start cannonballs", command=smeltCannonBalls)
startSmeltCannonBallsButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()