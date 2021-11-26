import pyautogui
import time
import datetime
import os

for y,x in enumerate(range(180)):
    pyautogui.screenshot(f'screen{y}.png')
    date = (datetime.datetime.today()).strftime('%H:%M:%S')
    print(f"Zrobiłem {y+1} screen o godzinie {date}")
    time.sleep(30)

os.system("shutdown /r /s 1")