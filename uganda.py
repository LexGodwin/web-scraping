from bs4 import BeautifulSoup
import  requests
from csv import writer

url ="https://www.webometrics.info/en/africa/uganda?sort=desc&order=World%20Rank"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')
list = soup.find_all('tr',class_="even")

with open('rankingsforuniversitiesinuganda.csv','w',encoding='utf8',newline='') as f:
        thewriter = writer(f)
        header = ['university','ranking','worldrank','det','impactrank','opennessrank','excellencerank']
        thewriter.writerow(header)
         
for list in lists:
        ranking = list.find('center', class_="1").text
        worldrank = list.find('center', class_="29751").text
        university = list.find('a', class_="https://www.mityanagrovetinstitute.com/").text.replace('\n ', '')
        det = list.find('a', class_="/en/detalles/mityanagrovetinstitute.com").text.replace('\n ', '')
        impactrank = list.find('center', class_="29737").text.replace('\n ', '')
        opennessrank = list.find('center', class_="6492").text.replace('\n ', '')
        excellencerank = list.find('center', class_="665").text.replace('\n ', '')

        info = [university,ranking,worldrank,det,impactrank,opennessrank,excellencerank ]
        print(info)
        thewriter.writerow(info)