from numpy import *
from PIL import ImageGrab
from PIL import ImageOps
import pyautogui
import time
import keyboard

dino = (444,260)

def main():
        while True:
            time.sleep(2)
            restart()
            while True:
                if (img_grab() != 229500):
                    pyautogui.press('space')
                    time.sleep(0.1)
            
def restart():
    pyautogui.click(682,242)

def img_grab():
    box = (dino[0]+50, dino[1], dino[0]+140, dino[1]+10)
    img = ImageGrab.grab(box)
    gray_ver = ImageOps.grayscale(img)
    a = array(gray_ver)
    return a.sum()

#def jump(val):
    
    
if __name__ == '__main__':
    main()
    