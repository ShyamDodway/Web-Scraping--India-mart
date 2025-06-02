import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
}

# Correct category URLs
urls = {
    'Generic Medicines': 'https://dir.indiamart.com/impcat/generic-medicines.html',
    'Surgical Gloves': 'https://dir.indiamart.com/impcat/surgical-gloves.html',
    'Flex Printers': 'https://dir.indiamart.com/impcat/flex-printers.html',
    'Drone Camera': 'https://dir.indiamart.com/impcat/drone-camera.html',
    'Dyed Cotton': 'https://dir.indiamart.com/impcat/dyed-cotton-fabric.html'
}

all_data = []

# Loop through each category and 5 pages per category
for category, base_url in urls.items():
    print(f"\nScraping category: {category}")
    
    for page in range(1, 6):  # 5 pages per category
        url = f"{base_url}?page={page}"
        print(f"Fetching page: {url}")
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Failed to fetch {url}")
            continue

        soup = BeautifulSoup(response.content, 'html.parser')
        product_blocks = soup.find_all('div', class_='prd-listing')

        for product in product_blocks:
            try:
                name = product.find('a', class_='prd-name').get_text(strip=True)
            except:
                name = None

            try:
                price = product.find('span', class_='prd-price').get_text(strip=True)
            except:
                price = None

            try:
                company = product.find('span', class_='cmpny-name').get_text(strip=True)
            except:
                company = None

            try:
                location = product.find('span', class_='loc').get_text(strip=True)
            except:
                location = None

            try:
                desc = product.find('p', class_='prd-desc').get_text(strip=True)
            except:
                desc = None

            all_data.append({
                'Category': category,
                'Product Name': name,
                'Price': price,
                'Company': company,
                'Location': location,
                'Description': desc
            })

        # Wait between pages
        time.sleep(random.uniform(1.5, 3.0))

# Save data
df = pd.DataFrame(all_data)
df.to_csv('indiamart_products.csv', index=False)
df.to_json('indiamart_products.json', orient='records', indent=2)

print("\n✅ Scraping complete.")
print("Data saved to 'indiamart_products.csv' and 'indiamart_products.json'")
