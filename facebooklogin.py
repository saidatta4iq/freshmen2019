import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PythonOrgSearch(unittest.TestCase):
    driver = None

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--disable-notifications")
        chrome_options.add_argument("headless")
        caps = chrome_options.to_capabilities()
        self.driver = webdriver.Chrome(
            '/var/lib/jenkins/chromedriver',
            desired_capabilities=caps
        )

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.facebook.com/")
        #self.assertIn("Facebook", driver.title)
        email=driver.find_element_by_id("email")
        paone=driver.find_element_by_name("pass")
        email.send_keys("your user login id here ....")
        paone.send_keys("your password here...")
        paone.send_keys(Keys.RETURN)
        print("Login Successfull")
        elementone=WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="userNavigationLabel"]')))
        logoutbtcss=driver.find_element_by_xpath(
                "//*[@id='userNavigationLabel']"
            )
        logoutbtcss.click()
        time.sleep(5)
        lgbtcss=driver.find_element_by_xpath("/html/body/div[25]/div/div/div/div/div[1]/div/div/ul/li[8]/a/span/span")
        lgbtcss.click()
        print("logout success fully")

    def test_second(self):
        assert 1 == 1

    def test_third(self):
        assert 1 != 2

    def tearDown(self):
        self.driver.quit()
