import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

current_cookie_amount = 0
clicks_per_cookie = 0  # Number of clicks per iteration
UPGRADE_THRESHOLD = 3  # Threshold for deciding when to buy an upgrade

# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")  # Start the browser maximized
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://ozh.github.io/cookieclicker/")

time.sleep(2)  # Wait for the page to load

english_lang = driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]')
english_lang.click()
time.sleep(1)  # Wait for the page to load
browser_cookies = driver.find_element(By.CLASS_NAME, value="cc_btn.cc_btn_accept_all")
browser_cookies.click()


time.sleep(1)  # Wait for the page to load
bigCookie = driver.find_element(By.ID, value="bigCookie")
bigCookie.click()



def get_cookie_amount():
    cookie_amount = int(driver.find_element(By.ID, value="cookies").text.split(" ")[0].replace(",",""))
    return cookie_amount


def cookies_per_second():
    #time.sleep(0.01)  # Wait for the page to update
    return float(driver.find_element(By.ID, value="cookies").text.split("\n")[1].split(" ")[-1])

def click_cookie(number_of_clicks):
    global current_cookie_amount, clicks_per_cookie
    for _ in range(number_of_clicks):
        bigCookie.click()
        current_cookie_amount = get_cookie_amount()
        clicks_per_cookie = cookies_per_second()
        upgrade_logic()  # Call the upgrade logic after clicking the cookie

def choose_upgrade(upgrade_list: list):
    # Implement the logic to choose an upgrade based on available cookies
    if len(upgrade_list) == 0:
        print("No upgrades available.")
        return
    elif clicks_per_cookie == 0 and len(upgrade_list) > 0:
        print(f"Items: {upgrade_list[0][0]}")
        print(f"Buying upgrade: {upgrade_list[0][1]} for {upgrade_list[0][2]} cookies.")
        upgrade_list[0][0].click()
        return
    else:
        last_upgrade = upgrade_list[-1]
        penultimate_upgrade = upgrade_list[-2] if len(upgrade_list) > 1 else upgrade_list[-1]
        upgrade_cost_ratio_last = float(current_cookie_amount / last_upgrade[2])
        upgrade_cost_ratio_penultimate = float(current_cookie_amount / penultimate_upgrade[2])
        if current_cookie_amount >= last_upgrade[2]:
            print(f"Buying upgrade: {last_upgrade[1]} for {last_upgrade[2]} cookies.")
            last_upgrade[0].click()
        elif current_cookie_amount >= penultimate_upgrade[2] and upgrade_cost_ratio_penultimate >= UPGRADE_THRESHOLD+UPGRADE_THRESHOLD*clicks_per_cookie:
            print(f"Buying upgrade: {penultimate_upgrade[1]} for {penultimate_upgrade[2]} cookies.")
            penultimate_upgrade[0].click()
        else:
            print("No suitable upgrades available at this time. Waiting for more cookies.")
            print(f"Current cookies: {current_cookie_amount}, Clicks per second: {clicks_per_cookie}, Last upgrade cost: {last_upgrade[2]}, Penultimate upgrade cost: {penultimate_upgrade[2]}, Last upgrade cost ratio: {upgrade_cost_ratio_last}, Penultimate upgrade cost ratio: {upgrade_cost_ratio_penultimate}")
    pass

def upgrade_logic():

    global current_cookie_amount
    # Implement the logic to upgrade items based on available cookies
    products_available = driver.find_elements(By.CLASS_NAME, value="product.unlocked")
    product_map :dict = {}
    product_list_all:list = []
    if len(products_available) == 0:
        pass
    else:
        for product in products_available:
            product_list = product.text.split("\n")
            product_list_all.append([product,product_list[0], int(product_list[1].replace(",",""))])  # Store the product element, name, and cost in a list
            product_map[product_list[0]] = int(product_list[1].replace(",",""))
    
    choose_upgrade(product_list_all)  # Call the choose_upgrade function with the list of available products


def main():
    # Start gameplay loop
    click_cookie(3600)
    time.sleep(1000)  # Wait for the page to load

if __name__ == '__main__':
    main()