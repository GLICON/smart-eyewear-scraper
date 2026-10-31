"""Stage 3: open a FramesDirect listing page with Selenium."""
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.framesdirect.com/eyeglasses/"

# 1. Start a Chrome browser that Python can control
driver = webdriver.Chrome()

# 2. Open the listing page and give it time to load
driver.get(URL)
time.sleep(5)

# 3. Check we're on the right page
print("Page title:", driver.title)

# 4. Find every product box using the class found in Stage 2
boxes = driver.find_elements(By.CLASS_NAME, "prod-holder")
print("Product boxes found:", len(boxes))

# 5. Save the page's HTML so we can study it without visiting the site again
os.makedirs("data/raw", exist_ok=True)
with open("data/raw/framesdirect_page1.html", "w", encoding="utf-8") as f:
    f.write(driver.page_source)
print("Saved the page to data/raw/framesdirect_page1.html")

# 6. Close the browser
driver.quit()