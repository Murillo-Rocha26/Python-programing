import pyautogui
import time


for i in range(2):
    time.sleep(3)

    pyautogui.press('win')

    pyautogui.write('Bloco de Notas', interval=0.5)

    pyautogui.press('enter')

    time.sleep(3)

    pyautogui.write('Hello World!!!')

    pyautogui.hotkey('alt','f4')

    time.sleep(1)

    pyautogui.press('n')

time.sleep(3)

pyautogui.press('win')

pyautogui.write('Chrome', interval=0.2)

pyautogui.press('enter')

time.sleep(3)

pyautogui.hotkey('alt', 'f4')

time.sleep(3)