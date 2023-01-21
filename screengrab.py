import pyautogui
import time
from time import time, ctime

def take_screenshot():
  t = time()  
  file_name = ctime(t) + ".png" 
  path_name = '/Users/joel/Desktop/Screenshots/'

  myScreenshot = pyautogui.screenshot()
  myScreenshot.save(path_name + file_name)
  

take_screenshot()

