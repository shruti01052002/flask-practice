#Basic Component of a Flask Application
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask</h1>"

#Creating Dynamic Routes <>

