from selenium import webdriver
import time
import unittest
from termcolor import colored
import random

rand_num = int(time.time())


class registerCases(unittest.TestCase):

    rand_num = int(time.time())

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_1_Empty_Inputs(self):
        self.browser.get("http://techvents-ip.great-site.net/Signup.php")
        signup_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        signup_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Register", self.browser.title)
        print(colored("\u2713 test_1 : Empty Inputs Test Passed \n OK", "green"))

    def test_2_Short_Password(self):
        self.browser.get("http://techvents-ip.great-site.net/Signup.php")
        rand_num = int(time.time())
        username = self.browser.find_element_by_xpath(
            "//input[@name='Username']")
        username.send_keys("TEST_USER_"+str(rand_num))
        password = self.browser.find_element_by_xpath(
            "//input[@name='Password']")
        password.send_keys("987")
        confirm_password = self.browser.find_element_by_xpath(
            "//input[@name='ConfirmPassword']")
        confirm_password.send_keys("987")
        signup_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        signup_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Register", self.browser.title)
        print(colored("\u2713 test_2 : Short Password Test Passed \n OK", "green"))

    def test_3_Invalid_Confirm_Password(self):
        self.browser.get("http://techvents-ip.great-site.net/Signup.php")
        rand_num = int(time.time())
        username = self.browser.find_element_by_xpath(
            "//input[@name='Username']")
        username.send_keys("TEST_USER_"+str(rand_num))
        password = self.browser.find_element_by_xpath(
            "//input[@name='Password']")
        password.send_keys("12345")
        confirm_password = self.browser.find_element_by_xpath(
            "//input[@name='ConfirmPassword']")
        confirm_password.send_keys("98765")
        signup_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        signup_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Register", self.browser.title)
        print(
            colored("\u2713 test_3 : Invalid Confirm Password Test Passed \n OK", "green"))

    def test_4_Valid_Register_Credentials(self):
        self.browser.get("http://techvents-ip.great-site.net/Signup.php")
        username = self.browser.find_element_by_xpath(
            "//input[@name='Username']")
        username.send_keys("TEST_USER_"+str(rand_num))
        password = self.browser.find_element_by_xpath(
            "//input[@name='Password']")
        password.send_keys("12345")
        confirm_password = self.browser.find_element_by_xpath(
            "//input[@name='ConfirmPassword']")
        confirm_password.send_keys("12345")
        signup_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        signup_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Login", self.browser.title)
        print(colored("\u2713 test_4 : Valid Registration Test Passed \n OK", "green"))

    def test_5_Valid_Login_Credentials(self):
        self.browser.get("http://techvents-ip.great-site.net/Login.php")
        username = self.browser.find_element_by_xpath(
            "//input[@name='Username']")
        username.send_keys("TEST_USER_"+str(rand_num))
        password = self.browser.find_element_by_xpath(
            "//input[@name='Password']")
        password.send_keys("12345")
        login_btn = self.browser.find_element_by_xpath(
            "//input[@name='Submit']")
        login_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | User Dashboard", self.browser.title)
        print(colored("\u2713 test_5 : Valid Login Test Passed \n OK", "green"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
