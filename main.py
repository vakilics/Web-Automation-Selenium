# Download driver: https://developer.chrome.com/docs/chromedriver/downloads
from ansible_collections.fortinet.fortios.plugins.modules.fortios_registration_forticare import login
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://demoqa.com/login")

# Enter credentials!
username_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'password')))
# can directly click on log in if no other adds!
#logging_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'login')))
# Or if add, then do below:
logging_button = driver.find_element(By.ID, 'login')
#logout_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'logout')))

# Fill credentials anc click login
username_filed.send_keys('hamidva')
password_filed.send_keys('G0admn@demoqa')
#logging_filed.click()
#logout_filed.click()
# Some adds may come faster and may click it! So, we find the argument
driver.execute_script("arguments[0].click();",logging_button)

# Locate elements dropbox
elements = (WebDriverWait(driver, 10).
           until(EC.visibility_of_element_located((By.XPATH,'//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div'))))
elements.click()
text_box = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'item-0')))
text_box.click()

# Locate the form fields and submit burron
fullname_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
current_address_field = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
permanent_address_filed = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))
submit_button = driver.find_element(By.ID, 'submit')

# Filed in form fields
fullname_filed.send_keys('Hamid Vakili')
email_filed.send_keys('vakilitestmail@gmail.com')
current_address_field.send_keys('vessa,32,Germany')
permanent_address_filed.send_keys('vessa,32,Germany')
driver.execute_script("arguments[0].click();", submit_button)

input("Please enter to close browser")
driver.quit()
