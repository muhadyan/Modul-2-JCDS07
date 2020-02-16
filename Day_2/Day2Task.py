# get api sportsdb, daftar pemain suatu klub
# input: klub apa?
# daftar pemain: nama, posisi, usia, negara
# save di excel, json, csv

import requests

klub = input('Ketik nama klub: ')

url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data = requests.get(url)
player = data.json()['player']

listnya = []
listoflist = []
from datetime import datetime as dt
x = dt.now()
tahun = x.strftime('%Y')

if player == None:
    print('Klub Ga Ada Pak hehe')
else:
    for i in player:
        nama = i['strPlayer']
        posisi = i['strPosition']
        umur = i['dateBorn']
        umur = int(tahun) - int(umur[:4])
        negara = i['strNationality']
        listnya.append(nama)
        listnya.append(posisi)
        listnya.append(umur)
        listnya.append(negara)
        listoflist.append(listnya)
        listnya = []

col = ['Nama', 'Posisi', 'Umur', 'Negara']


# Export ke Excel
import xlsxwriter
nulis = xlsxwriter.Workbook('Pemain_Bola.xlsx')
sheet = nulis.add_worksheet('Sheet 1')

sheet.write(0, 0, 'No.')
for i in col:
    sheet.write(0, col.index(i)+1, i)

row = 1
for w, x, y, z in listoflist:
    sheet.write(row, 1, w)
    sheet.write(row, 2, x)
    sheet.write(row, 3, y)
    sheet.write(row, 4, z)
    row += 1
row = 1
for i in range(len(listoflist)):
    sheet.write(row, 0, i+1)
    row += 1

nulis.close()


# Export ke json
import json
listData = []
for i in listoflist:
    data = dict(zip(col, i))
    listData.append(data)

with open('Pemain_Bola.json', 'w') as keJson:
    json.dump(listData, keJson)


# Export ke csv
import csv
with open('Pemain_Bola.csv', 'w', newline='') as keCsv:
    a = csv.DictWriter(keCsv, fieldnames=col)
    a.writeheader()
    a.writerows(listData)