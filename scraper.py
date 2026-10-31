"""Stage 5: open several FramesDirect listing pages with Selenium, politely."""
import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.framesdirect.com/eyeglasses/?p={page}"
PAGES_TO_SCRAPE = 3

os.makedirs("data/raw", exist_ok=True)
driver = webdriver.Chrome()

try:
    for page in range(1, PAGES_TO_SCRAPE + 1):
        url = BASE_URL.format(page=page)
        print(f"Opening page {page}: {url}")
        driver.get(url)
        time.sleep(5)  # let the page finish loading

        boxes = driver.find_elements(By.CLASS_NAME, "prod-holder")
        print(f"  Product boxes found: {len(boxes)}")
        if not boxes:
            print("  No products on this page - stopping.")
            break

        path = f"data/raw/framesdirect_page{page}.html"
        with open(path, "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print(f"  Saved to {path}")

        # Be polite: wait a random 3-6 seconds before the next page
        pause = random.uniform(3, 6)
        print(f"  Waiting {pause:.1f} seconds...")
        time.sleep(pause)
finally:
    driver.quit()  # always close the browser, even if something goes wrong