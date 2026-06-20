from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.mail import MailHelper
from fixture.signup import SignupHelper
from fixture.soap import SoapHelper



class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.vars = {}
        self.session = SessionHelper(self)
        self.soap = SoapHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.mail = MailHelper(self)
        self.signup = SignupHelper(self)
        self.project = ProjectHelper(self)
        self.base_url = config['web']['base_url']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        # дома поменять обратно
        self.wd.get(self.base_url)
        self.wd.set_window_size(1006, 892)

    def destroy(self):
        self.wd.quit()
