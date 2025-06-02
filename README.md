# IndiaMART Product Scraper 

This project is a web scraping tool developed in Python to extract product data from **IndiaMART B2B marketplace**. It is part of the Slooze Data Engineering Take-Home Challenge.

---

## Features

- Scrapes product listings from 5 selected categories:
  - Generic Medicines
  - Surgical Gloves
  - Flex Printers
  - Drone Camera
  - Dyed Cotton
- Fetches data from the **first 5 pages** of each category
- Extracted fields:
  - Product Name
  - Price
  - Company Name
  - Location
  - Product Description
  - Category
- Stores data in both **CSV** and **JSON** formats

---

## Requirements

- Python 3.x
- Libraries:
  - `requests`
  - `beautifulsoup4`
  - `pandas`

Install required packages:

```bash
pip install requests beautifulsoup4 pandas
