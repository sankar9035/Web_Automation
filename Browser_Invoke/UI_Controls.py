from selenium import webdriver #this is for drivers class.
from selenium.webdriver.chrome.service import Service #this is for chrome/edge service class.
from selenium.webdriver.common.by import By

# service_obj = Service(executable_path=r'C:\Users\sanka\Downloads\edgedriver_win64\msedgedriver.exe')
# driver = webdriver.Edge(service=service_obj)

driver = webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.maximize_window()
Title = driver.title
print(Title)
assert "Practice" in Title

Checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

for checkbox in Checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() == True
        break

#Here also we can create a CSS_Selector using class nake e.g .radioButton .
Radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")


for radio in Radio_buttons:
    if radio.get_attribute("value") == "radio3":
        radio.click()
        assert radio.is_selected() == True
        break


#Now we gonna performing is_display() method to check element is visible or not for user.
assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()