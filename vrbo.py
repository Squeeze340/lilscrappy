#from selenium import webdriver
#from datetime import time
import time

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
driver.get("https://www.tripadvisor.com/ShowForum-g147400-i171-U_S_Virgin_Islands.html")
# item = driver.find_elements(By.CLASS_NAME, "typeahead-SINGLE_SEARCH_HER0")
# item.send_keys("st john")

#  Create a posts_list where we will store the posts
post_list = []

#  Loop through all the posts and get the needed information
for i in range(24):
    table = driver.find_element(By.ID, "SHOW_FORUMS_TABLE")
    if i == 0: 
        continue
    # get the link element and click it
    topic = f"//tbody[1]/tr[{i}]/td[3]/b/a"
    elements = table.find_elements(By.XPATH, topic)
    if len(elements)== 0:
        continue

    elements[0].click()
    # get the information from the post and create a post object\
    # try:
    elements = driver.find_elements(By.XPATH, "//span[@class='topTitleText']")
    print(elements[0].text)
    driver.back()
    # except: 
    #     print("had an error")
    # header = elements[0].text
    # adding the post's information to it. 

    # add the post object to the posts_list

    # go back to the country's forum page and continue 
    
# next_page = driver.find_element(By.CLASS_NAME "paging taLnk")
# next_page = driver.find_element(By.ID , "pager_top2")
# next_page.click()


# driver.implicitly_wait(7)
# SCROLL_PAUSE_TIME = 0.5

# from selenium.webdriver.support.ui import WebDriverWait
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



