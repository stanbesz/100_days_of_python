import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

number_articles = driver.find_element(By.ID, value="mwDw")

print(f"Number of articles in Wikipedia: {number_articles.text}")

#number_articles.click()
# content_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# content_portals.click()

# driver.implicitly_wait(50) # wait for 5 seconds before closing the browser

search_box = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_box.click()
search_box = driver.find_element(By.NAME, value='search')
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)