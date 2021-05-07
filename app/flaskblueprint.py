# demo/blueprints/home.py
from flask import Blueprint
home = Blueprint("home", __name__)
@home.route('/')
def index():
    return "This is home index page."