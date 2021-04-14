from urllib.request import urlopen 
from bs4 import BeautifulSoup
import pandas as pd 

years = [1994, 1995]
draft_stats = []

for i in range(len(years)):

    url = 'https://www.pro-football-reference.com/years/{}/draft.htm'.format(years[i])
    html = urlopen(url)
    stats = BeautifulSoup(html)

    column_headers = stats.findAll('tr')[1]
    column_headers = [i.getText() for i in column_headers.findAll('th')]

    rows = stats.findAll('tr')[2:]
    
    for i in range(len(rows)):
        draft_stats.append([col.getText() for col in rows[i].findAll(['th','td'])])


df = pd.DataFrame(draft_stats, columns = column_headers)

print(df)