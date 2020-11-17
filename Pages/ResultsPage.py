from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By


class ResultsPage(BasePage):
    """ locators for results page"""
    PERFORMANCE = (By.XPATH, "//div[@class='left-column']//i18n-string[text()='Performance']/../../div[2][@class='score']")
    SEO = (By.XPATH, "//div[@class='left-column']//i18n-string[text()='SEO']/../../div[2][@class='score']")
    MOBILE = (By.XPATH, "//div[@class='left-column']//i18n-string[text()='Mobile']/../../div[2][@class='score']")
    SECURITY = (By.XPATH, "//div[@class='left-column']//i18n-string[text()='Security']/../../div[2][@class='score']")

    def __init__(self, driver):
        super().__init__(driver)

    def get_score(self, locator):
        string = self.get_element_text(locator)
        score = string.split('/')
        score_value = int(score[0]) / int(score[1])
        return round(score_value,2)

    def get_results(self):
        results = {'performance': self.get_score(ResultsPage.PERFORMANCE),
                   'seo': self.get_score(ResultsPage.SEO),
                   'mobile': self.get_score(ResultsPage.MOBILE),
                   'security': self.get_score(ResultsPage.SECURITY)}
        return results

    def validate_score(self, scores_input):
        for key in scores_input.keys():
            if scores_input[key] < 0.7:
                return False
        return True
