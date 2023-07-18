from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

s = Service("H:\\chrome94\\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get('http://hotstar.com')
html_doc = driver.page_source
username = driver.find_element(By.ID, "app")
test= username.find_element(By.CLASS_NAME ,"landing-page-container")
print(test.__dict__)
# line 14 indents correctly the output.
driver.quit()
