import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# #this way also we can invoke the browser.
# Replace with the actual path to your downloaded msedgedriver.exe
# service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)


#this will invoke the browser and webdriver is the class in selenium.
driver = webdriver.Chrome() #webdriver is the class and edge/chrome is the method of webdriver class, it will invoke the edge browser.

driver.get("https://rahulshettyacademy.com/client/#/auth/login")
driver.maximize_window()
Title = driver.title
print(Title)

driver.find_element(By.LINK_TEXT, "Forgot password?").click() #click on forgot password link_text locater.

#parent to child traversing in Xpath and css selector.
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com")



time.sleep(3)