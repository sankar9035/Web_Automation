import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service

# #this way also we can invoke the browser.
# Replace with the actual path to your downloaded msedgedriver.exe
service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service_obj)


#this will invoke the browser and webdriver is the class in selenium.
#driver = webdriver.Chrome() #webdriver is the class and edge/chrome is the method of webdriver class, it will invoke the edge browser.

driver.get("https://login.salesforce.com/?locale=in")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys('sankarrudrapalsocialmedia@gmail.com')
driver.find_element(By.ID, "password").send_keys('Welcome@1234')
driver.find_element(By.ID, "rememberUn").click()

#Downloading free book from the webpage








time.sleep(2) #time is class, it's execute python library or time is a built-in module, sleep is function often refer to as a method of the time module.





