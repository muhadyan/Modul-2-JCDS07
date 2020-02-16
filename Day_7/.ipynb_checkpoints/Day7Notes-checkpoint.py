import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='Adyan',
    passwd='C3ndolbig',
    database='ptabc'
)
# biar kalo manggil hasilnya dictionary
c = db.cursor(dictionary=True)

# # manggil nama
# query='select * from karyawan'
# c.execute(query)
# out = c.fetchall()
# print(out)

# # manggil namanya doang dan dijadikan list
# print(list(map(lambda x: x[0], out)))

# # input data
# query='insert into karyawan (nama) values (%s)'
# data = ('Andi',)
# c.execute(query, data)
# db.commit()

# # menghapus data
# query='delete from karyawan where nama = (%s)'
# data = ('Andi',)
# c.execute(query, data)
# db.commit()

# # Update data
# query='update karyawan set nama = %s where nama = (%s)'
# data = ('Hani', 'Ani')
# c.execute(query, data)
# db.commit()

# # Update data lebih dari 2 kolom
# query='update karyawan set nama = %s, gaji= %s where id_kar = %s'
# data = ('Zizi', 20000000, 9)
# c.execute(query, data)
# db.commit()

# # tambahin 1 kolom
# query='alter table karyawan add column hobby varchar(255)'
# c.execute(query)
# db.commit()



# JOIN TABLE
## id pengkonek ada di tabel pertama
### Bikin Tabel A
# mysql> create table tabelA(
#     -> id_user int,
#     -> username varchar(255),
#     -> primary key(id_user)
#     -> );

### Bikin Tabel B
# mysql> create table tabelB(
#     -> id_bagian int,
#     -> namaBagian varchar(255)
#     -> );

### Input data Tabel A
# mysql> insert into tabelA values
#     -> (1, 'Andi', 1),
#     -> (2, 'Budi', 1),
#     -> (3, 'Caca', 2),
#     -> (4, 'Deni', 2),
#     -> (5, 'Euis', 1);

### Input data Tabel B
# mysql> insert into tabelB values
#     -> (1, 'Human Resource'),
#     -> (2, 'Marketing'),
#     -> (3, 'Finance'),
#     -> (4, 'Engineer');

### Cross join
# mysql> select username, namaBagian from
#     -> tabelA cross join tabelB;

### Inner join
# mysql> select username, namaBagian from
#     -> tabelA inner join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian;
## atau
# mysql> select username, namaBagian from
#     -> tabelA inner join tabelB
#     -> where tabelA.id_bagian = tabelB.id_bagian;
## atau (jika nama kolomnya sama)
# select username, namaBagian from
#     -> tabelA inner join tabelB
#     -> using (id_bagian);

### Left join
# mysql> select username, namaBagian from
#     -> tabelA left join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian;

### Right join
# mysql> select username, namaBagian from
#     -> tabelA right join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian;

### Left not join
# mysql> select username, namaBagian from
#     -> tabelA left join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian
#     -> where tabelB.namaBagian is null;

### Right not join
# mysql> select username, namaBagian from
#     -> tabelA right join tabelB
#     -> on tabelA.id_bagian = tabelB.id_bagian
#     -> where tabelA.username is null;

### Full outer join
# mysql> select username, namaBagian from
#     -> tabelA left join tabelB
#     -> using (id_bagian)
#     -> union
#     -> select username, namaBagian from
#     -> tabelA right join tabelB
#     -> using (id_bagian);

### Full outer not join
# mysql> select username, namaBagian from
#     -> tabelA left join tabelB
#     -> using (id_bagian)
#     -> where tabelB.namaBagian is null
#     -> union
#     -> select username, namaBagian from
#     -> tabelA right join tabelB
#     -> using (id_bagian)
#     -> where tabelA.username is null;


## Id pengkonek ada di tabel lain
### Bikin tabel AB
# mysql> create table tabelab (
#     -> user_id int,
#     -> bagian_id int);

### Input data tabel AB
# mysql> insert into tabelab values
#     -> (1, 1),
#     -> (2, 2),
#     -> (3, 2),
#     -> (4, 2),
#     -> (5, 3),
#     -> (6, 4);

### Inner join
# mysql> select username, namaBagian from
#     -> tabela inner join tabelab
#     -> on tabela.id_user = tabelab.user_id
#     -> inner join tabelb
#     -> on tabelb.id_bagian = tabelab.bagian_id;
## atau
# mysql> select username, namaBagian from
#     -> tabela a, tabelab ab, tabelb b
#     -> where a.id_user = ab.user_id and b.id_bagian = ab.bagian_id;



# bikin query buat manggil query yg panjang (kayak function)
# mysql> create view kotaidn as
#     -> select city.name as kota, country.name as negara from
#     -> city inner join country
#     -> on city.countrycode = country.code
#     -> where country.code = 'idn';

# manggilnya
# mysql> select * from kotaidn;


# ngeliat semua tables termasuk 'view'
# mysql> show full tables;