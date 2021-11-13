import pyautogui
x,y = pyautogui.position()

pyautogui.click(600,600)
pyautogui.typewrite(['a','b','left','left','d','right','right','s'],interval=0.1)

#pyautogui.press("f1")
#pyautogui.hotkey("ctrl","o")
#pyautogui.typewrite()
#pyautogui.KEYBOARD_KEYS