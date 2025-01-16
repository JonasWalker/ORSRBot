import cv2 as cv
import numpy as np
import os
import time
from tkinter import *
import pyautogui

# should be center of guy
# x,y = 900, 490

root = Tk()
root.title("OSRS Bot")
root.geometry("500x300")


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

    # emptyInventoryOfIronOre()
    mining()





def close():
   root.destroy()
#    root.quit()

# def emptyInventoryOfIronOre():
#     points = findSomethingBasic('mining/IronOreInInventory.jpg', .90)
#     print("point: ", points)
#     for point in points:
#         pyautogui.moveTo(point[0], point[1], .5)
#         pyautogui.keyDown('shift')
#         pyautogui.click(point[0], point[1])
#         pyautogui.keyUp('shift')

#     print("empty inventory complete")

def zoom():    
    time.sleep(3)
    pyautogui.scroll(-2500)

def getMousePosition():
    time.sleep(3)
    points = pyautogui.position()
    print("Mouse Position: ", points)


startButton = Button(root, text="Start mining iron", command=mining)
startButton.pack()

zoomButton = Button(root, text="zoom", command=zoom)
zoomButton.pack()

positionButton = Button(root, text="get mouse position", command=getMousePosition)
positionButton.pack()


clostButton = Button(root, text="Exit", command=close)
clostButton.pack()
root.mainloop()