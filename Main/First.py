import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
s=Service('C:/PythonProjects/Drivers/chromedriver.exe')
driver=webdriver.Chrome(service=s)
url=r"https://www.flipkart.com"
driver.get(url)
driver.maximize_window()
driver.implicitly_wait(10)
closeButton="//button[text()='✕']"
driver.find_element(By.XPATH,closeButton).click()
searchbar="//input[@title='Search for products, brands and more']"
driver.find_element(By.XPATH,searchbar).send_keys("iphone 12")
searchicon="//*[@id='container']/div/div[1]/div[1]/div[2]/div[2]/form/div/button"
driver.find_element(By.XPATH,searchicon).click()
minimum="(//select[@class='_2YxCDZ'])[1]"
maximum="(//select[@class='_2YxCDZ'])[2]"
minel=driver.find_element(By.XPATH,minimum)
maxel=driver.find_element(By.XPATH,maximum)
mins=Select(minel)
mins.select_by_value("50000")
maxs=Select(maxel)
maxs.select_by_value("Max")
fassured="(//input[@type='checkbox']//preceding::label)[1]"
#driver.find_element(By.XPATH,fassured).click()

driver.execute_script('arguments[0].click',fassured)
print("fassured")

prod1="//div[text()='APPLE iPhone 12 (Black, 64 GB)']//ancestor::a"
driver.find_element(By.XPATH,prod1).click()
parent=driver.current_window_handle
print("Parent "+parent)
child=driver.window_handles
print(child)
'''
for x in child:
    if (x==parent):
        driver.switch_to_window(x)
        
'''
driver.switch_to.window(child[1])
addtocart="(//span[text()='Add 3 Items to Cart']//ancestor::button)[1]"
driver.find_element(By.XPATH,addtocart).click()
placeorder="//span[text()='Place Order']"
driver.find_element(By.XPATH,placeorder).click()
f="sample"
path="C:/PythonProjects/scr"
os.chdir(path)
NewFolder = 'PBI_' + f
os.makedirs(NewFolder)
driver.save_screenshot(NewFolder+'/foo.png')



