from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome
options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://practicetestautomation.com/practice-test-login/")

    # Enter username
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    ).send_keys("student")

    # Enter password
    driver.find_element(By.ID, "password").send_keys("Password123")

    # Click Login
    driver.find_element(By.ID, "submit").click()

    # Validate login
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    ).text

    print("Login Test Passed:", success_message)

except Exception as e:
    print("Login Test Failed:", str(e))

finally:
    driver.quit()
