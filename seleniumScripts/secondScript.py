
# import the webdriver
from selenium import webdriver
# import the Keys class
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome (executable_path="C:\\Users\\RMS-PI2\\Downloads\\chromedriver.exe")

url="https://www.techlistic.com/p/demo-selenium-practice.html"
driver. get(url)

customer = driver.find_element (by=By.ID, value="customers")
print(customer.text)

tsc_table = driver.find_element(by=By.CLASS_NAME, value="tsc_table_s13")
print(tsc_table.text)

driver.quit()