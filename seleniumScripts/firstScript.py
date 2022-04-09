from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTest1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome("C:\\Users\\RMS-PI2\\Downloads\\chromedriver.exe")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_test1(self):
        self.driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
        self.driver.set_window_size(1536, 808)
        self.driver.find_element(By.NAME, "firstname").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("Galbie")
        self.driver.find_element(By.NAME, "lastname").click()
        self.driver.find_element(By.NAME, "lastname").send_keys("Elinour")
        self.driver.find_element(By.ID, "sex-1").click()
        self.driver.find_element(By.ID, "exp-2").click()
        self.driver.find_element(By.ID, "datepicker").click()
        self.driver.find_element(By.ID, "datepicker").send_keys("9/4/2022")
        self.driver.find_element(By.ID, "profession-0").click()
        self.driver.find_element(By.ID, "tool-2").click()
        self.driver.find_element(By.ID, "continents").click()
        self.driver.execute_script("window.scrollTo(0,1512.800048828125)")
        dropdown = self.driver.find_element(By.ID, "selenium_commands")
        dropdown.find_element(By.XPATH, "//option[. = 'WebElement Commands']").click()
        self.driver.find_element(By.ID, "submit").click()
