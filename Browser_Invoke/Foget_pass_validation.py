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
assert "Shop" in Title

driver.find_element(By.LINK_TEXT, "Forgot password?").click() #click on forgot password link_text locater.

'''
There will be an another approach writting  Xpath and css selector patrent to child traversing.
Xpath syntax: //parenttag/childtag e.g //form/div[1]/input
CSS_Selector syntax: parenttag childtag e.g form div:nth-child(2) input
'''
#parent to child traversing in Xpath and css selector.
driver.find_element(By.XPATH, "//form/div[1]/input").send_keys("demo@gmail.com") #Email box
driver.find_element(By.CSS_SELECTOR, "form div:nth-child(2) input").send_keys("Welcome@1234") #Password box
driver.find_element(By.CSS_SELECTOR, "#confirmPassword").send_keys("Welcome@1234") #Confirm password box

#if there is nothing present in web page only test is present using text only we can create XPATH that facility not present in CSS_Selector.
#//tagname[text()='text of the element'] e.g below
#//button[text()='Save New Password'] --> Xpath syntax for button with text "Save New Password"




time.sleep(3)

driver.quit()
