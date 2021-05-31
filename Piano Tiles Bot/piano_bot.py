from pyautogui import *
import keyboard
import pyautogui
import win32api, win32con

#tile 1 1510
#tile 2 1620
#tile 3 1730
#tile 4 1840
#y 680
#rgb tile 101
time.sleep(5)
intial_pixel = [0]

def click(x,y):
        win32api.SetCursorPos((x,y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    

while (keyboard.is_pressed("e")==False):
    
    if pyautogui.pixel(580,650)[0] in intial_pixel:
        click(580,650)
    
    if pyautogui.pixel(880,650)[0] in intial_pixel:
        click(880,650)
    
    if pyautogui.pixel(1180,650)[0] in intial_pixel:  
        click(1180,650)
    
    if pyautogui.pixel(1480,650)[0] in intial_pixel:
        s(1480,650)
    