import time, unittest,sys, logging,pytest,traceback
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base import Base
from Reader import WebReader
from Base import Invoke
#browser =None
'''
@pytest.fixture()
def test_openbrowser():
    s = Service('C:/PythonProjects/browsers/chromebrowser.exe')
    global browser
    browser = webbrowser.Chrome(service=s)
    browser.delete_all_cookies()
    browser.get(WebReader.geturl())
    browser.maximize_window()
    browser.implicitly_wait(WebReader.getimplicitwait())
    logging.info("Browser Opened")
    yield
    print("Browser closed")
    
    browser.close()
    print("Browser closed")
    
    '''
def test_click(browser):
    browser.find_element(By.XPATH, WebReader.getlocator("closeBtn")).click()
    global driver1
    driver1=browser

def test_searchproduct():
    driver1.find_element(By.XPATH,WebReader.getlocator("searchbar")).send_keys("iphone 12")
    act = ActionChains(driver1)
    srchele=driver1.find_element(By.XPATH, WebReader.getlocator("searchicon"))
    act.move_to_element(srchele).click().perform()
    print("Product searched........")
    

def test_pricefilter():
    min=Select(driver1.find_element(By.XPATH,WebReader.getlocator("minimum")))
    min.select_by_value("50000")
    max=Select(driver1.find_element(By.XPATH,WebReader.getlocator("maximum")))
    max.select_by_value("Max")
    print("Pricefilter............")


def test_fassured():

    #self.browser.execute_script('arguments[0].click', Base.fassured)
    wait = WebDriverWait(driver1,10)
    #wait.until(EC.element_to_be_clickable((By.XPATH,Base.fassure)))
    #driver1.execute_script('arguments[0].click', WebReader.getlocator("fassure"))
    driver1.find_element(By.XPATH, WebReader.getlocator("fassure")).click()
    time.sleep(3)
    print("Fassured..............")


def test_switching_window():
    #self.browser.execute_script("arguments[0].scrollIntoView",Base.prod1)
    #self.browser.execute_script("arguments[0].click",Base.prod1)
    WebDriverWait(driver1, 10).until(EC.element_to_be_clickable((By.XPATH, WebReader.getlocator("prod1"))))
    try:
        time.sleep(5)
        driver1.find_element(By.XPATH,WebReader.getlocator("prod1")).click()
    except ElementClickInterceptedException:
        print("Click exception occured...")
    except:
        print("Unknown exception occured...")
        traceback.print_exc()
    print("clicked for window")
    parent = driver1.current_window_handle
    print("Parent " + parent)
    child = driver1.window_handles
    print(child)
    driver1.switch_to.window(child[1])
    print("switched window..............")


def test_addingcart(browserclose):
    p=driver1.find_element(By.XPATH, WebReader.getlocator("price")).text

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
    driver1.find_element(By.XPATH,WebReader.getlocator("addtocart")).click()
    driver1.find_element(By.XPATH,WebReader.getlocator("placeorder")).click()
    print("add to cart..............")

