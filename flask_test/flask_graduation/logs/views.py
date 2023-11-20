from flask_restful import Resource
from flask_graduation import models
from flask_graduation.logs import logs_api
from flask import request
from flask_graduation.utils.message import to_dict_msg


class Admin(Resource):
    def get(self):
        name = request.args.get('name')
        id = request.args.get('id')
        page_num = int(request.args.get('page_num'))
        page_size = int(request.args.get('page_size'))
        if name:
            user_list = models.User.query.filter(models.User.name == name).paginate(page=page_num, per_page=page_size)
        elif id:
            user_list = models.User.query.filter(models.User.id == id).paginate(page=page_num, per_page=page_size)
        else:
            user_list = models.User.query.paginate(page=page_num, per_page=page_size)

        data = {
            'page_num': page_num,
            'page_size': page_size,
            'totalPage': user_list.total,
            'data_list': [d.to_dict() for d in user_list.items]
        }

        return to_dict_msg(200, data=data)


logs_api.add_resource(Admin, '/admin')

