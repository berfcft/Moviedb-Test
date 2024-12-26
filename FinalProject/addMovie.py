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

#kullanıcı adı gir
kullaniciadi = driver.find_element(By.ID, 'username')

kullaniciadi.send_keys("ladron")
#şifre gir
sifregiris = driver.find_element(By.ID, 'password')

sifregiris.send_keys("test")
#login düğmesine tıkla
driver.find_element(By.ID, 'login_button').click()
time.sleep(2)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[1]/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/ul/li[1]/div/div/div/ul/li[1]').click()
driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div/div/div/div[2]/div[2]/div/section/div/div/div[2]/div[2]/h2/a').click()
driver.find_element(By.XPATH, '/html/body/div[1]/main/section/div[2]/div/div/section/div[2]/section/div[2]/ul/li[3]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div[2]/ul/li[4]/a').click()
driver.find_element(By.XPATH, '/html/body/div[14]/div/div/div[1]/div/div[2]/p[4]').click()
mesaj = driver.find_element(By.XPATH, '/html/body/div[1]/main/div[4]/div/div/div/div[2]/div/div/div[2]/div[1]/div[2]').text

if "Venom: Son Dans (2024), Eddie Brock ve Venom’un hikâyesinin son bölümünü işleyen bir bilim kurgu, aksiyon ve macera filmidir. Bu filmde, Eddie ve simbiyotu Venom, artık bir arada yaşamaya alışmışlardır. Ancak, kendilerini hem dünyalarından hem de başka düşmanlardan kaçmak zorunda kalan birer kaçak olarak bulurlar. Bu durum, Eddie ve Venom’un hayatta kalmak için güçlü bir ortaklık kurmasını gerektirir." in mesaj:
 print("OK. What you are doing is working correctly")
else: 
 print("Error: Correct information works incorrectly")