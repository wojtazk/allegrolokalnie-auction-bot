from selenium import webdriver
import time


options = webdriver.FirefoxOptions()
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

driver.get('https://wojtazk.github.io/')
time.sleep(5)
print('Initialized headless browser')

driver.quit()
