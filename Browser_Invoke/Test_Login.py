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

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME, "name").send_keys('sankar rudrapal')
driver.find_element(By.NAME, "email").send_keys('sankarrudrapalsocialmedia@gmail.com')
driver.find_element(By.ID, "exampleInputPassword1").send_keys('Welcome@1234')
driver.find_element(By.ID, "exampleCheck1").click()
driver.maximize_window()
# //tagname[@attribute='value'] --> Xpath e.g //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text #to get the text of the alert message after clicking on submit button.
print(message)

time.sleep(3)