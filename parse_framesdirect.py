"""Stage 5: extract product details from every saved FramesDirect page."""
import glob

from bs4 import BeautifulSoup


def get_text(box, class_name):
    """Return the text of the element with this class inside a product box, or '' if missing."""
    element = box.find(class_=class_name)
    return element.get_text(strip=True) if element else ""


products = []
for path in sorted(glob.glob("data/raw/framesdirect_page*.html")):
    with open(path, encoding="utf-8") as f:
        soup = BeautifulSoup(f.read(), "html.parser")

    for box in soup.find_all("div", class_="prod-holder"):
        model = get_text(box, "product_name")
        if not model:
            continue  # promotional banner, not a product
        products.append({
            "brand": get_text(box, "catalog-name"),
            "model": model,
            "price": get_text(box, "prod-aslowas"),
            "original_price": get_text(box, "prod-catalog-retail-price"),
            "discount": get_text(box, "frame-discount"),
        })
    print(f"{path}: running total {len(products)} products")

print("Total products:", len(products))
for product in products[:3]:
    print(product)