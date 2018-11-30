from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def getUser(name):
    return render_template('user.html', name=name)

@app.route('/galeria')
def f():
    obrazki = [
        'http://www.dekomozaik.pl/userdata/gfx/13a5beec12de0bd6f358e3003b87e21e.jpg',
        'http://maxfruit.pl/226-large_default/pomarancza.jpg',
        'https://www.zajadam.pl/wp-content/uploads/2015/02/Pomarancza.png',
        'https://res.cloudinary.com/dj484tw6k/f_auto,q_auto,c_pad,b_white,w_360,h_360/v1499889192/be/82135.jpg'
    ]
    return render_template('galeria.html', obrazki=obrazki)