import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

service = Service("./chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.themoviedb.org/")

link = driver.current_url
baslik = driver.title
print("page title:" + baslik)

if "https://www.themoviedb.org/" in link: 
    print("True we are on the TMDB")
    print("current title:" + link) 

driver.find_element(By.XPATH, '//*[@aria-label="Giriş"]').click() 
print("giriş butonuna tıklanıldı")

#kullanıcı adı gir
kullaniciadi = driver.find_element(By.ID, 'username') 
kullaniciadi.send_keys("deneme*")
print("username girildi")
#şifre gir
sifregiris = driver.find_element(By.ID, 'password')
sifregiris.send_keys("deneme1234")
print("şifre girildi")
#login düğmesine tıkla
driver.find_element(By.ID, 'login_button').click()
print("hesaba girildi")

time.sleep(5)

# Bir film sayfasına git ve yorum ekleme alanını doldur

button_movie = driver.find_element(By.XPATH, '/html/body/div[1]/header/div[1]/div/div[1]/a/img')
button_movie.click()
print("Anasayfaya gittik")
time.sleep(2)

try:
    movie = driver.find_element(By.XPATH, '//*[@id="trending_scroller"]/div/div[1]/div[1]/div[1]/a/img')
    driver.execute_script("arguments[0].scrollIntoView();", movie)
    movie.click()
    print("İlk filme tıklanıldı")
except Exception as e:
    print("İlk filme tıklanırken bir hata oluştu:", e)


# Discustion butonuna tıkla
discustion = driver.find_element(By.XPATH, '//*[@id="media_v4"]/div/div/div[1]/div/section[2]/section/div[1]/ul/li[2]')
driver.execute_script("arguments[0].scrollIntoView(true);", discustion)
discustion.click()
print("Discustion sayfa butonuna tıklanıldı.")
#Discustion sayfasına geçiş yapmak

time.sleep(3)
go_discustion = driver.find_element(By.XPATH, '//*[@id="media_v4"]/div/div/div[1]/div/section[2]/section/div[2]/div/div/p')
driver.execute_script("arguments[0].scrollIntoView(true);", go_discustion)
go_discustion.click()

discustion_link = driver.current_url

#Discustion sayfasına geçişi kontrol etmek
if "https://www.themoviedb.org/movie/558449-gladiator-ii/discuss" in discustion_link:
    print("Discustion sayfasındayız")

time.sleep(3)

#Yeni yorum oluşturmak
comment_box = driver.find_element(By.XPATH, '//*[@id="new_discussion"]')
comment_box.click()


# Öğeyi bekleyin ve göründüğünden emin olun
subject = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '#new_comment > fieldset > label:nth-child(3) > span.k-input.k-textbox.k-input-solid.k-input-md.k-rounded-md > span'))
)


actions = ActionChains(driver)
actions.move_to_element(subject).click().send_keys('Rating').perform()  
print("subject girildi.")

#driver.switch_to.default_content()


time.sleep(3)
message = driver.find_element(By.XPATH, '//*[@id="message"]') 
driver.execute_script("arguments[0].scrollIntoView(true);", subject)
message.send_keys("")
print("mesaj yazıldı")

time.sleep(4)

try:
    # Engelleyici öğeyi bulun ve gizleyin
    blocking_element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "ot-sdk-row"))
    )
    driver.execute_script("arguments[0].style.display = 'none';", blocking_element)
    print("Engelleyici öğe gizlendi.")
except Exception as e:
    print("Engelleyici öğe bulunamadı veya bir sorun oluştu:", e)

try:
    # Submit butonunu bulun ve tıklayın
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="submit"]'))
    )
    submit_button.click()
    print("Submit butonuna tıklanıldı")
except Exception as e:
    print("Submit butonuna tıklanırken bir hata oluştu:", e)

# Yorumun göründüğünü kontrol et


time.sleep(5)  # Yorumun yüklenmesi için kısa bir bekleme
driver.get("https://www.themoviedb.org/movie/558449-gladiator-ii/discuss/category/5047951f760ee3318900009a")

try:
    # Yorumlar bölümünü bekle
    comments_section = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="discussions"]/table/tbody'))
    )
    
    # "Rating" metninin varlığını doğrula
    assert "Rating" in comments_section.text, "Yorum gönderilemedi!"
    print("Yorum başarıyla gönderildi ve doğrulandı.")
    
    # "Rating" metnini içeren öğeyi bul
    rating_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="discussions"]/table/tbody/tr[1]/td[1]/div/div/div[2]/a'))
    )
    time.sleep(3)
    
    driver.execute_script("arguments[0].click();", rating_element)

    print("Yorumlar başarıyla açıldı.")
except Exception as e:
    print("Yorumlar açılırken bir hata oluştu:", str(e))

# Tarayıcıyı kapat
time.sleep(5)
driver.quit()