import time
from selenium import webdriver
from google_authetication import google_authetication
from access_elements import access_elements

f = open("data.txt", 'a')
k = 0


ID = ''
PW = '' # Insert google email, PW

driver = google_authetication(ID,PW)

# open obj browser
URL = 'https://stackshare.io/application_and_data' # Base URL
driver.get(url=URL)

main_class = ['application_and_data', 'utilities', 'devops', 'business_tools']

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

for stack_class in main_class:
    URL = 'https://stackshare.io/'+stack_class
    driver.get(url=URL)
    data = access_elements(driver, stack_class)
    for element in data:
        try:
            f.write(str([k]+element))
            f.write('\n')
        except:
            pass
        k += 1
f.close()


    
        