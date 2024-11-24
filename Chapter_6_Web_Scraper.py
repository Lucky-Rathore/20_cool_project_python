#tricky 
import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.scrapethissite.com/pages/forms/'
response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, 'html.parser')
table_rows = soup.find_all('tr')

data = []
for row in table_rows:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

df = pd.DataFrame(data, columns=['Team Name', 'Year', 'Wins', 'Losses', 'Win %', 'Goals For (GF)', 'Goals Against (GA)', '+ / -'])
df.to_csv('output.csv', index=False)