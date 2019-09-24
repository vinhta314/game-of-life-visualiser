from flask import render_template
from flask_socketio import emit
from game_of_life_app import app, socketio

values = {
    'slider1': 25,
    'slide2': 0
}

@app.route('/')
def index():
    return render_template('index.html', **values)


@socketio.on('connect')
def test_connect():
    emit('after connect', {'data': 'Lets dance'})