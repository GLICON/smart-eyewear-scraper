"""Stage 6: scrape Glasses.com, whose products are added by JavaScript."""
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://www.glasses.com/gl-us/eyeglasses"
MORE_CLICKS = 2  # each click adds about 26 frames

os.makedirs("data/raw", exist_ok=True)
driver = webdriver.Chrome()

try:
    driver.get(URL)

    # Wait up to 20 seconds for JavaScript to add the first product tile
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "product-tile")))
    print("Products after page load:", len(driver.find_elements(By.CLASS_NAME, "product-tile")))

    for click in range(1, MORE_CLICKS + 1):
        buttons = driver.find_elements(By.CLASS_NAME, "load-more-button")
        if not buttons:
            print("No MORE button left - all products loaded.")
            break
        # Scroll the button into view, then click it
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", buttons[0])
        time.sleep(1)
        driver.execute_script("arguments[0].click();", buttons[0])
        time.sleep(random.uniform(3, 6))  # wait for new products, and be polite
        print(f"Products after MORE click {click}:",
              len(driver.find_elements(By.CLASS_NAME, "product-tile")))

    with open("data/raw/glasses_page1.html", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Saved to data/raw/glasses_page1.html")
finally:
    driver.quit()