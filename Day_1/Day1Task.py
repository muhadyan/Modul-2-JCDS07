# bisa langsung input ke excel
nama = input('ketik nama: ')
kota = input('ketik kota: ')

listoflist = []
kolom = ['Nama', 'Kota']
listnya = []
data = []

listnya.append(nama)
listnya.append(kota)
listoflist.append(listnya)

# update an save di csv
tambah = open('task.csv', 'a')
for x,y in listoflist:
    tambah.write(x+',')
    tambah.write(y)
    tambah.write('\n')
tambah.close()

# # update di excel
import xlsxwriter
import csv
with open('task.csv', 'r') as x:
    baca = csv.reader(x)
    z = list(baca)
col = list(z[0])
data = list(z[1:])

nulis = xlsxwriter.Workbook('task.xlsx')
sheet = nulis.add_worksheet('Sheet 1')

sheet.write(0, 0, 'No.')
for i in col:
    sheet.write(0, col.index(i)+1, i)

row = 1
for y, z in data:
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    row += 1
row = 1
for i in range(len(data)):
    sheet.write(row, 0, i+1)
    row += 1

nulis.close()