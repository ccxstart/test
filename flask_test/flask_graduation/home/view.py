import json

from flask_graduation.home import home_api, home
from flask import request
from flask_graduation import db, models
from flask_restful import Resource
from flask_graduation.utils.message import to_dict_msg, to_dict_msg_min_max


class Data(Resource):
    def get(self):
        return 'home'


home_api.add_resource(Data, '/home')


# 省份列表接口
class ProvinceList(Resource):
    def get(self):
        try:
            province_list = []
            province_all = db.session.query(models.Datas.province).distinct().all()
            for da in province_all:
                province_list.append(da[0])
            return to_dict_msg(200, data=province_list)
        except Exception:
            return to_dict_msg(20000)


home_api.add_resource(ProvinceList, '/data/province_list')


# 市级列表接口
class CityList(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city_list = []
            city_all = db.session.query(models.Datas.city).filter(models.Datas.province == province).distinct().all()
            for da in city_all:
                city_list.append(da[0])
            return to_dict_msg(200, data=city_list)
        except Exception:
            return to_dict_msg(20000)


home_api.add_resource(CityList, '/data/city_list')


# 县级列表接口
class DowntownList(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city = request.args.get('city')
            downtown_list = []
            downtown_all = db.session.query(models.Datas.downtown).filter(models.Datas.province == province).filter(models.Datas.city == city).distinct().all()
            for da in downtown_all:
                downtown_list.append(da[0])
            print(downtown_list)
            return to_dict_msg(200, data=downtown_list)
        except Exception:
            return to_dict_msg(20000)


home_api.add_resource(DowntownList, '/data/downtown_list')


# 地区散点图接口
class Splattering(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city = request.args.get('city')
            downtown = request.args.get('downtown')
            if province:
                if city:
                    if downtown:
                        result = models.Datas.query.filter_by(province=province, city=city, downtown=downtown).all()
                    else:
                        result = models.Datas.query.filter_by(province=province, city=city).all()
                else:
                    result = models.Datas.query.filter_by(province=province).all()
            else:
                return to_dict_msg(20001)
            # result = models.Datas.query.filter_by(province=province, city=city, downtown=downtown).all()
            print(result)
            area_list = []
            rent_list = []
            all_list = []
            for r in result:
                area = r.area
                area = area.replace('㎡', '')
                rent = r.rent
                area_list.append(area)
                rent_list.append(rent)
                # print(area, rent)
                all_list.append([area, rent])
            return to_dict_msg(200, data=all_list)
        except Exception as e:
            print(e)
            return to_dict_msg(20000)


home_api.add_resource(Splattering, '/data/splattering')


# 租金分析饼状图
class Pie(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city = request.args.get('city')
            downtown = request.args.get('downtown')
            radius_list = [{'min_rent': 0, 'max_rent': 1500}, {'min_rent': 1500, 'max_rent': 3000},
                           {'min_rent': 3000, 'max_rent': 5000}, {'min_rent': 5000, 'max_rent': 7000},
                           {'min_rent': 7000, 'max_rent': 15000}]
            data_list = []
            if province:
                if city:
                    if downtown:
                        for radius in radius_list:
                            min_rent = radius['min_rent']
                            max_rent = radius['max_rent']
                            ss = models.Datas.query.filter(models.Datas.province == province,
                                                           models.Datas.city == city, models.Datas.downtown == downtown,
                                                           models.Datas.rent > min_rent,
                                                           models.Datas.rent <= max_rent).count()
                            data_list.append({'value': ss, 'name': f'{min_rent}元-{max_rent}元'})
                    else:
                        for radius in radius_list:
                            min_rent = radius['min_rent']
                            max_rent = radius['max_rent']
                            ss = models.Datas.query.filter(models.Datas.province == province,
                                                           models.Datas.city == city,
                                                           models.Datas.rent > min_rent,
                                                           models.Datas.rent <= max_rent).count()
                            data_list.append({'value': ss, 'name': f'{min_rent}元-{max_rent}元'})
                else:
                    for radius in radius_list:
                        min_rent = radius['min_rent']
                        max_rent = radius['max_rent']
                        ss = models.Datas.query.filter(models.Datas.province == province,
                                                       models.Datas.rent > min_rent,
                                                       models.Datas.rent <= max_rent).count()
                        data_list.append({'value': ss, 'name': f'{min_rent}元-{max_rent}元'})
            else:
                return to_dict_msg(20001)
            # for radius in radius_list:
            #     min_rent = radius['min_rent']
            #     max_rent = radius['max_rent']
            #     ss = models.Datas.query.filter(models.Datas.province == province,
            #                                   models.Datas.city == city, models.Datas.downtown == downtown,
            #                                   models.Datas.rent > min_rent, models.Datas.rent <= max_rent).count()
            #     data_list.append({'value': ss, 'name': f'{min_rent}元-{max_rent}元'})

            return to_dict_msg(200, data=data_list)
        except Exception:
            return to_dict_msg(20000)


home_api.add_resource(Pie, '/data/pie')


# 房源数量接口
class HouseNum(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city = request.args.get('city')
            if province:
                if city:
                    result = db.session.query(
                        models.Datas.downtown,
                        db.func.count().label('count')
                    ).filter(
                        models.Datas.province == province,
                        models.Datas.city == city
                    ).group_by(
                        models.Datas.downtown
                    ).all()
                else:
                    result = db.session.query(
                        models.Datas.city,
                        db.func.count().label('count')
                    ).filter(
                        models.Datas.province == province
                    ).group_by(
                        models.Datas.city
                    ).all()
            else:
                return to_dict_msg(20001)
            # result = db.session.query(
            #     models.Datas.downtown,
            #     db.func.count().label('count')
            # ).filter(
            #     models.Datas.province == province
            # ).group_by(
            #     models.Datas.downtown
            # ).all()

            # 构建结果字典
            data = {}
            right_option_x = []
            right_option_y = []
            left_option = []
            for downtown, count in result:
                # if province not in data:
                #     data[province] = {}
                # data[downtown] = count
                right_option_x.append(downtown)
                right_option_y.append(count)
                left_option.append({'value': count, 'name': downtown})
            # data['x_right'] = right_option_x
            # data['y_right'] = right_option_y
            # abscissa : 横坐标       ordinate : 纵坐标
            data['right'] = {'x_right': right_option_x, 'y_right': right_option_y}
            data['left'] = left_option
            return to_dict_msg(200, data=data)
        except Exception as e:
            print(e)
            return to_dict_msg(20000)


home_api.add_resource(HouseNum, '/data/houseNum')


# 平均房租接口
class AverageRent(Resource):
    def get(self):
        try:
            province = request.args.get('province')
            city = request.args.get('city')
            if province:
                if city:
                    result = db.session.query(
                        models.Datas.downtown,
                        db.func.round(db.func.avg(models.Datas.rent), 2).label('average_value')
                    ).filter(
                        models.Datas.province == province,
                        models.Datas.city == city
                    ).group_by(
                        models.Datas.downtown
                    ).all()
                else:
                    result = db.session.query(
                        models.Datas.city,
                        db.func.round(db.func.avg(models.Datas.rent), 2).label('average_value')
                    ).filter(
                        models.Datas.province == province
                    ).group_by(
                        models.Datas.city
                    ).all()
            else:
                return to_dict_msg(20001)
            # result = db.session.query(
            #     models.Datas.downtown,
            #     db.func.round(db.func.avg(models.Datas.rent), 2).label('average_value')
            # ).filter(
            #     models.Datas.province == province
            # ).group_by(
            #     models.Datas.downtown
            # ).all()

            data = {}
            right_option_x = []
            right_option_y = []
            left_option = []
            for downtown, count in result:
                right_option_x.append(downtown)
                right_option_y.append(count)
                left_option.append({'value': count, 'name': downtown})
            data['right'] = {'x_right': right_option_x, 'y_right': right_option_y}
            data['left'] = left_option
            return to_dict_msg(200, data=data)
        except Exception as e:
            print(e)
            return to_dict_msg(20000)


home_api.add_resource(AverageRent, '/data/averagerRent')


class Test(Resource):
    def get(self):
        data_list = []
        models.Data.query().filter()


# 地图展示接口
class ProvinceMap(Resource):
    def get(self):
        result = db.session.query(
            models.Datas.province,
            db.func.avg(models.Datas.rent).label('average_rent')
        ).group_by(models.Datas.province).all()

        average_rent_data = [{'name': row.province, 'value': round(row.average_rent, 2)} for row in result]

        name_list = []
        with open('./flask_graduation/utils/china.json', 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            data_list = data['features']
            for i in data_list:
                name = i['properties']['name']
                name_list.append(name)

        new_data_list = []

        for i in average_rent_data:
            na = i['name']
            value = i['value']
            for j in name_list:
                if na in j:
                    na = j
                    new_data_list.append({'name': na, 'value': value})

        min_avg_rent = min(avg['value'] for avg in average_rent_data)
        max_avg_rent = max(avg['value'] for avg in average_rent_data)
        return to_dict_msg_min_max(200, min=min_avg_rent, max=max_avg_rent, data=new_data_list)


home_api.add_resource(ProvinceMap, '/data/map')
