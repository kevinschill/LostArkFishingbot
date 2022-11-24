from math import fabs
from PIL import ImageGrab, Image
import numpy as np
import cv2 as cv
import time
import pyautogui
import random
import rect


def createRectangle():
    app = rect.RectShow()
    app.mainloop()
    temp_region = app.getCoords()
    del app

    return temp_region

print("Wait 5 Seconds for Setup Rectangle")
time.sleep(5)
coordinates = createRectangle()
time.sleep(5)
print("Wait 5 Seconds for Start botting.")


fishicon1 = cv.imread('fishIcon.png')
fishicon2 = cv.imread('fishIcon2.png')
fishicon3 = cv.imread('fishIcon3.png')

found_fish = False

while True: 
    if found_fish == False:
        img = ImageGrab.grab(bbox=coordinates)
        img_cv = cv.cvtColor(np.array(img),cv.COLOR_RGB2BGR)


        res = cv.matchTemplate(img_cv, fishicon1, cv.TM_CCOEFF_NORMED)
        if (res >= 0.8).any():
            pyautogui.press("e")
            time.sleep(random.randint(10,15))
            found_fish = True
        else:
            res = cv.matchTemplate(img_cv, fishicon2, cv.TM_CCOEFF_NORMED)
            if (res >= 0.8).any():
                pyautogui.press("e")
                time.sleep(random.randint(10,15))
                found_fish = True
            else:
                res = cv.matchTemplate(img_cv, fishicon3, cv.TM_CCOEFF_NORMED)
                if (res >= 0.8).any():
                    pyautogui.press("e")
                    time.sleep(random.randint(10,15))
                    found_fish = True

    if found_fish == True:
        pyautogui.press("e")
        time.sleep(1)
        found_fish = False
