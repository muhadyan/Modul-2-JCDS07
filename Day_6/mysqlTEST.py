import mysql.connector

db = mysql.connector.connect(
    host = 'localhost',
    port = 3306,
    user = 'Adyan',
    passwd = 'C3ndolbig',
    database = 'ptabc'
)

c = db.cursor()
c.execute('show databases')     # cursornya mau diarahin kemana
print(c.fetchall())             # untuk menampilkan semua nama database


# Ngeliat data
sql = 'select nama from karyawan'
c.execute(sql)
x = c.fetchall()
print(x)

for i in x:
    print(i)


# Masukkin data
sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
val = ('Andi', 15000000)
c.execute(sql, val)
db.commit()
print(c.rowcount, 'Data tersimpan') # buat notif aja


# Masukkin banyak data
sql = 'insert into karyawan (nama, gaji) values (%s, %s)'
val = [('Cici', 15000000), ('Caca', 15000000)]
c.executemany(sql, val)
db.commit()
print(c.rowcount, 'Data tersimpan')