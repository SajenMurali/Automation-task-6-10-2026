from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://vinothqaacademy.com/demo-site/")

# Wait until First Name field appears
first_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "vfb-5"))
)

first_name.send_keys("Vinoth")

time.sleep(2)
driver.find_element(By.NAME, "vfb-7").send_keys("Babu")
time.sleep(2)
driver.find_element(By.NAME,"vfb-31").click()
time.sleep(1)
driver.find_element(By.NAME,"vfb-20[]").click()
time.sleep(1)
driver.find_element(By.NAME,"vfb-13[address]").send_keys("No 1, Vinoth Street")
time.sleep(1)
driver.find_element(By.NAME,"vfb-13[address-2]").send_keys("BHEL nagar,Bharathi nagar 1st street")
time.sleep(1)
driver.find_element(By.NAME,"vfb-13[zip]").send_keys("Vellore")
time.sleep(2)
driver.find_element(By.NAME,"vfb-14").send_keys("sajen366@gmail.com")
