from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time


d = DesiredCapabilities.CHROME
d['goog:chromeOptions'] = {'args': ['--window-size=1920,1080']}

driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)
driver.get('https://www.twitch.tv/shoobytooby')
driver.implicitly_wait(10)
element = driver.find_elements(By.CLASS_NAME,"eekshR")
element[4].click()
time.sleep(10)
driver.save_screenshot('screenie.png')