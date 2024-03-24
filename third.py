import requests
import csv
from bs4 import BeautifulSoup

def extract_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Find all items with the 'caption' class as they contain the relevant details
    captions = soup.find_all('div', class_='caption')
    
    extracted_items = []
    for caption in captions:
        # Extract the name
        name_tag = caption.find('div', class_='name').find('a')
        name = name_tag.get_text(strip=True) if name_tag else 'No Name'
        
        # First attempt to extract price using the 'price' class
        price_tag = caption.find('span', class_='price')
        
        # If not found, attempt to extract using the 'price-normal' class
        if not price_tag:
            price_tag = caption.find('span', class_='price-normal')
        
        # Extract the price text or indicate 'No Price' if not found
        price = price_tag.get_text(strip=True) if price_tag else 'No Price'
        
        extracted_items.append({'name': name, 'price': price})
    
    return extracted_items

def save_to_csv(items, filename):
    if not items:
        print("No items to save to CSV.")
        return
    
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'price']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for item in items:
            writer.writerow(item)

# Example usage
url = 'https://www.daileisure.co.uk/rifles-and-shotguns/rifles/'  # Replace with the actual URL you are scraping
items = extract_items(url)

if items:
    save_to_csv(items, 'items.csv')
else:
    print("No items were extracted from the webpage.")
