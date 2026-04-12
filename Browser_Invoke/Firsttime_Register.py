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


"""
LINK TEXT OR PARTIAL LINK_TEXT locater is used to locate the link on the webpage, it will locate the link by its text.
Once locate into web page it will start with anchor tag <a> and it will have the text of the link in between the opening and closing anchor tag.
"""
driver.find_element(By.LINK_TEXT, "Register").click() #click on register link_text locater.


