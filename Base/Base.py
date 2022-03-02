import time, traceback
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Reader import WebReader
from Base.Invoke  import Invoke
class Base(Invoke):




    @Invoke.takesnapshot
    def clickBtn(self):

        #wait=WebDriverWait(self.driver, 10)
        #ele=wait.until(EC.element_to_be_clickable(By.XPATH,Base.closeBtn))
        self.driver.find_element(By.XPATH,WebReader.getlocator("closeBtn")).click()

    @Invoke.takesnapshot
    def searchproduct(self):
        self.driver.find_element(By.XPATH,WebReader.getlocator("searchbar")).send_keys("iphone 12")
        act = ActionChains(self.driver)
        srchele=self.driver.find_element(By.XPATH, WebReader.getlocator("searchicon"))
        act.move_to_element(srchele).click().perform()
        print("Product searched........")



    @Invoke.takesnapshot
    def pricefilter(self):
        min=Select(self.driver.find_element(By.XPATH,WebReader.getlocator("minimum")))
        min.select_by_value("50000")
        max=Select(self.driver.find_element(By.XPATH,WebReader.getlocator("maximum")))
        max.select_by_value("Max")
        print("Pricefilter............")



    @Invoke.takesnapshot
    def fassured(self):

        #self.driver.execute_script('arguments[0].click', Base.fassured)
        wait = WebDriverWait(self.driver,10)
        #wait.until(EC.element_to_be_clickable((By.XPATH,Base.fassure)))
        self.driver.execute_script('arguments[0].click', WebReader.getlocator("fassure"))
        #self.driver.find_element(By.XPATH, Base.fassured).click()
        print("Fassured..............")



    @Invoke.takesnapshot
    def switching_window(self):
        #self.driver.execute_script("arguments[0].scrollIntoView",Base.prod1)
        #self.driver.execute_script("arguments[0].click",Base.prod1)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, WebReader.getlocator("prod"))))
        try:
            time.sleep(5)
            self.driver.find_element(By.XPATH,WebReader.getlocator("prod")).click()
        except ElementClickInterceptedException:
            print("Click exception occured...")
        except:
            print("Unknown exception occured...")
            traceback.print_exc()
        print("clicked for window")
        parent = self.driver.current_window_handle
        print("Parent " + parent)
        child = self.driver.window_handles
        print(child)
        self.driver.switch_to.window(child[1])
        print("switched window..............")



    @Invoke.takesnapshot
    def addingcart(self):
        p=self.driver.find_element(By.XPATH, WebReader.getlocator("price")).text

        s = p.split('₹')
        c = s[1]
        s2 = c.split(',')
        print(s2)
        l = len(s2)
        d = ""
        for x in range(0, l):
            d = d + s2[x]
        i = int(d)
        print("int: ", i)
        assert i > 50000, "price is below 50000"
        print("After assertion")

        print("Price of iphone 12: "+p)
        self.driver.find_element(By.XPATH,WebReader.getlocator("addtocart")).click()
        self.driver.find_element(By.XPATH,WebReader.getlocator("placeorder")).click()
        print("add to cart..............")


    def fullmethod(self):
        self.clickBtn()
        self.searchproduct()
        self.pricefilter()
        self.fassured()
        self.switching_window()
        self.addingcart()