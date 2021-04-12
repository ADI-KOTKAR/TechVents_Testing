from selenium import webdriver
import time 
import unittest
from termcolor import colored
 
class loginCases(unittest.TestCase):
 
    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)
 
    def test_1_Empty_Inputs(self):
        self.browser.get("http://techvents-ip.great-site.net/Login.php")
        login_btn = self.browser.find_element_by_xpath("//input[@name='Submit']")
        login_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Login", self.browser.title)
        print(colored("\u2713 test_1 Passed....OK","green"))
    
    def test_2_Invalid_Credentials(self):
        self.browser.get("http://techvents-ip.great-site.net/Login.php")
        username = self.browser.find_element_by_xpath("//input[@name='Username']")
        username.send_keys("ADITYA")
        password = self.browser.find_element_by_xpath("//input[@name='Password']")
        password.send_keys("98765")
        login_btn = self.browser.find_element_by_xpath("//input[@name='Submit']")
        login_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Login", self.browser.title)
        print(colored("\u2713 test_2 Passed....OK","green"))

    def test_3_Valid_Credentials(self):
        self.browser.get("http://techvents-ip.great-site.net/Login.php")
        username = self.browser.find_element_by_xpath("//input[@name='Username']")
        username.send_keys("ADITYA")
        password = self.browser.find_element_by_xpath("//input[@name='Password']")
        password.send_keys("12345")
        login_btn = self.browser.find_element_by_xpath("//input[@name='Submit']")
        login_btn.click()
        time.sleep(2)
        self.assertIn("TechVents | Admin Dashboard", self.browser.title)
        print(colored("\u2713 test_3 Passed....OK","green"))

if __name__ == '__main__':
    unittest.main(verbosity=2)