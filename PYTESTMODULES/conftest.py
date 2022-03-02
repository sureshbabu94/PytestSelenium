from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pytest, logging,os
from datetime import datetime
from Reader import WebReader
driver = None



#Old_method
@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        #if (report.skipped and xfail) or (report.failed and not xfail):
        if True:
            file_name = report.nodeid.replace("::", "_")+".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)

@pytest.fixture()
def browser():

    s = Service('./Drivers/chromedriver.exe')
    global driver
    driver = webdriver.Chrome(service=s)
    driver.delete_all_cookies()
    driver.get(WebReader.geturl())
    driver.maximize_window()
    driver.implicitly_wait(WebReader.getimplicitwait())
    logging.warning("Browser Opened")
    return driver

@pytest.fixture(scope="module")
def browserclose():
    yield
    driver.quit()
    logging.warning("Browser Closed")