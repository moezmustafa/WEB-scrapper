import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Google Images tab
url = 'https://www.google.com/search?client=firefox-b-d&sca_esv=9fb7e5799ecea4f2&sxsrf=ACQVn0_JNKPuYmox16BcSIjw4Ag_jErnWA:1711304983700&q=pokemon&tbm=isch&source=lnms&prmd=isvnbz&sa=X&ved=2ahUKEwj4hZ_tw42FAxWx_rsIHXXEA_MQ0pQJegQIChAB&biw=1472&bih=791&dpr=2'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image elements
image_elements = soup.find_all('img')

# Create a list to store the data
data = []

# Extract the name and link of each image
for image in image_elements:
    name = image.get('alt', '')
    link = image.get('src', '')
    data.append([name, link])

# Save the data to a CSV file
filename = '/Users/mrmoez/Desktop/WEB scrapper/images.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name', 'Link'])
    writer.writerows(data)

print('Data saved to', filename)