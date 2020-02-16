# BIKIN DATABASE DI MYSQL

# mengaktifkan mySQL di terminal                        ==>     mysql -u Adyan -p
# untuk ngeliat ada database apa aja di server kita     ==>     show databases
# cara bikin database                                   ==>     create database tokoOnlineku;
# cara ngecek nama db yg mau dibuat udah ada belum      ==>     create database if not exists tokoOnlineku;
# kalo mau bekerja di sebuah database                   ==>     use tokoOnlineku;
# ngecek sekarang lagi di db mana                       ==>     select database();
# buat ngeliat tabel yg ada di db                       ==>     show tables;
# buat bikin tabel                                      ==>     create table pedagang (no int, nama varchar(5));
# di tabel itu ada apa aja                              ==>     describe pedagang;
# hapus database                                        ==>     drop database tokoOnlineku;
# hapus TABEL                                           ==>     drop table pedagang;
# hapus seluruh data di table                           ==>     delete from pembeli
# ngecek semua isi tabel                                ==>     select * from pedagang;
# masukin data                                          ==>     insert into pedagang values (2, 'Andi');
# masukin data                                          ==>     insert into pedagang (nama) values ('Budi');
# masukin data                                          ==>     insert into pedagang (nama,no) values ('Caca',25);
# masukin beberapa data sekaligus                       ==>     insert into pedagang values(3, 'Dedi'),(6, 'Euis'),(98, 'Fafa');


# create table pembeli(
#     -> no int not null auto_increment,
#     -> nama varchar(100) not null default 'Anonymous Buyer',
#     -> usia tinyint,
#     -> berat float(3,1),
#     -> sex enum('pria', 'wanita'),
#     -> bod date,
#     -> created_at timestamp default current_timestamp,
#     -> primary key (no)
#     -> );


# insert into pembeli (nama, usia, berat, sex, bod) values
#     -> ('Andi',22,77.8,'PRIA','1996-12-29'),
#     -> ('Budi',22,79.8,'WANITA','1995-12-29');