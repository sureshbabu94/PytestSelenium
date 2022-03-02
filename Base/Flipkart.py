
import time, unittest, HtmlTestRunner,sys, logging, html_test_report,pytest
from Reader import WebReader
from Base import Base
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from datetime import datetime
print(sys.path)
class Flipkart(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        logging.warning("SetUp")
    @classmethod
    def tearDownClass(cls):
        logging.warning("TearDown")

    def setUp(self):
        print("setup")
        self.s = Service('C:/PythonProjects/Drivers/chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.delete_all_cookies()
        self.driver.get(WebReader.geturl())
        self.driver.maximize_window()
        self.driver.implicitly_wait(WebReader.getimplicitwait())
        logging.info("Browser Opened")



    def tearDown(self):
        print("tear down")
        self.driver.close()
        logging.info("Browser Closed")

    def test_third(self):
        print("third test")
        b=Base(self.driver)
        b.fullmethod()



'''
def run_report():
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(log=True, verbosity=2, output='xyz', title='Test report', report_name='yyz',
                           open_in_browser=True, description="HTMLTestReport"))
'''

if __name__=='__main__':
     #unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\PythonProsjects\\Reports"))
     unittest.main(testRunner=HtmlTestRunner.HtmlTestRunner(output="C:\\PythonProjects\\Reports"))