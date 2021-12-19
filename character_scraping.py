import requests
from bs4 import BeautifulSoup
import pandas as pd

# Create an URL object
url = 'https://blog.lingodeer.com/chinese-hsk-1-vocabulary-list/'
# Create object page
page = requests.get(url)

# parser-lxml = Change html to Python friendly format
# Obtain page's information
soup = BeautifulSoup(page.text, 'lxml')

table1 = soup.find('table')
print(table1)
