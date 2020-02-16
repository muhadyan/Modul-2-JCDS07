from flask import Flask, render_template, jsonify, abort, send_from_directory

server = Flask(__name__)

# home route
@server.route('/')
def home():
    return '<h1>Halo semuanya!</h1>'

# render html
@server.route('/html')
def html():
    return render_template('html.html')

# send data from flask, render html
@server.route('/data')
def data():
    nama = "Andi"
    kota = "Jakarta"
    return render_template(
        'data.html',
        data = {'name': nama, 'city': kota}
        )

employees = [
    {'id':1, 'nama':'Andi', 'usia':20, 'kota':'Jakarta'},
    {'id':2, 'nama':'Budi', 'usia':21, 'kota':'Jakarta'},
    {'id':3, 'nama':'Caca', 'usia':22, 'kota':'Jakarta'},
    {'id':4, 'nama':'Deni', 'usia':23, 'kota':'Jakarta'},
    {'id':5, 'nama':'Euis', 'usia':25, 'kota':'Jakarta'}
]

# route response json
@server.route('/karyawan')
def karyawan():
    return jsonify(employees)

# dynamic route: karyawan/1
@server.route('/karyawan/<int:id>')
def employeez(id):
    if id > len(employees) or id < 1:
        abort(404)
    else:
        return jsonify(employees[id-1])

# route untuk error 404
@server.errorhandler(404)
def notFound(error):
    return render_template('error.html')

# render static file : storage
@server.route('/file/<path:namaFile>')
def myFile(namaFile):
    return send_from_directory('storage', namaFile)

if __name__ == '__main__':
    server.run(
        debug = True,
        host = 'localhost',
        port = 1234
        )