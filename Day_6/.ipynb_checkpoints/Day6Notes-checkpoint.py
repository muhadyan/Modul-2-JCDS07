# mysql> create table karyawan(
#     -> id_kar bigint not null auto_increment,
#     -> nama varchar(5) default 'nonim',
#     -> sex set('pria', 'wanita'),
#     -> gaji int default 5000000,
#     -> created_at timestamp default current_timestamp,
#     -> primary key(id_kar)
#     -> );


# untuk liat sebagian tabel aja                     ==> select gaji, nama from karyawan;
# untuk liat sebagian data di sebagian tabel        ==> select nama from karyawan limit 2;
# untuk liat data setelah urutan ke-2 sebanyak 1    ==> select * from karyawan limit 2,1;
# untuk bikin info tambahan (ga masuk ke tabel)     ==> select nama, gaji, 0.03 * gaji from karyawan;
# info tambahannya diberikan alias                  ==> select nama, gaji, 0.03 * gaji as pot_bpjs from karyawan;
# diurutin berdasarkan nama                         ==> select * from karyawan order by nama;
# diurutin berdasarkan 2 kolom                      ==> select * from karyawan order by nama, created_at;
# diurutin terbalik                                 ==> select * from karyawan order by nama desc;
# buat ngeliat data dengan spesifikasi tertentu     ==> select * from karyawan where nama = 'Anna';
# buat ngeliat data selain spesifikasi tertentu     ==> select * from karyawan where nama != 'Anna';
# buat liat data tertentu dengan range              ==> select * from karyawan where gaji between 4000000 and 8000000;
#                                                   ==> select * from karyawan where gaji > 4000000 and gaji < 8000000;
# buat liat data yg huruf depannya 'a'              ==> select * from karyawan where nama like 'a%';
# buat liat data yg huruf belakangnya 'i'           ==> select * from karyawan where nama like '%i';
# buat liat data yg huruf diantaranya 'i'           ==> select * from karyawan where nama like '%ls%';
# buat ngitung banyaknya data                       ==> select count(*) from karyawan;
# buat ngitung banyaknya data tertentu              ==> select count(*) from karyawan where nama = 'Anna';
#                                                   ==> select count(nama) from karyawan where nama = 'Anna';
# null ga keitung
# nyari value tertinggi data tertentu               ==> select max(gaji) from karyawan;
# nyari value terendah data tertentu                ==> min(gaji) from karyawan;
# nyari total value data tertentu                   ==> select sum(gaji) from karyawan;
# nyari rata2 value data tertentu                   ==> select avg(gaji) from karyawan;

# nyari yg gajinya di bawah rata2                   ==> select * from karyawan where gaji < (select avg(gaji) from karyawan);
# delete data tertentu aja                          ==> delete from karyawan where id_kar = 2;
# edit data tertentu                                ==> update karyawan set nama = 'Ani' where sex = 'wanita';

# edit satu data dua kolom:
# mysql> update karyawan set
#     -> nama = 'Dina', gaji = 7500000
#     -> where id_kar = 4;



# SETIAP UPDATE KOLOM ITU DECLARE 'alter table' DULU

# tambahin kolom saat data sudah terisi:
# mysql> alter table karyawan
#     -> add column
#     -> alamat text;

# delet kolom:
# mysql> alter table karyawan
#     -> drop column alamat;

# update kolom di setelah kolom sex:
# mysql> alter table karyawan
#     -> add column
#     -> alamat text
#     -> after sex;

# mindahin posisi kolom:
# mysql> alter table karyawan
#     -> modify column
#     -> sex set('pria','wanita')
#     -> after gaji;

# rename kolom:
# mysql> alter table karyawan
#     -> rename column
#     -> sex to gender;



# install mySQL connector for python
# py -m pip install MySQL-connector-python