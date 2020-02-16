# WEB SCRAPING
# Install beautifulsoup4    --> py -m pip install beautifulsoup4
from bs4 import BeautifulSoup

# SCRAPING from html file
data = BeautifulSoup(open('webScraping.html', 'r'), 'html.parser')     # html parser itu buat ngescrap data dari html

print(data)
print(data.prettify())      # biar tampilannya lebih cantik
print(data.title)           # buat ambil judulnya
print(data.title.name)      # buat ngeliat tag judulnya
print(data.title.text)      # buat ambil text judulnya
# or
print(data.title.string)


print(data.h1)
print(data.h1.name)
print(data.h1.text)
print(data.h1.string)


print(data.li.text)         # hanya yg pertama yg keambil
print(data.ul.text)         # semuanya keambil
print(data.ul.string)       # ga keambil jika isinya banyak (none)

print(data.find_all('li'))  # keluarnya list

for i in data.find_all('li'):
    print(i.text)
# or
ul = data.ul
for i in ul.find_all('li'):
    print(i.text)


print(data.find(class_ = 'orang'))          # buat nyari data di sebuah class (yg keluar yg paling atas)
print(data.find('li', class_ = 'orang'))    # buat nyari data di sebuah tag dengan class tertentu

# ngambil semua data  di tag dan id atau class tertentu
ul = data.ul
for i in ul.find_all('li', class_ = 'orang'):
    print(i.text)
    print(i['id'])
    print(i['class'])



# SCRAPING from url
import requests
web = requests.get('http://127.0.0.1:5500/Day_4/webScraping.html')
print(web.content)      # buat ambil content yg ada di web itu
data = BeautifulSoup(web.content, 'html.parser')
print(data)             # dipercantik

# ngambil semua data  di tag dan id atau class tertentu
ul = data.ul
for i in ul.find_all('li', id = 'person'):
    print(i.text)