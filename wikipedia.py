from selenium import webdriver

from webdriver_manager.firefox import GeckoDriverManager

import pyautogui as pg
from selenium.webdriver.common.keys import Keys
import time


# this is to go to browser and search for the page
driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
time.sleep(10)
driver.get("https://www.wikipedia.org/")

driver.maximize_window() #this is to make screen maximixe  
time.sleep(5)

# here i am sending the search keys
input=driver.find_element_by_xpath("//input[@id='searchInput']")
input.click()
input.send_keys("martin luther king")
time.sleep(3)

# this is to select the page
select = driver.find_element_by_xpath("/html[1]/body[1]/div[3]/form[1]/fieldset[1]/div[1]/div[2]/div[1]/a[1]")
select.click()
