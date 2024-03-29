import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class TestGoogle:

    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()

    def setup_method(self):
        self.driver.get("https://google.com")

    def test_case(self):
        driver = self.driver

        driver.save_screenshot("test-reports/images/result_001.png")

        driver.find_element_by_css_selector(
            "#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys("hoge")
        driver.find_element_by_css_selector(
            "#tsf > div:nth-child(2) > div > div.RNNXgb > div > div.a4bIc > input").send_keys(Keys.TAB)

        driver.save_screenshot("test-reports/images/result_002.png")

        driver.find_element_by_css_selector(
            "#tsf > div:nth-child(2) > div > div.FPdoLc.VlcLAe > center > input.gNO89b").click()

        driver.save_screenshot("test-reports/images/result_003.png")

        assert driver.title.count('hoge'), "ページタイトルにhogeが含まれていること"
        assert driver.title.count(
            'foobar'), "ページタイトルにfoobarが含まれていること"  # わざと失敗させる

    def teardown_class(cls):
        cls.driver.quit()
