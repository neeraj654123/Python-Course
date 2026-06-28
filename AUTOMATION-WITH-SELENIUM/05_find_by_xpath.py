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
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("Books")
time.sleep(5)
driver.find_element(By.XPATH, "//input[@id='nav-search-submit-button']").click()
time.sleep(5)