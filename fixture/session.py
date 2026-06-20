from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()

        wd.find_element(By.NAME, "username").clear()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type='submit']").click()

    def logout(self):
        wd = self.app.wd
        try:
            wd.find_element(By.LINK_TEXT, "Logout").click()
        except NoSuchElementException:
            wd.find_element(By.LINK_TEXT, "Выйти").click()

    def is_logged_in(self):
        wd = self.app.wd
        try:
            wd.find_element(By.CSS_SELECTOR, ".user-info")
            return True
        except NoSuchElementException:
            pass

        try:
            wd.find_element(By.CSS_SELECTOR, "td.login-info-left span")
            return True
        except NoSuchElementException:
            return False

    def is_logged_in_as(self, username):
        return self.get_logged_user() == username

    def get_logged_user(self):
        wd = self.app.wd

        selectors = [
            ".user-info",
            "a.user-info",
            "span.user-info",
            "td.login-info-left span"
        ]

        for selector in selectors:
            try:
                return wd.find_element(By.CSS_SELECTOR, selector).text.strip()
            except NoSuchElementException:
                pass

        return None

    def ensure_logout(self):
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()

        self.login(username, password)