from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-mesto.praktikum-services.ru/")

# Найди поле "Email" и заполни его
driver.find_element(By.ID, "email").send_keys('alexandr_sursyakov_2@yandex.ru')
# Найди поле "Пароль" и заполни его
driver.find_element(By.ID, "password").send_keys('As89169565647')
# Найди кнопку "Войти" и кликни по ней
driver.find_element(By.CLASS_NAME, "auth-form__button").click()
# Добавь явное ожидание для загрузки страницы
WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "header__user")))
# Войти
driver.find_element(By.CLASS_NAME, "profile__image").click()

# Ввести ссылку и войти
driver.find_element(By.ID, "owner-avatar").send_keys('https://code.s3.yandex.net/qa-automation-engineer/python/files/avatarSelenium.png')
# Кликнуть сохранить
driver.find_element(By.CLASS_NAME, "button popup__button").click()

driver.quit()
