import requests
import csv
from bs4 import BeautifulSoup

def extract_items(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    items = soup.find_all('div', class_='main-products-wrapper') 
    
    extracted_items = []
    for item in items:
        name_tag = item.find('a', class_='caption' + 'a')
        name = name_tag.get_text(strip=True) if name_tag else 'No Name'
        
        price_tag = item.find('span',  class_='price')
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
url = 'https://www.daileisure.co.uk/rifles-and-shotguns/rifles/'  # Replace with the actual URL
items = extract_items(url)

if items:
    save_to_csv(items, 'military_items.csv')
else:
    print("No items were extracted from the webpage.")
