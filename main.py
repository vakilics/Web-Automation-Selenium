# Download driver: https://developer.chrome.com/docs/chromedriver/downloads
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import  Options

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

service = Service("chromedriver-linux64/chromedriver")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://demoqa.com/login")

input("Please enter to close browser")
driver.quit()
