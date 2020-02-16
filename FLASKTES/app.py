from flask import Flask, render_template, jsonify, redirect, request

app = Flask(__name__)

@app.route('/')
def beranda():
    return render_template('home.html')


x = [
    {'no':1, 'nama': 'Andi'},
    {'no':2, 'nama': 'Budi'},
    {'no':3, 'nama': 'Caca'}
]

@app.route('/data')
def data():
    return jsonify(x)

@app.route('/data/<int:no>')
def datano(no):
    return jsonify(x[no-1])

# Redirect
@app.route('/home')
def home():
    return redirect('/')

@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'GET':
        return 'Anda nge-GET'
    elif request.method == 'POST':
        body = request.json
        print(body)
        return jsonify({
            'status': 'Data sukses terkirim',
            'nama': body['name'],
            'usia': body['age']
        })
    else:
        return 'Anda request selain GET & POST'

if __name__ == '__main__':
    app.run(debug=True)