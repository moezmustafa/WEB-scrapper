import requests
from bs4 import BeautifulSoup
import csv

# Send a GET request to the Google Images tab
url = 'https://www.daileisure.co.uk/rifles-and-shotguns/rifles/'
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the image elements
# there is the class named 'name' and inside that is a div with class 'a' that contains the name of the image
text_elements = soup.find_all('div', class_='name')

# Create a list to store the data
data = []

# Extract the name and link of each image
for image in text_elements:
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