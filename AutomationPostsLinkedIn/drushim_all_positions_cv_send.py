# ------------------------------------------------------------------------------------------------
# -- coding                                   | utf-8
# -- Author                                   | Sergei Chernyahovsky
# -- Site                                     | http://sergeicher.pro/
# -- Favorite Quote                           | “Always code as if the guy who ends up
#                                                   maintaining your code will be a violent
#                                                       psychopath who knows where you live”
# -- Language                                 | Python
# -- Version                                  | 3.11
# -- WebDriver                                | Selenium
# -- Version                                  | 4.6.0
# -- Description                              | # Automatically sends CV to all available positions #
# ------------------------------------------------------------------------------------------------
# https://www.drushim.co.il/jobs/cat24/?experience=1-2-3&ssaen=3

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from time import *

chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=chrome_options, service=ChromeService(ChromeDriverManager().install()))
action = ActionChains(driver)
driver.implicitly_wait(10)
driver.delete_all_cookies()


def StartBrowser():
    # Login Flow
    driver.get("https://www.jobkarov.com/")
    driver.find_element(By.XPATH, "//span[@class='Link icon-login']").click()
    driver.find_element(By.XPATH, "//input[@name='email']").send_keys("sergeicher87@gmail.com")
    driver.find_element(By.XPATH, "//input[@name='password']").send_keys("Qq1@3456")
    driver.find_element(By.XPATH, "//input[@type='submit']").click()
    driver.find_element(By.LINK_TEXT, "הפצת קו\"ח").click()
    driver.execute_script("scrollTo(0,1000);")


def CloseBrowser():
    global driver
    driver.quit()
# TODO : Implement this

#  flow of send CV automation
if __name__ == '__main__':
    pass