import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

event_menu = driver.find_element(By.XPATH, value='//*[@id="content"]/div/section/div[2]/div[2]/div/ul').text
list_of_events = event_menu.split("\n")
dict_of_events:dict = {}
for i in range(0, len(list_of_events), 2):
    dict_of_events[i] = {"date":list_of_events[i],"name":list_of_events[i+1]}
print(dict_of_events)