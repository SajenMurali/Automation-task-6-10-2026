from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://www.amazon.in/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3F%26tag%3Dgooghydrabk1-21%26ref%3Dnav_signin%26adgrpid%3D155259813593%26hvpone%3D%26hvptwo%3D%26hvadid%3D825671333270%26hvpos%3D%26hvnetw%3Dg%26hvrand%3D17116945361121168631%26hvqmt%3De%26hvdev%3Dc%26hvdvcmdl%3D%26hvlocint%3D%26hvlocphy%3D9152884%26hvtargid%3Dkwd-64107830%26hydadcr%3D14452_2479340%26mcid%3De9c68a2d0f333bcaacd29ec00843c329%26hvocijid%3D17116945361121168631--%26hvexpln%3Dnav%26gad_source%3D1&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
driver.maximize_window()
time.sleep(2)

wait = WebDriverWait(driver, 5)

username = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ap_email_login")
    )
)
username.send_keys("9345954657")
driver.find_element(By.ID, "continue").click()
password = wait.until(
    EC.visibility_of_element_located(
        (By.ID, "ap_password")
    )
)
password.send_keys("sajen@2006")
time.sleep(2)
driver.find_element(By.ID,"signInSubmit").click()
search_box = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "twotabsearchtextbox"))
)

search_box.click()
search_box.send_keys("mouse")
time.sleep(2)
driver.find_element(By.ID,"nav-search-submit-button").click()
time.sleep(2)
driver.find_element(By.NAME,"submit.addToCart").click()


time.sleep(4)
cart = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "nav-cart"))
)

cart.click()

time.sleep(4)