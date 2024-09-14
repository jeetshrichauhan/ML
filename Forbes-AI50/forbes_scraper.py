import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape details from each company's page
def get_company_details(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <dl> blocks
    details = {}
    dl_blocks = soup.find_all('dl', class_='listuser-block__item')
    
    for block in dl_blocks:
        dt = block.find('dt', class_='profile-stats__title')
        dd = block.find('dd', class_='profile-stats__text')
        
        if dt and dd:
            label = dt.get_text(strip=True)
            data = dd.get_text(strip=True)
            details[label] = data
    
    return details

# Load the URLs from the CSV
urls_df = pd.read_csv('company_urls.csv')
urls = urls_df['URL'].tolist()

# Scrape data for each company
all_company_data = []
for url in urls:
    full_url = url if url.startswith('https://') else f'https://www.forbes.com{url}' 
    company_details = get_company_details(full_url)
    all_company_data.append(company_details)

# Convert to DataFrame and save to CSV
company_details_df = pd.DataFrame(all_company_data)
company_details_df.to_csv('company_details.csv', index=False)
print('Company details saved to CSV.')
