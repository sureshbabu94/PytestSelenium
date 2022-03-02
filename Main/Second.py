import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from Fourth import Fourth
from User import User

class Second(unittest.TestCase):
    def setUp(self):
        print("setup")
        self.s = Service('C:/PythonProjects/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.url = r"https://trailblazer.me/trailblazerlogin?&locale=en_US"
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//body/div[2]/div[2]/div[1]/div[1]/div[2]/div[1]/span[1]/div[3]/span[1]/button[1]/img[1]").click()
        self.driver.find_element(By.XPATH,"//input[@id='loginPage:email-card-form:emailTextInput']").send_keys("sureshbabu3126@gmail.com")
        self.driver.find_element(By.XPATH, "//span[contains(text(),'Log In')]").click()
        self.driver.find_element(By.XPATH,"//button[@id='detect_card-login-button']").click()
        self.driver.find_element(By.XPATH,"//a[contains(text(),'Skip for Now')]").click()
        #self.driver.find_element(By.XPATH,"//input[@id='loginPage:email-card-form:challengeTextInput']").send_keys("")
        self.driver.find_element(By.XPATH,"//input[@id='loginPage:email-card-form:verifyChallengeButton']").click()
        self.driver.navigate().to("https://trailhead.salesforce.com/en/today")
        date = datetime.now()
        self.driver.save_screenshot("C:/PythonProjects/scr/" + date + "trailhead.png")

    def tearDown(self):
        print("tear down")
        self.driver.close()

    def test_third(self):
        print("third test")
        #third = Fourth(self.driver)
        #third.clickBtn()
        user=User(self.driver)
        user.handson()
        user.settup()
        user.createuser()


if __name__ == '__main__':
    unittest.main()