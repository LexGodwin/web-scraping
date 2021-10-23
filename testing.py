from bs4 import BeautifulSoup
import requests
import pandas as pd
import  csv

#getting the html 
url = "https://www.webometrics.info/en/africa/uganda?sort=desc&order=World%20Rank"
page = requests.get(url)
soup = BeatifulSoup(page.text,'lxml')
 
table_body = soup.find('table')
row_data = [] #store row info
 
for row in table_body.find_all('tr')
col = row.find_all('td')
col = [ele.text.strip() for ele in col]

row_data.append(col)
row_data

