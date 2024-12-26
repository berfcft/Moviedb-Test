from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.themoviedb.org/")
link = driver.current_url
baslik = driver.title
print("page title:" + baslik)

if "https://www.themoviedb.org/" in link: print("True we are on the TMDB")
print("current title:" + link) 

driver.find_element(By.XPATH, '//*[@aria-label="Giriş"]').click()                                                         
kullaniciadi = driver.find_element(By.ID, 'username')
kullaniciadi.send_keys("deneme")
sifregiris = driver.find_element(By.ID, 'password')
sifregiris.send_keys("test")
driver.find_element(By.ID, 'login_button').click()

wait = WebDriverWait(driver, 10)  # 10 saniye kadar bekler
mesaj_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@class='open no_click']")))
time.sleep(0.5)
mesaj = mesaj_element.text
print(mesaj)
time.sleep(0.5)
print("mesaj:" + mesaj) 
if " There was a problem  " in mesaj:
    print("OK. Wrong username works correctly.")
else:
   print("Error: Wrong username handling is incorrect")