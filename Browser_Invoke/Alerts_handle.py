import time

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

driver.find_element(By.CSS_SELECTOR, "#name").send_keys("Sankar")
driver.find_element(By.ID, "alertbtn").click()
'''
handling java or javascript pop-up alert we can not html it. so, driver does not have any knowledge about it.
in this case we have to switch from driver control to alert mode and then we can handle the alert pop-up.
syntax: driver.switch_to.alert. to grab text from alert alert.text it will grab the txt.
'''
alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)
assert "Sankar" in alert_text


time.sleep(2)


