from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

# Keep browser open after script finishes
options = Options()
options.add_experimental_option("detach", True)

# Launch Chrome
driver = webdriver.Chrome(options=options)
driver.maximize_window()

# Open Google
driver.get("https://www.google.com")

# Find the search box and type the query
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("selenium")

# Press Enter to search
search_box.send_keys(Keys.ENTER)

# Wait until you press Enter in the terminal
input("Press Enter to close the program...")