import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.select import Select

# #this way also we can invoke the browser.
# Replace with the actual path to your downloaded msedgedriver.exe
service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
driver = webdriver.Edge(service=service_obj)

# driver.get("https://rahulshettyacademy.com/angularpractice/") #this URL for static dropdown
driver.get("https://rahulshettyacademy.com/dropdownsPractise/") #this URL for dynamic dropdown

driver.maximize_window()
Title = driver.title
print(Title)
#assert "ProtoCommerce" in Title
assert "Flight Booking" in Title

"""
Here we are using static dropdown, in static dropdown we have to use select class of selenium and 
we have to import it from selenium.webdriver.support.ui module.
Select class is used to handle the dropdown in selenium, it will provide us the methods to select the value from the dropdown.
Static dropdown means the dropdown are fixed and we can select the value from the dropdown by using the index number, value or visible text.
Select class is case sensitive.
"""

# dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
# dropdown.select_by_index(1)
# dropdown.select_by_visible_text("Male")
#dropdown.select_by_value() #If the dropdown have value attribute then we can use this method to select the value from the dropdown.


'''
Dynamic dropdown means the dropdown are not fixed and we have to select the value from the dropdown by using the text of the value.
In dynamic dropdown we have to use the click method to select the value from the dropdown,
we have to click on the dropdown and then we have to click on the value from the dropdown.
'''

driver.find_element(By.ID, "autosuggest").send_keys("ind")
time.sleep(3) #we have to wait for few seconds to load and grab the text.
'''
the logic behind selecting option from dynamic dropdown, since there is an auto suggest once after enter "ind" and we have to select the one
specific value but there is an list of option so, first we have taken written common CSS_Selector to grab all the elements 
and using FIND_ELEMENTS method for storing all the option and ITERATING the list using FOR LOOPS.
'''
countries = driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")
print(len(countries)) #to get the count of the option in the dropdown.

# Initialize an empty list to store country names
# list_country = []
#
# for country in countries:
#     country_text = country.text  # Get the text of the country element
#     list_country.append(country_text)  # Add the country name to the list
#     print(country_text)  # Print each country name
#     if country_text == "India":  # Case-insensitive comparison
#         country.click()
#         break
#
# # Now list_country contains all country names
# print(f"All countries: {list_country}")
#
# print(driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value")) #to get the value of the selected option 'india'.

for country in countries:
    if country.text == "India":  # Case-insensitive comparison
         country.click()
         break

'''
when update value dynamically through the script how do we extract the text so, .get_attribute("value") method is used to get the value.
'''
target_value = (driver.find_element(By.CSS_SELECTOR, "#autosuggest").get_attribute("value"))
print(target_value)
assert target_value == "India"