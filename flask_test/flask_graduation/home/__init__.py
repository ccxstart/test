from flask_restful import Api
from flask import Blueprint

home = Blueprint('home', __name__, url_prefix='/home')

home_api = Api(home)

from flask_graduation.home import view
