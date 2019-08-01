import pytest
from selenium import webdriver

class TestGoogle:

    driver = webdriver.Chrome()

    def setup_class(cls):
        cls.driver = webdriver.Chrome(
            "./chromedriver")
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get("https://google.com")

    def test_case(self):
        driver = self.driver

        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("hoge")
        driver.find_element_by_css_selector("#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()

    def teardown_class(cls):
        cls.driver.quit()
