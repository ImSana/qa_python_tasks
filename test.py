from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://ya.ru/")

driver.find_element(By.TAG_NAME, "input").send_keys("Яндекс")
driver.find_element(By.TAG_NAME, "input").clear()
driver.find_element(By.TAG_NAME, "input").send_keys("Практикум")
