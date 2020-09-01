import pytest
from time import sleep
import sys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


@pytest.fixure(scope="function")
def capture(request):
    pass


@pytest.fixture(scope='class')
def init_chrome_driver(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close


@pytest.mark.usefixtures(init_chrome_driver)
class BasicChrome:
    pass


class ChromeTests(BasicChrome):
    def test_lambda_todo_app(self):

        self.self.chrome_driver.get('https://lambdatest.github.io/sample-todo-app/')

        self.self.chrome_driver.find_element_by_name('li1').click()
        self.self.chrome_driver.find_element_by_name('li2').click()

        title = "Sample page - lambdatest.com"
        assert title == self.chrome_driver.title

        sample = "this is my todo item"
        send = self.chrome_driver.find_element_by_id("sampletodotext")
        send.send_keys(sample)
        sleep(1)

        add = self.chrome_driver.find_element_by_id("addbutton")
        add.click()
        sleep(1)

        new_todo = self.chrome_driver.find_element_by_xpath("//ul[@class='list-unstyled']/li[@class='ng-scope'][6]/span[@class='done-false']").text
        assert new_todo == sample

        sleep(2)
        self.chrome_driver.close()
