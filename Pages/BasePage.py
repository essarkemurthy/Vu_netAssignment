from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

""" this is the super class for all Pages """

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.implicitly_wait(2)

    def do_click(self, locator):
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(locator)).click()
        except:
            print("not found", locator)

    def do_send_keys(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        # element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).clear()
        # try:
        #     if element:
        #         self.driver.find_element(locator).send_keys(text)
        # except:
        #     print(element, "is not visible")

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(locator))
        return element.text

    def is_visible(self, locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))
        return self.driver.title
