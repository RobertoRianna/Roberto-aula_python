#Visita https://www.w3schools.com/html/html_tables.asp
#Estrai i dati dalla prima tabella sulla pagina e stampali in formato leggibile

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
    driver.get("https://www.w3schools.com/html/html_tables.asp")
    barra = driver.find_element(By.ID,"accept-choices")
    barra.click()
    tabella = driver.find_element(By.ID,"customers")
    
    print(tabella.text)
    return tabella
    

    

driver = setup_driver()
dati(driver)
