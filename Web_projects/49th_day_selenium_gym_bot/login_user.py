from selenium.common.exceptions import TimeoutException
import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from enum import Enum
import os
import time
import datetime

# Login Info
EMAIL_ACCOUNT = "stan.the.man@gmail.com"
ACCOUNT_PASSWORD = "banana"
GYM_URL = "https://appbrewery.github.io/gym/"


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

#C:\Users\stani\Desktop\Python\100_days_of_python\Web_projects\49th_day_selenium_gym_bot\chrome_profile
user_data_dir = os.path.join(os.getcwd(), "chrome_profile") 

# keeps the Chrome profile data stored in the specified directory,
#  allowing you to maintain session data, cookies,
#  and other settings across different runs of your Selenium script.
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")
chrome_options.add_argument("--maximized")  # Start Chrome maximized

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

wait = WebDriverWait(driver, timeout=2)

def login_user():
    # Find the login button and click it
    login_button = driver.find_element(By.ID, "login-button")
    login_button.click()

    # Using built-in wait to ensure the email and password fields are visible before interacting with them
    wait.until(lambda _ : driver.find_element(By.ID, "email-input") and driver.find_element(By.ID, "password-input"))

    email_field = driver.find_element(By.ID, "email-input")
    password_field = driver.find_element(By.ID, "password-input")


    email_field.send_keys(EMAIL_ACCOUNT)
    password_field.send_keys(ACCOUNT_PASSWORD)

    login_submit_user = driver.find_element(By.ID, "submit-button")

    login_submit_user.click()

    # Wait for the schedule page to load after login
    wait.until(expected_conditions.presence_of_element_located((By.ID, "schedule-page")))

    pass