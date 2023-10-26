from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://qa-mesto.praktikum-services.ru/")

# Find elements
email = driver.find_element(By.ID, "email")
password = driver.find_element(By.ID, "password")

# Check attribute values
assert email.get_attribute('placeholder') == "Email"
assert password.get_attribute('placeholder') == "Пароль"

# Close the browser
driver.quit()