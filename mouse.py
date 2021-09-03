import pyautogui
from time import sleep

screenWidth,screenHeight = pyautogui.size()
print(screenWidth,screenHeight)

#while True:
#    pyautogui.moveTo(10, 11)
#    pyautogui.moveTo(12, 13)
#   pyautogui.click()
    
screenWidth,screenHeight = pyautogui.size()
print(screenWidth,screenHeight)

TEAMS_ICON = (42,50)
TEAMS_CHAT = (1385,124)
TEAMS_ALERT = (1390,65)

def openTeams():
    pyautogui.doubleClick(TEAMS_ICON)
    sleep(5)
    
def clicker():
    pyautogui.click(TEAMS_CHAT)
    sleep(5)
    pyautogui.click(TEAMS_ALERT)
    sleep(5)
    

openTeams()
while True:
    clicker()
        
