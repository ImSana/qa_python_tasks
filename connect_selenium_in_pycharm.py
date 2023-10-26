from selenium import webdriver
import time

# инициализируем драйвер браузера
driver = webdriver.Chrome()
class ChromeOptions:
    chrome_options = webdriver.ChromeOptions()  # создали объект для опций
    chrome_options.add_argument('--headless')  # добавили настройку
    chrome_options.add_argument('--window-size=640,480')  # добавили ещё настройку
    driver = webdriver.Chrome(options=chrome_options)  # создали драйвер и передали в него настройки


# сделаем паузу
time.sleep(5)

# закроем браузер
driver.quit()
