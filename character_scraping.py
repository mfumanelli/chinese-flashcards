import requests
from bs4 import BeautifulSoup
import pandas as pd
import yaml

with open(r'config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# create url object
URL = config['character_scraping']['url']


def character_scraping(url=URL):
    # create object page
    page = requests.get(URL)

    # obtain page's information
    soup = BeautifulSoup(page.text, 'lxml')

    table = soup.find('table')

    # create a column list
    headers = []
    for i in table.find_all('th'):
        title = i.text
        headers.append(title)

    # create a dataframe
    data = pd.DataFrame(columns=headers)

    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [i.text for i in row_data]
        length = len(data)
        data.loc[length] = row

    return data
