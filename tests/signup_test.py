from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def signup_test():
    name = "test-login"
    cif = "test"
    email = "test@test"
    telephone = "test"

    service = Service("C:\SeleniumDrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8080")
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/ul/li[2]/a").click()
    sleep(2)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/input[1]").send_keys(name)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/input[2]").send_keys(cif)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/input[3]").send_keys(email)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/input[4]").send_keys(telephone)
    sleep(1)
    driver.find_element(By.XPATH, "/html/body/div/div/div/form/input[8]").click()
    sleep(5)

    # falta que dirija a la siguiente página

    print("Sign Up successfull")

    driver.quit()