import requests
from bs4 import BeautifulSoup
import csv

url = "https://contour-software.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

social_links = []

for link in soup.find_all("a", href=True):
    href = link["href"]
    
    if any(social in href for social in 
           ["facebook.com", "instagram.com", 
            "twitter.com", "linkedin.com", 
            "youtube.com"]):
        social_links.append(href)

print(social_links)

with open('social_links.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Social-Media Links']) 
    for link in social_links:
        writer.writerow([link])

print(f"\nSaved {len(social_links)} links to social_links.csv")



