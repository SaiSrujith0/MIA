import pyautogui as p
import time
#print(p.position())
def s():
    p.hotkey(["win","4"])
    time.sleep(10)
    p.click(27,958,duration=2)
    time.sleep(2)
    p.click(1821,172,duration=1)
    p.click(1821,172,duration=1)
    time.sleep(10)
    p.click(1660,190,duration=1)
    time.sleep(2)
    p.hotkey(["win","m"])

def c():
    p.hotkey(["win","i"])
    time.sleep(1)
    p.click(136,818,duration=1)
    time.sleep(1)
    p.click(1679,214,duration=1)
    time.sleep(2)
    p.hotkey(["win","m"])
c()
time.sleep(1)
s()
