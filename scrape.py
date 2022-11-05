import time
import os
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#tutorial: https://www.scrapingbee.com/blog/selenium-python/

#options = Options()
#options.headless = False
#options.add_argument("--window-size=1920,1200")

driverPath = os.path.abspath('chromedriver.exe')
DRIVER_PATH = driverPath

driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver.get('https://open.spotify.com/playlist/6C9GNbtKzpnqxCZjZ9RtSp')
#driver.find_element(By.CLASS_NAME, 'class="Type__TypeElement-goli3j-0 dlOSsY t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line')
time.sleep(3)

#songs = driver.find_elements(By.CLASS_NAME, "Type__TypeElement-goli3j-0 dlOSsY t_yrXoUO3qGsJS4Y6iXX standalone-ellipsis-one-line")
#print(songs)

# #Specific height (1080 pixel in my monitor)
# driver.execute_script("window.scrollTo(0, 1080);")

# #Bottom of page
# page = driver.find_element_by_xpath('/html')
# driver.execute_script("""arguments[0].scrollTo(0, arguments[0].scrollHeight);""", page)

fileToWrite = open("divs.txt", "w")

bottom_sentinel = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@data-testid='bottom-sentinel']")))
song_list = []
for x in range(10):
    songs = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//div[@data-testid='tracklist-row']")))
    for value in songs:
        song_list.append(value.get_attribute('innerHTML'))
    time.sleep(0.5)
    bottom_sentinel.location_once_scrolled_into_view
    driver.implicitly_wait(15)

songs = driver.find_elements(By.TAG_NAME, 'div')

i = 0
for value in songs:
    fileToWrite.write(value.text)
    print(value.text)
    i = 1 + i
    if(i == 3):
        break
    print(i)
fileToWrite.close()

print("DONE")
driver.quit