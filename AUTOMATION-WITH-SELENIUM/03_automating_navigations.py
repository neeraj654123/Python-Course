from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()

driver.get("https://practice.expandtesting.com/")

driver.find_element(By.LINK_TEXT, "Tips").click()


time.sleep(2)
driver.back()
time.sleep(2) 
driver.forward()
time.sleep(2)
driver.refresh()
time.sleep(2)
driver.quit()