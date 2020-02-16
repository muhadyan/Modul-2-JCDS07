# Bikin yg bisa ngasih rekomendasi makanan
siapa = input('Nama kamu siapa? : ')
dimana = input(f'{siapa} mau makan dimana? : ')
apaYa = input('Mau makan apa? : ')
import requests

host = 'https://developers.zomato.com/api/v2.1'
kategori2 = f'/locations?query={dimana}'
apiKey = '061df7ab95a0831212d8c2e6dbd273a6'
headInfo = {
    'user-key': apiKey
}
url2 = host + kategori2
data2 = requests.get(url2, headers=headInfo)
kode_kota = data2.json()['location_suggestions'][0]['entity_id']

kategori = f'/search?entity_id={kode_kota}&entity_type=city&q={apaYa}'
url = host + kategori
data = requests.get(url, headers=headInfo)

for i in data.json()['restaurants']:
    print('Nama Resto: ',i['restaurant']['name'])
    print('Alamat: ',i['restaurant']['location']['address'])
    print('Jam buka: ',i['restaurant']['timings'])
    print('Harga makan berdua: ',i['restaurant']['average_cost_for_two'])
    print('')