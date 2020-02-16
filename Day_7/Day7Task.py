# https://github.com/LintangWisesa/Ujian_AnalyticsVisualization_JCDS05

# Soal 1
# select * from city where countrycode = 'IDN' order by population desc limit 10;

# Soal 2
# mysql> select ID, city.name as nama_kota, District, country.name as negara, city.Population as population from
#     -> city inner join country
#     -> on city.countrycode = country.code
#     -> order by population desc
#     -> limit 10;

# Soal 3
# mysql> select code, name, continent, region, indepyear as tahun_merdeka from country
#     -> where indepyear is not null
#     -> order by tahun_merdeka
#     -> limit 10;

# Soal 4
# select continent as benua, count(name) as Jumlah_negara, sum(population) as populasi, avg(lifeexpectancy) as Rata_AngkaHrpnHdp from country group by benua order by populasi desc;

# Soal 5
# mysql> select name as Nama,
#     -> continent as Benua,
#     -> lifeexpectancy as AngkaHarapanHidup,
#     -> GNP from
#     -> country where continent = 'Asia' and lifeexpectancy > (
#     -> select avg(lifeexpectancy) from
#     -> country where continent = 'Europe'
#     -> ) order by lifeexpectancy desc;

# Soal 6
# mysql> select countrycode, name, language, isOfficial, Percentage from
#     -> countrylanguage inner join country
#     -> on countrylanguage.countrycode = country.code
#     -> where language = 'English'
#     -> and isOfficial = 'T'
#     -> order by percentage desc
#     -> limit 10;

# Soal 7
# mysql> select country.name as Negara_ASEAN,
#     -> country.population as Populasi_Negara,
#     -> GNP,
#     -> city.name as Ibukota,
#     -> city.population as Populasi_Ibukota from
#     -> country inner join city
#     -> on country.Capital=city.ID
#     -> where country.name='Brunei'
#     -> or country.name='Cambodia'
#     -> or country.name='East Timor'
#     -> or country.name='Indonesia'
#     -> or country.name='Laos'
#     -> or country.name='Malaysia'
#     -> or country.name='Myanmar'
#     -> or country.name='Philippines'
#     -> or country.name='Singapore'
#     -> or country.name='Thailand'
#     -> or country.name='Vietnam'
#     -> order by Negara_ASEAN
#     -> ;

# Soal 8
# mysql> select country.name as Negara_G20,
#     -> country.population as Populasi_Negara,
#     -> GNP,
#     -> city.name as Ibukota,
#     -> city.population as Populasi_Ibukota from
#     -> country inner join city
#     -> on country.Capital=city.ID
#     -> where country.name='Argentina'
#     -> or country.name='Australia'
#     -> or country.name='Brazil'
#     -> or country.name='Canada'
#     -> or country.name='China'
#     -> or country.name='France'
#     -> or country.name='Germany'
#     -> or country.name='India'
#     -> or country.name='Indonesia'
#     -> or country.name='Japan'
#     -> or country.name='Mexico'
#     -> or country.name='Russian Federation'
#     -> or country.name='Saudi Arabia'
#     -> or country.name='South Africa'
#     -> or country.name='South Korea'
#     -> or country.name='Turkey'
#     -> or country.name='United Kingdom'
#     -> or country.name='United States'
#     -> order by Negara_G20
#     -> ;