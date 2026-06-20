import re
import html
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SignupHelper:

    def __init__(self, app):
        self.app = app

    def new_user(self, username, email, password):
        wd = self.app.wd
        wait = WebDriverWait(wd, 10)

        wd.get(self.app.base_url + "/signup_page.php")

        wait.until(EC.presence_of_element_located((By.NAME, "username"))).send_keys(username)
        wd.find_element(By.NAME, "email").send_keys(email)
        wd.find_element(By.CSS_SELECTOR, 'input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        assert mail is not None, "Не пришло письмо регистрации от Mantis"

        url = self.extract_confirmation_url(mail)
        assert url is not None, "Не удалось найти ссылку подтверждения в письме"

        print("CONFIRMATION URL:", url)

        wd.get(url)

        password_field = wait.until(
            EC.presence_of_element_located((By.NAME, "password"))
        )
        password_field.clear()
        password_field.send_keys(password)

        password_confirm_field = wd.find_element(By.NAME, "password_confirm")
        password_confirm_field.clear()
        password_confirm_field.send_keys(password)

        # Небольшая пауза, чтобы Mantis успел полностью подготовить форму и security token
        time.sleep(1)

        update_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Update User"]'))
        )
        update_button.click()

        wd.find_element(By.LINK_TEXT, "Proceed").click()


    def extract_confirmation_url(self, text):
        match = re.search(r"http://[^\s\"'<]+", text, re.MULTILINE)
        if match is None:
            return None

        return html.unescape(match.group(0))