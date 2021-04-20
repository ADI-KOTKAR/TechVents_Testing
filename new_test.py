from selenium import webdriver
import time
import unittest
from termcolor import colored


class NewTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_1_Login_and_Access(self):
        self.browser.get("http://techvents-ip.great-site.net/Login.php")
        username = self.browser.find_element_by_xpath(
            "//input[@name='Username']")
        username.send_keys("ADITYA")
        password = self.browser.find_element_by_xpath(
            "//input[@name='Password']")
        password.send_keys("12345")
        login_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        login_btn.click()
        time.sleep(3)
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        events_btn = self.browser.find_element_by_xpath(
            "//a[@href='Events.php']")
        events_btn.click()
        time.sleep(4)
        self.assertIn('TechVents | Events', self.browser.title)
        print(colored("\u2713 test_1 : Event Check Passed \nOK", "green"))
        # self.assertIn("TechVents | Blog", self.browser.title)
        # print(colored("\u2713 test_4 : Valid Registration Test Passed \n OK", "green"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
