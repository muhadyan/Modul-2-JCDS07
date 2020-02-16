# # BIODATA DATA (CV) html => server Flask
# # - Home
# # - About
# # - Education
# # - Skills
# # - Experiences

# from flask import Flask, render_template

# server = Flask(__name__)

# # home route
# @server.route('/')
# def home():
#     return render_template('home.html')

# # about route
# @server.route('/about')
# def about():
#     return render_template('about.html')

# # education route
# @server.route('/education')
# def education():
#     return render_template('education.html')

# # skills route
# @server.route('/skills')
# def skills():
#     return render_template('skills.html')

# # experience route
# @server.route('/experiences')
# def experiences():
#     return render_template('experiences.html')

# # route untuk error 404
# @server.errorhandler(404)
# def notFound(error):
#     return '<h1>Halaman Ga Ada</h1>'

# if __name__ == '__main__':
#     server.run(debug = True)



# digidb => flask response:
# - /table => HTML tabel data digidb
# - /json => JSON data digimon

import pandas as pd
import numpy as np
import json
from flask import Flask, render_template, jsonify, abort, send_from_directory


df = pd.read_html('http://digidb.io/digimon-list/')
df = df[0]

df.to_json(r'C:\Users\Adyan\Desktop\JCDS\Modul_2\Day_21\digi.json', orient='records')

with open('digi.json') as json_file:
    data = json.load(json_file)


#render dataframe as html
html = df.to_html()

#write html to file
text_file = open("digi.html", "w")
text_file.write(html)
text_file.close()


server = Flask(__name__)

# render json
@server.route('/json')
def json():
    return jsonify(data)

# render html
@server.route('/html')
def html():
    return render_template('digi.html')

if __name__ == '__main__':
    server.run(debug = True)