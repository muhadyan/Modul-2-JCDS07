## py -m pip install pymongo                     ==> install pymongo untuk mengkonekan data mongo ke py



import pymongo
dburl = 'mongodb://localhost:27017'
mymongo = pymongo.MongoClient(dburl)

dbs = mymongo.list_database_names()
# print(dbs)
mydb = mymongo['pymongodb']                     # seperti use pymongodb
mycol = mydb['colmong']



## Find data tertentu
alldata = list(mycol.find())
# print(alldata)
alldata = list(mycol.find({'nama': 'Andi'}))
# print(alldata)
alldata = list(mycol.find({'nama': 'Andi'}, {'nama':1}))
# print(alldata)
alldata = list(mycol.find({'usia': {'$gt':24}}, {'nama':1, 'usia':1}))
# print(alldata)

### Cari multiple data
nama = ['Andi', 'Euis', 'Fafa']
# print(list(mycol.find({'nama': {'$in': nama}})))



## Masukin data
### Masukin 1 data
# mydata = {'nama': 'Deni', 'usia': 18, 'kota': 'Kediri'}
# mycol.insert_one(mydata)

### Masukin banyak data
mydata = [
    {'nama': 'Euis', 'usia': 35, 'kota': 'Denpasar'},
    {'nama': 'Fafa', 'usia': 29, 'kota': 'Jakarta'},
    {'nama': 'Gian', 'usia': 22, 'kota': 'Sorong'}
]
# mycol.insanert_my(mydata)



## Ngeliat id-nya data-data yg baru kita masukin
### Jika datanya banyak
# x = mycol.insert_many(mydata)
# print(x.inserted_ids)

### Jika datanya satu dan liat data yg baru dimasukin
# x = mycol.insert_one({'nama': 'Nino'})
# print(x.inserted_id)
# print(list(mycol.find({'_id': x.inserted_id})))



## Delete data
### Delete 1 data
# x = {'nama': 'Fafa'}
# mycol.delete_one(x)

### Delete banyak data
# x = {'nama': 'Gian'}
# mycol.delete_many(x)

### Delete semua data
# mycol.delete_many({})



## Update data
### Update 1 data
# data = {'nama': 'Euis'}
# new = {'nama': 'Gus De'}
# mycol.update_one(data, {'$set': new})

### Update banyak data
# data = {'$and':[
#     {'usia': {'$gt': 25}},
#     {'usia': {'$lt': 30}}
# ]}
# new = {'nama': 'Youngman'}
# mycol.update_many(data, {'$set': new})



import datetime
## Masukin elemen waktu
### Jam lokal laptop kita
# mycol.insert_one({
#     'nama': 'Budi', 'waktu': datetime.datetime.now()
# })

### Jam international
# mycol.insert_one({
#     'nama': 'Deni', 'waktu': datetime.datetime.utcnow()
# })



## Ambil waktunya aja
query = mycol.find({'nama': 'Deni'}, {'waktu':1})
### Ambil waktunya dalam bentuk waktu utc
# print(list(query)[0]['waktu'])
### Ambil waktunya dalam bentuk waktu lokalnya
import pytz
jkt = pytz.timezone('Asia/Jakarta')
# print(jkt.localize(list(query)[0]['waktu']))