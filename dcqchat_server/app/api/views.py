from flask import Blueprint, request

api = Blueprint("api", __name__, url_prefix="/api")


@api.post("/upload")
def upload():
    return "test"
