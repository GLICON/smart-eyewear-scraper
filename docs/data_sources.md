# Data sources

Explored on: 31 October 2026, using Chrome Developer Tools (Inspect → Elements).

## FramesDirect.com
- Listing page: https://www.framesdirect.com/eyeglasses/
- About 13,000 eyeglasses, 24 per page.

| What | HTML class | Example |
|---|---|---|
| Product box | `prod-holder` | one box per frame |
| Brand | `catalog-name` | Oakley |
| Model | `product_name` | Airdrop |
| Price you pay | `prod-aslowas` | $227 |
| Original price (on sale items only) | `prod-catalog-retail-price` | $141 |
| Discount | `frame-discount` | 25% off |

- **More products:** numbered pages. Page 2 adds `?p=2` to the address.
- **In the page source?** Yes. The products are already in the HTML the server sends.

## Glasses.com
- Listing page: https://www.glasses.com/gl-us/eyeglasses

| What | HTML class | Example |
|---|---|---|
| Product box | `product-tile` | one box per frame |
| Brand | `product-brand` | Ralph by Ralph Lauren |
| Model | `product-code` | RA7158U |
| Original price | `product-list-price` | $ 141.00 |
| Sale price | `product-offer-price` | $ 105.75 |
| Number of colours | `product-colors` | 4 colors |

- **More products:** a **MORE** button (`load-more-button`) adds more frames to the same page.
- **In the page source?** No. The products are added by JavaScript after the page loads.

## What this means for the scraper
- **Glasses.com needs Selenium:** a real browser has to run the JavaScript before the products exist, and Selenium can click the MORE button.
- **FramesDirect** could be read directly, but using Selenium for both keeps the approach consistent.
- **BeautifulSoup** then reads the finished HTML and pulls out each field using the classes above.
- The two sites write prices differently (`$227` vs `$ 141.00`), so the data will need cleaning.