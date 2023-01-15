from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import pytesseract, os, asyncio, requests
from PIL import Image

Tesspath = 'C:\\Users\\nickb\\Desktop\\New folder\\PROJECTS\\OCR Tesseract\\Tesseract-OCR\\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = Tesspath

d = DesiredCapabilities.CHROME
d['goog:chromeOptions'] = {'args': ['--window-size=1920,1080']}


access_token = os.environ['TwitchApiToken']
ses = requests.Session()
hrs = {
'Client-Id':"s7dwe9ds450dsvisqgwue75xl509ps",
'Authorization':'Bearer {}'.format(access_token)
}
Endpoint = "https://api.twitch.tv/helix/streams?game_id=511224&language=en&first=100"
APICall = ses.get(Endpoint,headers=hrs)      
pagi = APICall.json()['pagination']['cursor']
list1 = APICall.json()['data']

for x in range(0,2):
    Endpoint = "https://api.twitch.tv/helix/streams?game_id=511224&language=en&first=100&after=%s" % pagi
    APICall = ses.get(Endpoint,headers=hrs)      
    pagi = APICall.json()['pagination']['cursor']
    list1.extend(APICall.json()['data'])
    ## will produce around the top 1000 streams (sorted by view numbers)

        
# for index, streams in enumerate(list1[::10]):
#     print(str(index)+" "+streams['user_name'])
#     print(streams['viewer_count'])
#     print(streams['is_mature'])
#     print()

async def getStream(asynNumber):
    driver = webdriver.Chrome(ChromeDriverManager().install(),desired_capabilities=d)
    for eachStream in list1[int('%d'%asynNumber)::5]:
        if eachStream['is_mature'] == True:
            continue
        driver.get('https://www.twitch.tv/%s' % eachStream['user_name'])
        await asyncio.sleep(5)
        try:
            element = driver.find_elements(By.CLASS_NAME,"eekshR")
            element[4].click()
            driver.save_screenshot('%s.png' % eachStream['user_name'])
            img = Image.open('%s.png' % eachStream['user_name'])
            img2 = img.crop((1610, 40, 1775, 90)) # (left, top, right, bottom)
            img2.save('%s 2.png' % eachStream['user_name'])
            imgcontent = pytesseract.image_to_string(img2)
            img.close()
            img2.close()
            os.remove('%s.png' % eachStream['user_name'])
            print(eachStream['user_name'])
            print(imgcontent)
            print()
        except:
            continue
    
async def main():
    await asyncio.gather(getStream(0), getStream(1), getStream(2), getStream(3), getStream(4))

asyncio.run(main())