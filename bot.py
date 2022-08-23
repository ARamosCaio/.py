import pyautogui as gui
import time
import random, string


#number = input('Enter the number: ')
sentence = ['every', 'word', 'in', 'this', 'sentence', 'was','sent', 'using','python','in','a','annoying','way']

time.sleep(5)

for i in range(len(sentence)):
    msg = "".join(sentence[i])
    gui.typewrite(msg)
    gui.press('Enter')
