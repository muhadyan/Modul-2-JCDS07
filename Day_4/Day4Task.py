# Ambil data Ultraman dan Monster
import requests
from bs4 import BeautifulSoup
web = requests.get('http://www.scifijapan.com/articles/2015/10/04/bandai-ultraman-ultra-500-figure-list/')
data = BeautifulSoup(web.content, 'html.parser')
strong = data.find_all('strong')

ultra = []
for i in strong[2:36]:
    ultra.append(i.text)
monster = []
for i in strong[37:110]:
    monster.append(i.text)
# or
out = []
for i in strong:
    out.append(i.text)
ultra = out[2:36]
monster = out[37:110]



# Ambil data Digimon
web = requests.get('http://digidb.io/digimon-list/')
data = BeautifulSoup(web.content, 'html.parser')

# bikin list of list semua data
listnya = []
listoflist = []
td = data.find_all('td')
for i in td:
    if len(listnya) == 0:
        listnya.append(i.text[1:])
    elif len(listnya) == 1:
        listnya.append(i.text[2:])
    else:
        listnya.append(i.text)
        if len(listnya) == 13:
            listoflist.append(listnya)
            listnya = []

td_img = data.find_all('img')
td_img = td_img[2:-2]
for i in td_img:
    listoflist[td_img.index(i)].insert(2, i['src'])

# bikin colom
col = []
th = data.find_all('th')
for i in th:
    col.append(i.text)
col[0] = 'No'
col.insert(2, 'Image')

# dibikin dict in list. Kemudian di export ke csv
listData = []
for i in listoflist:
    data = dict(zip(col, i))
    listData.append(data)

import csv
with open('Digimon.csv', 'w', newline='') as keCsv:
    a = csv.DictWriter(keCsv, fieldnames=col)
    a.writeheader()
    a.writerows(listData)