import xlsxwriter

filenya = xlsxwriter.Workbook('z.xlsx')
sheet = filenya.add_worksheet('Data')

sheet.write(0,0,1)
sheet.write(0,0, '=2*2')
sheet.write(0,1, '=A1 + 200')
sheet.write(0,2, '=SUM(A1:B1)')
for i in range(10):
    sheet.write(i+1, 0, i)
filenya.close()

import xlrd

filenya = xlrd.open_workbook('z.xlsx')
sheet = filenya.sheet_by_name('Data')
for i in range(sheet.nrows):
    print(sheet.cell_value(i, 0))



# ambil data dari API
# python GET request => API. Menggunakan package:
# urllib atau requests  ==> py -m pip install requests

import requests

url = 'http://jsonplaceholder.typicode.com/users'
data = requests.get(url)

print(data.json())
print(data.json()['name'])
print(data.json()['address']['street'])

# ngambil hanya sebagian datanya saja
for i in data.json():
    print(i['name'], 'di Jl.', i['address']['street'])



# API SportsDB
klub = input('Ketik nama klub: ')

url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data = requests.get(url)
player = data.json()['player']

if player == None:
    print('Klub Ga Ada Bos')
else:
    for name in player:
        print(f"{name['strPlayer']} ({name['strPosition']})")



# API Quotes
url = 'http://quotes.rest/qod'
data = requests.get(url)
data = data.json()
print(data['contents']['quotes'][0]['quote'])



# API Weather
x = '&appid=49d38e9182ce8bc386109585024c520b'
y = input('Masukkan Kota: ')
url = f'http://api.openweathermap.org/data/2.5/weather?q={y}{x}'
data = requests.get(url)
data = data.json()
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']

from datetime import datetime
waktu = datetime.utcfromtimestamp(int(sunrise))
print(int(waktu.strftime('%d'))+1)
print((int(waktu.strftime('%H'))+7) % 24)
print(f'Cuaca di {y} saat ini adalah',data['weather'][0]['description'])