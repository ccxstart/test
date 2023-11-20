from flask import Blueprint
from flask_restful import Api

logs = Blueprint('logs', __name__, url_prefix='/api/logs')
logs_api = Api(logs)

from flask_graduation.logs import views
