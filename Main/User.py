from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
class User:
    name="//div/button[contains(text(),'Suresh Babu Rajamanickam')]"
    handsonorg="//a[contains(text(),'Hands-On Orgs')]"
    launch="//a[text()='Launch']"
    setup="//*[@id='75:240;a']"
    create="//span[text()='Create']"
    user="//li[@role='presentation']//descendant::span[text()='User']"
    first_name="//input[@id='name_firstName']"
    last_name="//input[@id='name_lastName']"
    email="//input[@id='Email']"
    user_name="//input[@id='Username']"
    save="(//input[@name='save'])[1]"


    def __init__(self, driver):
        self.driver = driver

    def handson(self):
        self.driver.find_element(User.name).click()
        self.driver.find_element(User.handsonorg).click()
        self.driver.find_element(User.launch).click()
        date=datetime.now()
        self.driver.save_screenshot("C:/PythonProjects/scr/"+date+"handson.png")


    def settup(self):
        self.child = self.driver.window_handles
        self.driver.switch_to.window(self.child[1])
        self.driver.find_element(User.setup).click()
        self.driver.find_element(User.setup).click()
        date = datetime.now()
        self.driver.save_screenshot("C:/PythonProjects/scr/" + date + "settup.png")

    def createuser(self):
        self.child2=self.driver.window_handles
        self.driver.switch_to.window(self.child[2])
        self.driver.find_element(User.create).click()
        self.driver.find_element(User.user).click()
        self.driver.find_element(User.setup).click()
        self.driver.find_element(User.first_name).send_keys("Suresh Babu")
        self.driver.find_element(User.last_name).send_keys("Rajamanickam")
        self.driver.find_element(User.email).send_keys("sureshbabu3126@gmail.com")
        self.driver.find_element(User.user_name).send_keys("sure31261@gmail.com")
        self.driver.find_element(User.save).click()
        date = datetime.now()
        self.driver.save_screenshot("C:/PythonProjects/scr/" + date + "createuser.png")

