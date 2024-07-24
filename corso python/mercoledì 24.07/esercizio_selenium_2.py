#Visita https://practicetestautomation.com/practice-test-login/
# Effettua il login con username "student" e password "Password123"
# Verifica che il login sia avvenuto con successo

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

def setup_driver():
    driver = webdriver.Chrome()
    return driver


def login(driver):
    driver.get("https://practicetestautomation.com/practice-test-login/")

    username = driver.find_element(By.ID, "username")
    username.send_keys("student")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("Password123")

    bottone = driver.find_element(By.ID, "submit")
    bottone.click()
    
    time.sleep(5)
    
    if driver.title == "Logged In Successfully | Practice Test Automation":
        print("Login effettuato")
    else:
        print("Login non riucito")
    
    driver.quit()

    time.sleep(5)

    print("Login avvenuto con seccesso")



driver = setup_driver()
login(driver)