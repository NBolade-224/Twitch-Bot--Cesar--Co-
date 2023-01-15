from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time, pytesseract, os, asyncio
from PIL import Image

Tesspath = 'C:\\Users\\nickb\\Desktop\\New folder\\PROJECTS\\OCR Tesseract\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = Tesspath

d = DesiredCapabilities.CHROME
d['goog:chromeOptions'] = {'args': ['--window-size=1920,1080']}

# initialise drivers at start (if using 4 screens, intialise 4 etc), then use 'get' for switching stream on each loop. implement two awaits 
async def getStream(streamer):
    driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)
    driver.get('https://www.twitch.tv/%s' % streamer)
    time.sleep(2)
    element = driver.find_elements(By.CLASS_NAME,"eekshR")
    element[4].click()
    driver.save_screenshot('screenie.png')
    img = Image.open('screenie.png')
    img2 = img.crop((1610, 40, 1775, 90)) # (left, top, right, bottom)
    #img2.save('croppedBeach1.png')
    imgcontent = pytesseract.image_to_string(img2)
    img.close()
    img2.close()
    os.remove('screenie.png')
    print(imgcontent)

# async def main():
#     await asyncio.gather(count1('lizzissippi'), count1('wolfabelle'), count1('wolfabelle'), count1('wolfabelle'), count1('wolfabelle'), count1('wolfabelle'), count1('wolfabelle'))

# asyncio.run(main())