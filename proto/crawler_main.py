import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import subprocess
import shutil
import pyautogui

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
pyautogui.write('')    # Insert google email
pyautogui.press('tab', presses=3)   # Press the Tab key 3 times
pyautogui.press('enter') 
time.sleep(5)   # wait a process
pyautogui.write('')   # Insert PW
pyautogui.press('enter')



# open obj browser
URL = 'https://stackshare.io/application_and_data' # Base URL
driver.get(url=URL)

# sol Base URL login Problem
categories = driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div[2]/div//a')
categories[0].click()
time.sleep(5)
login_btn = driver.find_element_by_css_selector('body > div.css-xxn4z4 > div > div > div > div > div > div.css-1h8dtvr > a.css-8ycecp')
login_btn.click()
time.sleep(5)
driver.get(url=URL)
time.sleep(5)


# crawling starting log
print('*'*40)
print('start crawling!!')
print(driver.title)
print(driver.current_url)
print('*'*40)

# get categori urls 
categories = driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div[2]/div//a')
categori_urls = [] 
for categori in categories:
    categori_urls.append(categori.get_attribute('href'))

# start categori loop
for categori_url in categori_urls:
    driver.get(url=categori_url)
    time.sleep(5)
    
    # spread group list 
    groupBtn = driver.find_element_by_css_selector('#btn-responsive')
    groupBtn.click()
    time.sleep(5)

    # get group urls
    groups = driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div[2]/div/a')
    
    group_urls = []
    for group in groups:
        group_urls.append(group.get_attribute('href'))

    # start group loop
    for group_url in group_urls:
        driver.get(url=group_url)
        time.sleep(5)

        # crawling log
        print(f'{categori_url} > {group_url} : crawling!!!!')

        # Page move loop
        while True:
            # get stack name element
            search_box = driver.find_elements_by_class_name('landing-stack-name')
            #############################################################
            # In this part, possible to do any work with each tech stack
            for stack in search_box:
                print(stack.text)
            #############################################################
            
             # if page has 'next' button, go to next page
            try:
                nextBtn = driver.find_element_by_css_selector("#wrap > div:nth-child(4) > div > div:nth-child(3) > nav > span.next > a")
                nextBtn.click()
                time.sleep(5)
            # else, end the page loop
            except:
                break
        