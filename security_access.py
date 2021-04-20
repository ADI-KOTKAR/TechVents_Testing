from selenium import webdriver
import time
import unittest
from termcolor import colored


class securityAccess_Tests(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)

    def test_1_Check_Events(self):
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        events_btn = self.browser.find_element_by_xpath(
            "//a[@href='Events.php']")
        events_btn.click()
        time.sleep(2)
        self.assertIn('TechVents | Blog', self.browser.title)
        print(colored("\u2713 test_1 : Event Check Passed \nOK", "green"))

    def test_2_Check_News(self):
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        news_btn = self.browser.find_element_by_xpath("//a[@href='News.php']")
        news_btn.click()
        time.sleep(2)
        self.assertIn('TechVents | Blog', self.browser.title)
        print(colored("\u2713 test_2 : News Check Passed \nOK", "green"))

    def test_3_Check_Blogs(self):
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        blogs_btn = self.browser.find_element_by_xpath(
            "//h3[@class='post-title']")
        blogs_btn.click()
        time.sleep(2)
        self.assertIn('TechVents | Blog', self.browser.title)
        print(colored("\u2713 test_3 : Check Blogs Passed \nOK", "green"))

    def test_4_Check_Category(self):
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        iot_category = self.browser.find_element_by_xpath(
            "//button[@id='Internet of Things']")
        iot_category.click()
        time.sleep(2)
        category_found = self.browser.find_element_by_xpath(
            "//div[@id='display']/button/b").text
        self.assertIn("Internet of Things", category_found)
        print(colored("\u2713 test_4 : Check Category Passed \nOK", "green"))

    def test_5_Search(self):
        self.browser.get("http://techvents-ip.great-site.net/Blog.php")
        search_input = self.browser.find_element_by_xpath(
            "//input[@id='search']")
        search_input.send_keys("blockchain ")
        time.sleep(15)
        output_found = self.browser.find_element_by_xpath(
            "//div[@id='display']/button/b").text
        self.assertIn("blockchain", output_found)
        print(colored("\u2713 test_5 : Search Test Passed \nOK", "green"))


if __name__ == '__main__':
    unittest.main(verbosity=2)
