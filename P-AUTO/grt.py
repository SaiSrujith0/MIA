import pyautogui as p
import time
import pygetwindow as gw


c=0

windows = gw.getAllTitles()
l=["","Program Manager"]
for i in windows:
    if i not in l:
        if i=="Settings" and windows.count(i)>1:
            continue
        else:
            c+=1




def f():
    p.hotkey(["win","tab"])
    time.sleep(2)
    p.press("end")
    time.sleep(1)

    for i in range(c-1):
        p.hotkey(["ctrlleft","f4"])
        time.sleep(1)

    p.hotkey(["win","m"])
    time.sleep(1)

    for i in range(3):
        p.press("f5")
        time.sleep(2)

f()

