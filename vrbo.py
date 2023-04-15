#from selenium import webdriver
#from datetime import time
#import time

#driver = webdriver.Chrome()
#url = "https://www.ilanlyfe.vom"

# driver.get(url)
# get_element = driver.element.text()

# print(get_element)


from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from chromedriver_py import binary_path

# service_object = Service(binary_path)

driver = webdriver.Chrome()
# driver = webdriver.Chrome(service=service_object)

# Target URL
driver.get("https://www.tripadvisor.com/")
# item = driver.find_element(By.ID, "typeahead_results")
# item.send_keys("st john")
# button = driver.find_element(By.ID, "SEARCH_BUTTON_CONTENT")
# button[0].click()
# driver.implicitly_wait(7)
# SCROLL_PAUSE_TIME = 0.5

#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC

#WebDriverWait(driver, 14).until(EC.presence_of_element_located(("Waypoint8")))
# Get scroll height
#last_height = driver.execute_script("return document.body.scrollHeight")

#while True:
    # Scroll down to bottom
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Wait to load page
     #time.sleep(SCROLL_PAUSE_TIME)

    # Calculate new scroll height and compare with last scroll height
     #new_height = driver.execute_script("return document.body.scrollHeight")
    # if new_height == last_height:
    #    break
    # last_height = new_height
#driver.implicitly_wait(14)

#for price in driver.find_elements(By.CLASS_NAME, "DualPrice__primary"):
# print(price.text)



