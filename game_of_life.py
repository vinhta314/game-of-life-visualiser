from flask import Flask, render_template
from flask_socketio import SocketIO
from threading import Thread, Event
from time import sleep
from app.grid_model import CellularAutomationModel

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
app.config['DEBUG'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

socketio = SocketIO(app)


class GridThread(Thread):
    def __init__(self):
        super().__init__()
        self.model = CellularAutomationModel()
        self.delay = 1
        self._pause_event = Event()

    def pause(self):
        self._pause_event.clear()

    def resume(self):
        self._pause_event.set()

    def reset(self):
        self.model.reset_grid()

    def change_cell(self, x, y):
        print(x, y)
        self.model.toggle_cell_state(x, y)

    def _evolve_state(self):
        next_state = self.model.evolve()
        socketio.emit('nextState', next_state, broadcast=True)
        print(next_state)

    def run(self):
        self._pause_event.set()
        while True:
            self._pause_event.wait()
            self._evolve_state()
            sleep(self.delay)


thread = GridThread()


@app.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def on():
    global thread


@socketio.on('start')
def start_thread():
    if not thread.isAlive():
        thread.start()
    else:
        thread.resume()


@socketio.on('stop')
def stop_thread():
    if thread.isAlive():
        thread.pause()


@socketio.on('reset')
def reset_grid_state():
    thread.reset()


@socketio.on('updateCell')
def update_cell(msg):
    if thread.isAlive():
        thread.change_cell(x=msg['x'], y=msg['y'])


if __name__ == '__main__':
    socketio.run(
        app,
        host='0.0.0.0'
    )
