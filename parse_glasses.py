"""Stage 6: extract product details from the saved Glasses.com page."""
from bs4 import BeautifulSoup


def get_text(tile, class_name):
    """Return the text of the element with this class inside a product tile, or '' if missing."""
    element = tile.find(class_=class_name)
    return element.get_text(strip=True) if element else ""


with open("data/raw/glasses_page1.html", encoding="utf-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

products = []
for tile in soup.find_all("a", class_="product-tile"):
    products.append({
        "brand": get_text(tile, "product-brand"),
        "model": get_text(tile, "product-code"),
        "list_price": get_text(tile, "product-list-price"),
        "sale_price": get_text(tile, "product-offer-price"),
        "colours": get_text(tile, "product-colors"),
        "url": tile["href"],
    })

print("Total products:", len(products))
for product in products[:3]:
    print(product)