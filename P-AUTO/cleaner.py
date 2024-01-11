import time
import pyautogui


def o(p):
    for i in range(len(p)):
        pyautogui.hotkey('winleft', 'r')  
        time.sleep(1)  
        pyautogui.write(p[i])
        pyautogui.press("enter")
        time.sleep(1)
        if i!=2:
            pyautogui.hotkey("ctrlleft","a")
            pyautogui.press("del")
            time.sleep(1)
            pyautogui.hotkey(["alt","f4"])
            time.sleep(1)
            pyautogui.hotkey(["alt","f4"])
        else:
            pyautogui.press("enter") 
            time.sleep(1) 
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(5)
            pyautogui.hotkey(["win","r"])
            time.sleep(1)
            pyautogui.write("explorer.exe shell:RecycleBinFolder")
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.hotkey(["ctrlleft","a"])
            pyautogui.press("del")
            time.sleep(1)
            pyautogui.press("enter")
            time.sleep(1)
            pyautogui.hotkey(["alt","f4"])

def t():
    pyautogui.hotkey(["win","i"])
    time.sleep(1)
    pyautogui.write("delete te")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.click(675,261,duration=1)
    time.sleep(2)
    pyautogui.click(573,573,duration=1)
    time.sleep(1)
    pyautogui.click(609,356,duration=1)
    time.sleep(1)
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.hotkey(["alt","f4"])

def main():
    o(["prefetch","%temp%","cleanmgr"])
    time.sleep(3)
    t()

if __name__ == "__main__":

    main()
