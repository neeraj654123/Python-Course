from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

options= Options()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://www.amazon.in/")

time.sleep(5)
select =driver.find_element(By.LINK_TEXT, "MX Player")
select.click()
time.sleep(3)
select =driver.find_element(By.LINK_TEXT, "Web Series")
select.click()
time.sleep(3)
driver.refresh()
time.sleep(5)
