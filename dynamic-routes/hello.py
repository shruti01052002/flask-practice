from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/<name>')
def dynamic_router(name):
    return '<h1>Hello World, I am {}</h1>'.format(name)

@app.route('/index')
def indexfl():
    return render_template('index.html')

@app.route('/user')
def user():
    return render_template('user.html', name="Shruti")

@app.route('/condition')
def condition():
    return render_template('condition.html', eatable='fruits')

@app.route('/loops')
def loops():
    eatable = ["Apple", "Mango", "Carrot", "Potato"]
    return render_template('loops.html', eatable=eatable)
#debugger mode and reloader