import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")

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
    points = [1802,869]
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

def craftDragonNecklace():
    # click on furnance
    points = [1367,412]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)
    # click on braclet in menu
    points = [893,499]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(25)
    # click on bank booth
    points = [462,797]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])
    time.sleep(10)
    # click on jade braclet
    points = [1802,869]
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

    craftDragonNecklace()

def highAlchJadeBraclet():
     
    count = 0
    while(True):
        # click on high alch
        points = [1854,953]
        pyautogui.moveTo(points[0], points[1], 1)
        pyautogui.click(points[0], points[1])
        # click on braclet
        points = [1849,1086]
        pyautogui.moveTo(points[0], points[1], 1)
        pyautogui.click(points[0], points[1])
        time.sleep(2)

        count += 1
        if count == 27:
            break

    # click on bank
    points = [976,571]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])

    # click on gold
    points = [1764,871]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])

    # click on jade braclets
    points = [903,306]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])

    # exit bank
    points = [1061,126]
    pyautogui.moveTo(points[0], points[1], 1)
    pyautogui.click(points[0], points[1])


    highAlchJadeBraclet()



def close():
   root.destroy()
#    root.quit()


def zoom():    
    time.sleep(3)
    pyautogui.scroll(-2500)

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start Jade Braclet", command=craftJadeBraclets)
startButton.pack()

startButton = Button(root, text="Start Dragon Necklace", command=craftDragonNecklace)
startButton.pack()

startButton = Button(root, text="Start High Alch Jade Braclet", command=highAlchJadeBraclet)
startButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()

clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()