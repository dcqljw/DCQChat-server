from flask import Blueprint, render_template
from flask_socketio import emit, join_room

from app import socketio

chat_bp = Blueprint('chat', __name__)


@chat_bp.route('/')
def index():
    return render_template('index.html')


@socketio.on('connect')
def test_connect():
    emit('my response', {'data': 'Connected'})


@socketio.on("join")
def on_join(data):
    print(data)
    username = data["username"]
    room = data["room"]
    join_room(room)
    socketio.emit("joiend", {"username": username, "room": room}, room=room)


@socketio.on('message')
def handle_message(data):
    print(data)
    print(socketio.server.manager.rooms)
    username = data['username']
    room = data['room']
    message = data['text']
    socketio.emit('message', {'username': username, 'message': message}, room=room)


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('my event')
def handle_my_custom_event(json):
    print('received json: ' + str(json))
    socketio.emit('my response', json)

