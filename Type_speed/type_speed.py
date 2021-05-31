from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

start_time = time.time()
seconds = 65
PATH = "C:/Program Files (x86)/chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://typing-speed-test.aoeu.eu/?lang=en")
time.sleep(2)

while True:
	current_time = time.time()
	elapsed_time = current_time - start_time
	word = driver.find_element_by_id("currentword").text
	bar =  driver.find_element_by_xpath("//*[@id='input']")
	bar.send_keys(word)
	bar.send_keys(Keys.SPACE)
	if elapsed_time > seconds:
		break


