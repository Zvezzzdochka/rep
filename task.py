from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Уникальные селекторы для обязательных полей
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input").send_keys("ivan@example.com")

        # Отправка формы
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        # Проверка успешной регистрации
        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Те же селекторы — если поле удалено, тест упадёт
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.first_class input").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.second_class input").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, ".first_block .form-group.third_class input").send_keys("ivan@example.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        time.sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

        browser.quit()

if __name__ == "__main__":
    unittest.main()