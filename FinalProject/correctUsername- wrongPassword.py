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
kullaniciadi.send_keys("ladron")
sifregiris = driver.find_element(By.ID, 'password')
sifregiris.send_keys("Mediz200sdsd")
driver.find_element(By.ID, 'login_button').click()
mesaj = driver.find_element(By.CLASS_NAME, "content").text
time.sleep(0.5)

mesaj = driver.find_element(By.XPATH, "//*[@class='open no_click']").text



time.sleep(0.5)


if " There was a problem  " in mesaj:
    print("OK. Wrong password works correctly.")
else:
   print("Error: Wrong password handling is incorrect")