import requests
from bs4 import BeautifulSoup
import csv

page = requests.get("http://www.alloweb.org/annuaire-startups/annuaire-startups-par-marches/annuaire-startups-proptech/")
soup = BeautifulSoup(page.content, 'html.parser')

rows = soup.find_all('div', class_='listing-row')

def generate_row(row):
    company_name = row.find(class_='listing-row-title').get_text()
    link = row.find(class_='listing-row-image-link')['href']
    raw_logo_link = row.find(class_='listing-row-image')['data-bg']
    logo = raw_logo_link.replace('url(','').replace(')','')
    description = row.find(class_='listing-row-content').get_text().strip().replace("/ ","")
    return [company_name, link, logo, description]

with open('companies.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["company_name", "link", "logo","description"])
    for row in rows:
        writer.writerow(generate_row(row))


