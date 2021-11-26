import pyautogui
import time
import datetime
import subprocess

x = input("ile screen'ów chcesz zrobić? (1 screen jest robiony co 30 sekund)")

for y,x in enumerate(range(int(x))):
    pyautogui.screenshot(f'screen{y}.png')
    date = (datetime.datetime.today()).strftime('%H:%M:%S')
    print(f"Zrobiłem {y+1} screen o godzinie {date}")
    time.sleep(30)

subprocess.run(["shutdown", "-s"])
