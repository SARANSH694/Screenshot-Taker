import pyautogui
import tkinter as tk
from tkinter.filedialog import *

root =tk.Tk()
root.geometry('300x300')

i = input('Enter yur choice')

def click_screenshot():
    screenshot = pyautogui.screenshot()
    path = asksaveasfilename()
    screenshot.save(path+'_screenshot.png')

if(i == 's'):
    click_screenshot()
else :
    print('Thanks')