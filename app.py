# coding: utf-8

"""
Source : 
Date : 07/01/2021
Auteur : Claire Doriath
Dossier : /Python34/MesDEv/Flask/ProjetVideo
Fichier : app.py
Description : app flask 

Mot cles : 
"""

from flask import Flask , render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/claire')
def myclaire():
    return render_template('claire.html')





