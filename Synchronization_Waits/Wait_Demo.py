import time

from selenium import webdriver #this is for drivers class.
from selenium.webdriver.chrome.service import Service #this is for chrome/edge service class.
from selenium.webdriver.common.by import By

# service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
Title = driver.title
print(Title)
assert "GreenKart" in Title

driver.find_element(By.XPATH, "//input[@type='search']").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)
assert count == 3
#assert count > 0 #if incase future items count is change we validate with this assertion.

'''
chaining methods :

so far results hold 3 elements out gole is to click on add to cart button for all 3 items.
using chaining mechanism we can achieve this.
'''

for result in results:
    result.find_element(By.XPATH, "div/button").click() #this is for click on add to cart button.

driver.find_element(By.XPATH, "//img[@alt='Cart']").click() # this is for click on cart icon.
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()# XPATH using TEXT.
