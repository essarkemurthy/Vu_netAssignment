import pytest
from selenium import webdriver
from config.configdata import TestData


@pytest.fixture(scope='class', params=['chrome'])
def init_driver(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.chrome_driver_path)
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path="")
    # if request.param == "Ie":
    #     web_driver = webdriver.Ie(executable_path="")
    request.cls.driver = web_driver
    web_driver.maximize_window()
    # web_driver.implicitly_wait(3)
    yield
    web_driver.close()


