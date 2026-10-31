"""Stage 4: extract product details from the saved FramesDirect page with BeautifulSoup."""
from bs4 import BeautifulSoup

# 1. Read the page saved by scraper.py
with open("data/raw/framesdirect_page1.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")


def get_text(box, class_name):
    """Return the text of the element with this class inside a product box, or '' if missing."""
    element = box.find(class_=class_name)
    return element.get_text(strip=True) if element else ""


# 2. Go through every product box and pull out the fields found in Stage 2
products = []
for box in soup.find_all("div", class_="prod-holder"):
    model = get_text(box, "product_name")
    if not model:
        continue  # this box is a promotional banner, not a product

    products.append({
        "brand": get_text(box, "catalog-name"),
        "model": model,
        "price": get_text(box, "prod-aslowas"),
        "original_price": get_text(box, "prod-catalog-retail-price"),
        "discount": get_text(box, "frame-discount"),
    })

# 3. Show what we found
print("Products found:", len(products))
for product in products[:5]:
    print(product)
    