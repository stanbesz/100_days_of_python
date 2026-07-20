import selenium.webdriver as webdriver
from selenium.webdriver.common.by import By


# Keep Chrome browser open after script execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.amazon.com/s?k=gaming&_encoding=UTF8&content-id=amzn1.sym.bd749ccd-05a5-46df-9094-58bcc6398482&pd_rd_r=b05deb72-081c-40a8-836d-3576f14251f0&pd_rd_w=kSmS7&pd_rd_wg=azlul&pf_rd_p=bd749ccd-05a5-46df-9094-58bcc6398482&pf_rd_r=TQFS8WP3W4A3ZK0ZMZFR&ref=pd_hp_d_atf_unk")

price_eur = driver.find_element(By.CLASS_NAME, value="a-price-whole").text
price_cent = driver.find_element(By.CLASS_NAME, value="a-price-fraction").text

print(f"Price: {price_eur}.{price_cent}")
#driver.quit() # close the entire browser
#driver.close() # close a single tab