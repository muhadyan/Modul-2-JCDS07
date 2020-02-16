import mysql.connector
import requests
from bs4 import BeautifulSoup

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'Adyan',
    passwd = 'C3ndolbig',
    database = 'digimon'
)

c = db.cursor()
# c.execute('describe digi')
# print(c.fetchall())

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

data_tuple = []
for i in listoflist:
    x = tuple(i)
    data_tuple.append(x)

# bikin colom
col = []
th = data.find_all('th')
for i in th:
    col.append(i.text)
col[0] = 'No'
col.insert(2, 'Image')
col[7] = 'Equip_Slots'
col[12] = 'Int_'


sql = 'insert into digi (No, Digimon, Image, Stage, Type, Attribute, Memory, Equip_Slots, HP, SP, Atk, Def, Int_, Spd) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
c.executemany(sql, data_tuple)
db.commit()
print(c.rowcount, 'Data tersimpan')