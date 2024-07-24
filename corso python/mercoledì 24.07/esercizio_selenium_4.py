#Visita https://demoqa.com/dynamic-properties
# Attendi che il bottone "Visible After 5 Seconds" appaia cliccalo e verifica che l'azione sia stata eseguita con successo

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

def dati(driver):
    driver.get("https://demoqa.com/dynamic-properties")
    time.sleep(5)
    pulsante = driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/div[2]/div[2]/button[3]")
    pulsante.click()
    driver.quit()
    print("Pulsante cliccato!")

driver = setup_driver()
dati(driver)
