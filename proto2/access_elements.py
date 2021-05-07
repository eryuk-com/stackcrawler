import time
from selenium import webdriver



def access_elements(driver, stack_class):
    f = open("data.txt", 'a')

    # get category urls 
    res = []
    categories = driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div[2]/div//a')
    category_urls = []
    category_names = [] 
    for category in categories:
        category_urls.append(category.get_attribute('href'))
        category_names.append(category.text)

    # start category loop
    for idx, category_url in enumerate(category_urls):
        driver.get(url=category_url)
        time.sleep(5)
        
        # spread group list 
        groupBtn = driver.find_element_by_css_selector('#btn-responsive')
        groupBtn.click()
        time.sleep(5)

        # get group urls
        groups = driver.find_elements_by_xpath('//*[@id="wrap"]/div[2]/div/div[1]/div[2]/div/a')
        
        group_urls = []
        group_names = []
        for group in groups:
            group_urls.append(group.get_attribute('href'))
            group_names.append(group.text)

        # start group loop
        for jdx, group_url in enumerate(group_urls):
            driver.get(url=group_url)
            time.sleep(5)

            # crawling log
            print(f'{category_names[idx]} > {group_names[jdx]} : crawling!!!!')

            # Page move loop
            while True:
                # get stack name element
                search_box = driver.find_elements_by_class_name('landing-stack-name')
                #############################################################
                # In this part, possible to do any work with each tech stack
                for stack in search_box:
                    temp = [stack.text.lower(),
                            stack_class,
                            category_names[idx],
                            group_names[jdx],
                            stack.find_element_by_css_selector('a').get_attribute('href')]
                    print(temp)
                    res.append(temp)
                #############################################################
                
                # if page has 'next' button, go to next page
                try:
                    nextBtn = driver.find_element_by_css_selector("#wrap > div:nth-child(4) > div > div:nth-child(3) > nav > span.next > a")
                    nextBtn.click()
                    time.sleep(5)
                # else, end the page loopgmail.com          

                except:
                    break
    return res