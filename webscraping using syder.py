from bs4 import BeautifulSoup
import requests
import pandas as pd

#getting the html 
url = "https://www.webometrics.info/en/africa/uganda?sort=desc&order=World%20Rank"
page = requests.get(url)
soup = BeatifulSoup(page.text,'lxml')
soup

#getting the table 

table = soup.find('div':{'class':'sticky-enabled tableheader-processed sticky-table'})

headers = []

for i in table.find_all('th'):
    title = i.text.strip()
    headers.append(title)

df = pd.DataFrame(columns = headers)

for row in table.find_all('tr')[1:]:
    data = row.find_all('td')
    row_data = [td.text.strip() for td in data]
 length = len(def)
df.loc[length] = row_data