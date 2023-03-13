from flask import Blueprint

ws = Blueprint("message", __name__, url_prefix="/ws")
