import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = 'https://resanskrit.com/blogs/blog-post/bhagavad-gita-most-useful-quotes-hindi-english'

# Sending a GET request to the webpage
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Finding all div elements with class "shlok"
shloks = soup.find_all('div', class_='shlok')

# Open a file to write the quotes
with open('quotes.txt', 'w', encoding='utf-8') as file:
    for idx, shlok in enumerate(shloks):
        english_translation = ''
        for p in shlok.find_all('p'):
            if 'English Translation:' in p.text:
                english_translation = p.text.replace('English Translation:', '').strip()
                break
        if english_translation:
            file.write(f'{idx + 1}. {english_translation}\n')


                
print("Quotes successfully written to quotes2.txt!")
