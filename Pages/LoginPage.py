from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from utilities.readProperties import ReadConfig


class LoginPage(BasePage):
    website_input_xpath = (By.XPATH, "//input[@data-test-id='url']")
    email_input_xpath = (By.XPATH, "//input[@data-test-id='email']")
    homepage_button_xpath = (By.XPATH, "//button[@data-test-id='homepage-button-submit']")
    acceptCookie = (By.XPATH, "//a[contains(text(),'Accept')]")
    home_icon = (By.XPATH, "(//img[@src='//static.hsappstatic.net/website-grader-ui/static-1.93/img/hubspot-tools-logo.png'])[1]")
    """ constructor for page """

    def __init__(self, driver):
        super().__init__(driver)
        # self.driver.get(TestData.base_url)

    """page action methods"""
    def do_login(self, website, mail_id):
        self.driver.get(ReadConfig.get_application_url())
        self.do_click(self.acceptCookie)
        self.do_send_keys(self.website_input_xpath, website)
        self.do_send_keys(self.email_input_xpath, mail_id)
        self.do_click(self.homepage_button_xpath)
        # self.do_click(self.home_icon)
