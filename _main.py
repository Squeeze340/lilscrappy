import os
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title
print(title)
