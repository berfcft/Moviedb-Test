import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

# MovieDB web sitesini aç
driver.get("https://www.themoviedb.org")

# Arama kutusunu bekle ve bul
time.sleep(2)
search_box = driver.find_element(By.ID, "inner_search_v4")
search_box.click()

# Arama kutusuna metin yaz ve gönder
search_box.send_keys("Inception")
print("İnput girildi")
search_box.send_keys(Keys.RETURN) # type: ignore
print("Onaylandı")

# Arama sonuçlarını kontrol et
time.sleep(3)  # type: ignore # Sonuçların yüklenmesini bekle
results = driver.find_elements(By.CLASS_NAME, "result") 

assert len(results) > 0, "Arama sonucu bulunamadı!"

driver.quit()
