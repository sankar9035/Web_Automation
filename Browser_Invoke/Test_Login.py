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
Title = driver.title
print(Title)

driver.find_element(By.NAME, "email").send_keys('sankarrudrapalsocialmedia@gmail.com')#email box
driver.find_element(By.ID, "exampleInputPassword1").send_keys('Welcome@1234') #password box
driver.find_element(By.ID, "exampleCheck1").click() # Check me out if you Love IceCreams! checkbox
driver.maximize_window()
# //tagname[@attribute='value'] --> syntax Xpath e.g //input[@type='submit']
driver.find_element(By.XPATH, "//input[@type='submit']").click() #submit button
#syntax CSS_Selector-->tagname[attribute='value'] e.g "input[name='name']"
# another method of CSS_Selector-->tag name#id or #id e.g input#inlineRadio2
# another method of CSS_Selector-->tag name.class or .class e.g input.form-check-input

#another way of Xpath and CSS_Selector is by using the index number.
# below code will find the 3rd input box of type text and send the value to it and it will add the value of first box.
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys('welcome to selenium_automation ')

driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys('sankar rudrapal') #name box
#we are clearing the value of the 3rd input box of type text and it will clear the value of first box value as well.
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
driver.find_element(By.XPATH, "//input[@id='inlineRadio1']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text #to get the text of the alert message after clicking on submit button.
print(message)


#Required test case have assertion for a validation of the test case, here we are validating the alert message after clicking on submit button.

assert "Success" in message #if the message contains the word "Success" then the test case will be passed otherwise it will be failed.

time.sleep(3)