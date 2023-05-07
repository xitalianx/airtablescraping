from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from pyairtable import Airtable
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


API_KEY = 'YOUR_AIRTABLE_API_KEY'
BASE_ID = 'YOUR_AIRTABLE_BASE_ID'
TABLE_NAME = 'YOUR_TABLE_NAME'
COLUMN_1_NAME = 'Titolo'
COLUMN_3_NAME = 'Immagine prodotto'


airtable = Airtable(BASE_ID, TABLE_NAME, api_key=API_KEY)
records = airtable.get_all()
last_row = records[-1]
value = last_row['fields'][COLUMN_1_NAME]

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.google.com/imghp?hl=it")
time.sleep(1)

try:
    accetta = browser.find_element(By.XPATH, "/html/body/div[2]/div[2]/div[3]/span/div/div/div/div[3]/div[1]/button[2]")
    accetta.click()
    time.sleep(1)
except:
    pass    

barra_ricerca = browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
barra_ricerca.send_keys(value)
barra_ricerca.send_keys(Keys.RETURN)
result_img=browser.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img")
result_img.click()
time.sleep(2)
url_img=browser.find_element(By.XPATH, "/html/body/div[2]/c-wiz/div[3]/div[2]/div[3]/div[2]/div/div[2]/div[2]/div[2]/c-wiz/div/div/div/div[3]/div[1]/a/img[1]").get_attribute("src")

browser.quit()

airtable.update(last_row['id'], {COLUMN_3_NAME: url_img})
