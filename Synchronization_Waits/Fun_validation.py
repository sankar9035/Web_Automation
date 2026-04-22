import time

from selenium import webdriver #this is for drivers class.
from selenium.webdriver.chrome.service import Service #this is for chrome/edge service class.
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)

driver = webdriver.Chrome()
driver.implicitly_wait(10)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.maximize_window()
Title = driver.title
print(Title)
assert "GreenKart" in Title

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
count = len(results)
print(count)

assert count > 0
for result in results:
    result.find_element(By.XPATH, "div/button").click()
'''
chaining methods :

so far results hold 3 elements out gole is to click on add to cart button for all 3 items.
using chaining mechanism we can achieve this.
'''

driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
#------------------------------------------------
# Click to process to checkout button
#------------------------------------------------
driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
prices = driver.find_elements(By.CSS_SELECTOR, "tr td:nth-child(5) p") #here we target add to cart item prices.

#--------------------------------------------------------
# Sum Validation
#--------------------------------------------------------

sum = 0
for price in prices:
    sum = sum + int(price.text)

print(sum)
total = int(driver.find_element(By.CSS_SELECTOR, ".totAmt").text)
assert sum == total

#---------------------------------------
#Promocod Apply
#------------------------------------------


#----------------------------------------------
#1. we can apply explicit wait for a specific element which is going to appear after applying the promo code.
#----------------------------------------------
'''
here below line of code going to apply explicit wait since while entering a promo code its take a few min of time,
that might be not initially applicable for all the elements only for a specific element we can apply explicit wait.
So the requirement is once apply a promo_code its will take some time either its a valid code or not,
and text will be appear in the page after applying the promo code, so we have to wait until that text is visible in the page.
'''

driver.find_element(By.CSS_SELECTOR, ".promoCode").send_keys("sankarselenium")
driver.find_element(By.CSS_SELECTOR, ".promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, ".promoInfo")))
promo = driver.find_element(By.CSS_SELECTOR, ".promoInfo").text
print(promo)
assert "Invalid" in driver.find_element(By.CSS_SELECTOR, ".promoInfo").text

discount_price = int(driver.find_element(By.CSS_SELECTOR, ".discountAmt").text)
assert discount_price == total



'''
Here will do a validation before place an order, 
'''
#-------------------------------------------------------
# Price and total both are having a same class attribute and value, so we have to use CSS selector with nth-child to differentiate between them.
#-------------------------------------------------------
#tr td:nth-child(5) p


