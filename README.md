# 👓 Web Scraping for Smarter Eyewear Choices

A capstone project that uses **Python, Selenium and BeautifulSoup** to collect prescription
eyeglasses from **FramesDirect.com** and **Glasses.com**, so Frame & Lens can compare frames
and prices from both retailers in one place.

🚧 **Work in progress**

## Progress
- [x] Project set-up (virtual environment, requirements)
- [x] Explored both websites ([docs/data_sources.md](docs/data_sources.md))
- [x] FramesDirect: Selenium scraper with pagination and polite pauses
- [x] Glasses.com: Selenium scraper that waits for JavaScript and clicks MORE
- [x] BeautifulSoup parsers for both sites
- [ ] Clean and combine the data
- [ ] Save to CSV and a database
- [ ] Quality checks and results
- [ ] Final write-up

## Files
| File | What it does |
|---|---|
| `scraper.py` | Opens FramesDirect pages 1–3 with Selenium and saves them |
| `scrape_glasses.py` | Opens Glasses.com, waits for products, clicks MORE, saves the page |
| `parse_framesdirect.py` | Extracts brand, model and prices from the saved FramesDirect pages |
| `parse_glasses.py` | Extracts brand, model and prices from the saved Glasses.com page |

## How to run
```bash
python -m venv sec
source sec/bin/activate
pip install -r requirements.txt
python scraper.py
python scrape_glasses.py
python parse_framesdirect.py
python parse_glasses.py
```
