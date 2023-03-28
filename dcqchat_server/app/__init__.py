from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()


def create_app():
    app = Flask(__name__)
    socketio.init_app(app, cors_allowed_origins='*')
    from app.message.views import chat_bp
    app.register_blueprint(chat_bp)
    return app
