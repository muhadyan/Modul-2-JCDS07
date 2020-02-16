# Kurs USD, IDR, Bitcoin
print('Selamat datang')
print('Silahkan pilih konversi yang akan Anda lakukan :')
print(' (1) USD United States => IDR Indonesia')
print(' (2) IDR Indonesia => USD United States')
print(' (3) USD United States => Bitcoin')
print(' (4) IDR Indonesia => Bitcoin')
print(' (5) Bitcoin => USD United States')
print(' (6) Bitcoin => IDR Indonesia')
pilihan = input('Pilihan Anda (1/2/3/4/5/6): ')
nama_bank = input('Silahkan ketik bank pilihan Anda: ')

import requests
url = f'https://kurs.web.id/api/v1/{nama_bank.lower()}'
data = requests.get(url)

url_bc = 'https://blockchain.info/ticker'
data_bc = requests.get(url_bc)

if data.json()['error'] == 'false':
    jual_usd = data.json()['jual']
    beli_usd = data.json()['beli']
    jual_bc = data_bc.json()['USD']['sell']
    beli_bc = data_bc.json()['USD']['buy']
    if pilihan == '1' or pilihan == '2':
        if pilihan == '1':
            kursnya = input('Berapa Dollar uang yang akan dikonversi: ')
            print(f'Hasil konversi $ {kursnya} adalah Rp {int(kursnya) * int(jual_usd)}')
        elif pilihan == '2':
            kursnya = input('Berapa Rupiah uang yang akan dikonversi: ')
            print(f'Hasil konversi Rp {kursnya} adalah $ {round(int(kursnya) / int(jual_usd),2)}')
        print(f'Dengan kurs jual = Rp {jual_usd} & kurs beli = Rp {beli_usd}')
    elif pilihan == '3' or pilihan == '5':
        if pilihan == '3':
            kursnya = input('Berapa Dollar uang yang akan dikonversi: ')
            print(f'Hasil konversi $ {kursnya} adalah {round(int(kursnya) / int(jual_bc),2)} Bitcoin')
        elif pilihan == '5':
            kursnya = input('Berapa Bitcoin uang yang akan dikonversi: ')
            print(f'Hasil konversi {kursnya} Bitcoin adalah $ {round(int(kursnya) * int(jual_bc),2)}')
        print(f'Dengan kurs jual = $ {jual_bc} & kurs beli = $ {beli_bc}')
    elif pilihan == '4' or pilihan == '6':
        if pilihan == '4':
            kursnya = input('Berapa Rupiah uang yang akan dikonversi: ')
            ke_USD = int(kursnya) / int(jual_usd)
            print(f'Hasil konversi Rp {kursnya} adalah {round(ke_USD / int(jual_bc),2)} Bitcoin')
        elif pilihan == '6':
            kursnya = input('Berapa Bitcoin uang yang akan dikonversi: ')
            ke_USD = int(kursnya) * int(jual_usd)
            print(f'Hasil konversi {kursnya} Bitcoin adalah {round(ke_USD * int(jual_bc),2)} Bitcoin')
        print(f'Dengan kurs jual = Rp {int(jual_bc) * int(jual_usd)} & kurs beli = Rp {int(beli_bc) * int(beli_usd)}')
    else:
        print('Pilihan Tidak Ada')
else:
    print('Pilihan Bank Tidak Ada')



# API yg API-Key nya bukan di link (ex: Zomato)
import requests

host = 'https://developers.zomato.com/api/v2.1'
kategori = '/categories'
apiKey = '061df7ab95a0831212d8c2e6dbd273a6'
headInfo = {
    'user-key': apiKey
}

url = host + kategori
data = requests.get(url, headers=headInfo)
print(data.json()['categories'])



# HTML sebagai kerangka
# CSS sebagai Percantik
# Javascript sebagai pembuat behavior