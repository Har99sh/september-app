from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

def login_test():
    username = "test-login"
    password = "test"

    service = Service("C:\SeleniumDrivers\chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    driver.get("http://localhost:8080")
    driver.maximize_window()
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/nav/div/div/ul/li[1]/a").click()
    sleep(2)
    driver.find_element(By.ID, "floatingInput").send_keys(username)
    sleep(3)
    driver.find_element(By.ID, "floatingPassword").send_keys(password)
    sleep(3)
    driver.find_element(By.XPATH, "/html/body/div/div/div/main/div/div/div/div[2]/form/div[3]/button[1]").click()
    sleep(5)

    # falta que dirija a la siguiente página

    print("Login successfull")

    driver.quit()
