from flask import Flask
from flask_socketio import emit, SocketIO

# from app.message.views import ws

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")


# app.register_blueprint(api)
@socketio.on('message')
def handle_message(message):
    print('received message: ' + message)
    emit('message', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, debug=True)

import os,time
import subprocess

