import Third
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class Fourth(object):
    #closeBtn="//button[text()='✕']"
    closeBtn = (By.XPATH,"//button[text()='✕']")
    searchbar=(By.XPATH,"//input[@title='Search for products, brands and more']")
    searchicon=(By.XPATH,"//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button")
    minimum=(By.XPATH,"(//select[@class='_2YxCDZ'])[1]")
    maximum=(By.XPATH,"(//select[@class='_2YxCDZ'])[2]")
    fassured=(By.XPATH,"(//input[@type='checkbox']//preceding::label)[1]")
    prod1=(By.XPATH,"//div[text()='APPLE iPhone 12 (Black, 64 GB)']//ancestor::a")
    addtocart=(By.XPATH,"(//span[text()='Add 3 Items to Cart']//ancestor::button)[1]")
    placeorder=(By.XPATH,"//span[text()='Place Order']")

    def __init__(self, driver):
        self.driver = driver

    def clickBtn(self):
        print("Type of Close Btn: ",type(Fourth.closeBtn))
        wait=WebDriverWait(self.driver, 10)
        ele=wait.until(EC.element_to_be_clickable())
        self.driver.find_element(str(Fourth.closeBtn)).click()


    def searchproduct(self):
        self.driver.find_element(Fourth.searchbar).send_keys("iphone 12")
        self.driver.find_element(Fourth.searchicon).click()

    def pricefilter(self):
        min=Select(self.driver.find_element(Fourth.minimum))
        min.select_by_value("50000")
        max=Select(self.driver.find_element(Fourth.maximum))
        max.select_by_value("Max")

    def fassured(self):
        self.driver.execute_script('arguments[0].click', Fourth.fassured)

    def switching_window(self):

        self.driver.find_element(Fourth.prod1).click()
        parent = self.driver.current_window_handle
        print("Parent " + parent)
        child = self.driver.window_handles
        print(child)
        self.driver.switch_to.window(child[1])

    def addtocart(self):
        self.driver.find_element(Fourth.addtocart).click()
        self.driver.find_element(Fourth.placeorder).click()

    def fullmethod(self):
        self.clickBtn()
        self.searchproduct()
        self.pricefilter()
        self.fassured()
        self.switching_window()
        self.addtocart()