from sqlalchemy import and_
from flask_graduation.user import user_api, user
from flask import request
from flask_graduation import db, models
from flask_graduation.models import set_password
from flask_restful import Resource
from flask_graduation.utils.message import to_dict_msg
from flask_graduation.utils.tokens import generate_auth_token, verify_auth_token, login_required


class User(Resource):
    # home页查询数据
    # @login_required
    def get(self):
        province = request.args.get('province')
        city = request.args.get('city')
        downtown = request.args.get('downtown')
        page_num = int(request.args.get('page_num') if request.args.get('page_num') else 1)
        page_size = int(request.args.get('page_size') if request.args.get('page_size') else 10)
        # print(province, downtown, page_num, page_size)

        try:
            if province:
                if city:
                    if downtown:
                        datas_page = models.Datas.query.filter(and_(models.Datas.province.like(f'%{province}%'),
                                                                   models.Datas.city.like(f'%{city}%'),
                                                                    models.Datas.downtown.like(f'%{downtown}%'))).paginate(
                            page=page_num, per_page=page_size)
                    else:
                        datas_page = models.Datas.query.filter(and_(models.Datas.province.like(f'%{province}%'),
                                                                    models.Datas.city.like(
                                                                        f'%{city}%'))).paginate(
                            page=page_num, per_page=page_size)
                else:
                    datas_page = models.Datas.query.filter(models.Datas.province.like(f'%{province}%')).paginate(
                        page=page_num, per_page=page_size)
            else:
                datas_page = models.Datas.query.paginate(page=page_num, per_page=page_size)
            data = {
                'page_num': page_num,
                'page_size': page_size,
                'totalPage': datas_page.total,
                'data_list': [d.to_dict() for d in datas_page.items]
            }
            return to_dict_msg(200, data, '获取数据列表成功！')
        except Exception as e:
            print(e)
            return to_dict_msg(20000)

        # try:
        #     if province:
        #         if downtown:
        #             datas_page = models.Data.query.filter(and_(models.Data.province.like(f'%{province}%'),
        #                                                        models.Data.downtown.like(f'%{downtown}%'))).paginate(
        #                 page=page_num, per_page=page_size)
        #         else:
        #             datas_page = models.Data.query.filter(models.Data.province.like(f'%{province}%')).paginate(
        #                 page=page_num, per_page=page_size)
        #     else:
        #         datas_page = models.Data.query.paginate(page=page_num, per_page=page_size)
        #     data = {
        #         'page_num': page_num,
        #         'page_size': page_size,
        #         'totalPage': datas_page.total,
        #         'data_list': [d.to_dict() for d in datas_page.items]
        #     }
        #     return to_dict_msg(200, data, '获取数据列表成功！')
        # except Exception as e:
        #     print(e)
        #     return to_dict_msg(20000)

    # 注册用户
    def post(self):
        name = request.form.get('name')
        pwd = request.form.get('pwd')
        real_pwd = request.form.get('real_pwd')
        print(name, pwd)
        # 验证数据的正确性
        if not all([name, pwd, real_pwd]):
            return to_dict_msg(10000)
        if pwd != real_pwd:
            return to_dict_msg(10013)
        pwd = set_password(pwd)
        try:
            usr = models.User(name=name, pwd=pwd)
            u = models.User.query.filter_by(name=name).first()
            if u:
                return to_dict_msg(10021)
            db.session.add(usr)
            db.session.commit()
            return to_dict_msg(200)
        except Exception:
            to_dict_msg(20000)


user_api.add_resource(User, '/user')


# 登录接口
@user.route('/login', methods=['POST'])
# @login_required
def login():
    name = request.form.get('name')
    pwd = request.form.get('pwd')
    print(name, pwd)
    if not all([name, pwd]):
        return to_dict_msg(10000)
    if not (name and pwd):
        return to_dict_msg(10005)
    usr = models.User.query.filter_by(name=name).first()
    if not usr:
        return to_dict_msg(10005, msg='无此用户')
    if not usr.check_password(pwd):
        return to_dict_msg(10005)
    token = generate_auth_token(usr.id, 100000000)
    return to_dict_msg(200, data={'token': token})


@user.route('/test')
# @login_required
def test():
    province = request.args.get('province')
    city = request.args.get('city')
    downtown = request.args.get('downtown')

    # json_data = {}

    province_list = []
    province_all = db.session.query(models.Datas.province).distinct().all()
    for da in province_all:
        province_list.append(da[0])
        # print(da[0])
        # json_data['province_list'] = province_all
        # city_list = []
        # json_data[da[0]] = city_list
        # city_all = db.session.query(models.Datas.city).filter(models.Datas.province == da[0]).distinct().all()
        # for i in city_all:
        #     downtown_list = []
        #     c_list = db.session.query(models.Datas.downtown).filter(models.Datas.province == da[0]).filter(models.Datas.city == i[0]).distinct().all()
        #     for c in c_list:
        #         downtown_list.append(c[0])
        #     print(downtown_list)
        #     city_list.append({i[0]: downtown_list})
    print(province_list)
    return to_dict_msg(200, data=province_list)

