# pip install xlrd                      ==> untuk install excel
# py -m pip install xlrd                ==> untuk install excel
# py -m pip uninstall NAMA_PACKAGENYA   ==> untuk uninstall excel
# py -m pip list                        ==> untuk liat ada package apa aja di py kita
import xlrd

buka = xlrd.open_workbook('file.xlsx')  # untuk ngebuka file excel
sheet = buka.sheet_by_index(0)          # untuk ngebuka sheet ke berapa
# file.sheet_by_name('NAMANYA')         ==> untuk ngebuka sheet berdasarkan nama sheetnya
print(sheet.nrows, sheet.ncols)         # untuk ngeliat ada berapa row dan colum di sheet tersebut
print(sheet.cell_value(0,2))            # untuk ngeliat di urutan row dan colum tersebut isinya apa

# untuk dapet nama-nama colom atau row di file tersebut
for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))
for i in range(sheet.nrows):
    print(sheet.cell_value(i,1))

# untuk bikin list dari colom atau row di file tersebut
cols = []
for i in range(sheet.ncols):
    cols.append(sheet.cell_value(0,i))
print(cols)
# atau
print(sheet.row_values(0))

# untuk ngelist semua datanya
for i in range(sheet.nrows):
    print(sheet.row_values(i))



# untuk mindahin file dari excel ke json
a = []
for i in range(sheet.nrows):
    a.append(sheet.row_values(i))

import json
with open('file.json', 'w') as x:
    json.dump(a,x)
# atau
out = []
for i in a:
    out.append(dict(zip(a[0], i)))
out = out[1:]
print(out)
with open('file.json', 'w') as x:
    json.dump(out,x)

# untuk mindahin file dari excel ke csv
a = ''
for i in range(sheet.nrows):
    b = sheet.row_values(i)
    for j in b:
        b = str(b)
    a += b + '\n'

import csv
with open('file.csv', 'w') as y:
    y.write(a)
# atau
with open('file.csv', 'w', newline='') as file:
    kolom = list(out[0].keys())
    tulis = csv.DictWriter(file, fieldnames=kolom)
    tulis.writeheader()
    tulis.writerows(out)



# cara nulis ke excel
# py -m pip install xlsxwriter      ==> untuk nginstal package nulis excel
import xlsxwriter
data = xlsxwriter.Workbook('test123.xlsx')  # untuk nulis di file excel yg dituju
sheet = data.add_worksheet('DataKaryawan')  # untuk nulis di sheet di file excel yg dituju

sheet.write(0, 0, 'Nama')   # row, col, data    ==> untuk nulis di row dan kolom tersebut
sheet.write(0, 1, 'Kota')
sheet.write(0, 2, 'Job')

data.close()                # untuk mengakhiri semua fungsi & nutup filenya(karna kalo ga ditutup dulu filenya ga bisa dibuka)



# xlsx => new xlsx
buka = xlrd.open_workbook('file.xlsx')
sheetnya = buka.sheet_by_index(0)

data = xlsxwriter.Workbook('test123.xlsx')
sheet = data.add_worksheet('DataKaryawan')

b = 0
c = 0
for i in range(sheetnya.nrows):
    a = sheetnya.row_values(i)
    for j in a:
        sheet.write(b, c, j)
        c += 1
    c = 0
    b += 1

data.close()

import xlsxwriter
# json => xlsx
import json
with open('file.json', 'r') as x:
    y = json.load(x)
col = list(y[0].keys())
data = []
for i in y:
    data.append(list(i.values()))

nulis = xlsxwriter.Workbook('dataFromJson.xlsx')
sheet = nulis.add_worksheet('SheetA')

for i in col:
    sheet.write(0, col.index(i), i)

row = 1
for x, y, z in data:
    sheet.write(row, 0, x)
    sheet.write(row, 1, y)
    sheet.write(row, 2, z)
    row += 1

# csv => xlsx
import csv
with open('file.csv', 'r') as x:
    baca = csv.reader(x)
    z = list(baca)
col = list(z[0])
data = list(z[1:])

sheet2 = nulis.add_worksheet('SheetB')

for i in col:
    sheet2.write(0, col.index(i), i)

row = 1
for x, y, z in data:
    sheet2.write(row, 0, x)
    sheet2.write(row, 1, y)
    sheet2.write(row, 2, z)
    row += 1

nulis.close()