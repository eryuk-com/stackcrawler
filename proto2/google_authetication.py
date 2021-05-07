import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import pyautogui

def google_authetication(ID,PW):
    #google debuger mode excute
    try:
        shutil.rmtree(r"C:\chrometemp")  # remove Cookie, Cache files
    except FileNotFoundError:
        pass

    try:
        subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                        r'--user-data-dir="C:\chrometemp"')   # Open the debugger chrome
        
    except FileNotFoundError:
        subprocess.Popen(r'C:\Users\binsu\AppData\Local\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                        r'--user-data-dir="C:\chrometemp"')

    option = Options()
    option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

    chrome_ver = chromedriver_autoinstaller.get_chrome_version().split('.')[0]
    try:
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
        
    except:
        chromedriver_autoinstaller.install(True)
        driver = webdriver.Chrome(f'./{chrome_ver}/chromedriver.exe', options=option)
    driver.implicitly_wait(10)

    driver.get(
        url='https://accounts.google.com/signin/v2/identifier?hl=ko&passive=true&continue=https%3A%2F%2Fwww.google.com%2F'
            '%3Fgws_rd%3Dssl&ec=GAZAmgQ&flowName=GlifWebSignIn&flowEntry=ServiceLogin')


    # Google login page
    pyautogui.write(ID)    # Insert google email
    pyautogui.press('tab', presses=3)   # Press the Tab key 3 times!wkdus940815

    pyautogui.press('enter') 
    time.sleep(5)   # wait a process
    pyautogui.write(PW)   # Insert PW
    pyautogui.press('enter')

    return driver