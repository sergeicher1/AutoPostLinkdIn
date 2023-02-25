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
# https://www.jobkarov.com/Search/?speciality=2185&role=2190%2c2191%2c3806%2c2188&area=-2

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from time import *
from datetime import *

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
    action.move_to_element(driver.find_element(By.XPATH,
                                               "//div[@class='ftr']/span[@class='headerfooterlinks']/a[text()='משרות']")).perform()

    driver.find_element(By.XPATH, "//div[@class='ftr']/span[@class='headerfooterlinks']/a[text()='משרות']").click()


def CloseBrowser():
    sleep(3)
    global driver
    driver.quit()


def ChooseField():
    driver.find_element(By.XPATH, "//span[text()=' בחר תחום ']").click()
    driver.find_element(By.XPATH, "//*[@id='WinSelect']/input").send_keys("QA")
    driver.find_element(By.XPATH, "//*[@id='WinSelectIn']/div/label/input").click()
    driver.find_element(By.XPATH, "//*[@id='WinSelect']/div[2]/span[2]").click()


def ChooseJob():
    driver.find_element(By.XPATH, "//*[@id='frmSearch']/div/p[2]/button").click()
    driver.find_element(By.XPATH, "//input[@value='3807']").click()
    driver.find_element(By.XPATH, "//input[@value='2188']").click()
    driver.find_element(By.XPATH, "//input[@value='3806']").click()
    driver.find_element(By.XPATH, "//input[@value='2190']").click()
    driver.find_element(By.XPATH, "//input[@value='2191']").click()
    driver.find_element(By.XPATH, "//*[@id='WinSelect']/div[3]/span[2]").click()


def ChooseLocations():
    driver.find_element(By.XPATH, "//*[@id='frmSearch']/div/p[3]/button").click()
    driver.find_element(By.XPATH, "//input[@value='11']").click()
    driver.find_element(By.XPATH, "//input[@value='30']").click()
    driver.find_element(By.XPATH, "//input[@value='50']").click()
    driver.find_element(By.XPATH, "//input[@value='70']").click()
    driver.find_element(By.XPATH, "//*[@id='WinSelect']/div[3]/span[2]").click()


def ClickSearch():
    driver.find_element(By.XPATH, "//button[@id='search1']").click()


def InfiniteScrollDown():
    # driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    scroll_pause_time = 1  # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")  # get the screen height of the web
    i = 1

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
        i += 1
        sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if screen_height * i > scroll_height:
            break


def ScrollBackToTop():
    driver.execute_script("arguments[0].scrollIntoView();", driver.find_element(By.XPATH, "//*[@id='SearchTabs']/a[3]"))
    driver.execute_script("window.scrollTo(0,-200);")


def SendToAllPositions():
    # send to available positions
    try:
        for i in range(len(send_buttons)):

            # click on "X" to continue
            # FIXME: if text == לא ניתן להתעדכן על המשרה מהשרת
            # FIXME: if text == כבר שלחת קורות חיים היום
            action.move_to_element(send_buttons[i]).perform()
            sleep(1)
            if send_buttons[i].text == "כבר שלחת ב-היום" or send_buttons[i].text == "כבר שלחת ב-אתמול":
                continue
            else:
                send_buttons[i].click()
                sleep(1)

                # Check if there are no errors and input fields are presented
                if len(driver.find_elements(By.XPATH,
                                            "//div[@class='left']/div")) == 1:
                    driver.find_element(By.XPATH, "//span[@class='X']").click()

                # check if salary expectation presented and click the salary range
                if len(driver.find_elements(By.XPATH,
                                            "//div[@class='left']/div")) == 4:
                    action.move_to_element(
                        driver.find_element(By.XPATH, "//select[@name='range']")).click().perform()
                    driver.find_element(By.XPATH, "//option[@value='5']").click()
                    # and click the radio button
                    try:
                        driver.find_element(By.XPATH, "//input[@value='1']").click()
                        driver.find_element(By.XPATH, "//button[@class='GreenButton' and text()='שלח']").click()
                        sleep(1)
                    except Exception as e:
                        print("Exception: ", e)
                        driver.get_screenshot_as_file(
                            "Error" + str(datetime.now().strftime("%d.%m.%y %a %H-%M-%S")) + ".png")
                else:
                    # click the radio button ONLY
                    try:
                        driver.find_element(By.XPATH, "//input[@value='1']").click()
                        driver.find_element(By.XPATH, "//button[@class='GreenButton' and text()='שלח']").click()
                        sleep(1)
                    except Exception as e:
                        print("Exception: ", e)
                        driver.get_screenshot_as_file(
                            "Error" + str(datetime.now().strftime("%d.%m.%y %a %H-%M-%S")) + ".png")
    except Exception as e:
        print("Error: ", e)
        driver.get_screenshot_as_file("Error" + str(datetime.now().strftime("%d.%m.%y %a %H-%M-%S")) + ".png")


#  flow of send CV automation
if __name__ == '__main__':
    try:
        StartBrowser()
        ChooseField()
        ChooseJob()
        ChooseLocations()
        ClickSearch()
        InfiniteScrollDown()
        ScrollBackToTop()

        # Find number of all available positions
        send_buttons = driver.find_elements(By.XPATH, "//a[@class='send ']")
        print(len(send_buttons))
        SendToAllPositions()

        CloseBrowser()
        print("All CV send status is: OK!")
    except Exception as e:
        print("The error is: ", e)
        driver.get_screenshot_as_file("Error" + str(datetime.now().strftime("%d.%m.%y %a %H-%M-%S")) + ".png")

    # TODO: Make video
