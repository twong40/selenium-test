from selenium import webdriver                    # Import module 
from selenium.webdriver.common.keys import Keys   # For keyboard keys 
from selenium.webdriver.support.ui import WebDriverWait, Select 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options # Options for chromewebdriver
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException # Exceptions for webdriver
import math 
from random import randint
from time import sleep
ex=(NoSuchElementException,StaleElementReferenceException,)
options = Options()
options.headless = True # Set headless for chrome
browser = webdriver.Chrome(executable_path="../ChromeDriver/chromedriver")
while (True):
    browser.get('https://pisa.ucsc.edu/class_search/')
    sleep(randint(10,60))
    try: # proceed if element is found within 3 seconds otherwise will raise TimeoutException 
        # element = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.NAME, 'binds[:reg_status]')))
        #choose All Classes 
        drpStatus = Select(browser.find_element_by_name("binds[:reg_status]"))
        drpStatus.select_by_visible_text("All Classes")
        #find the Search button and click
        browser.find_element_by_xpath("/html/body/div/form/div/div[2]/div[15]/div/input").click()
        # change the number of elements to 100
        drpNumb = Select(browser.find_element_by_id("rec_dur"))
        drpNumb.select_by_visible_text("100")
        #get the total number of classes from xpath
        numClasses = browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/b[3]")
        pages = math.ceil(int(numClasses.text)/100) -2
        # xpath for the first click is different that the rest
        print("first")
        sleep(randint(10,100))
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/a").click()
        for x in range(pages):
            # wait until DOM is recreated and use the next link
            browser.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/a[2]").click()
            sleep(randint(10,100))
    except TimeoutException: 
        print("Time out!")

