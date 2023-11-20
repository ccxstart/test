from flask_graduation import db
from werkzeug.security import generate_password_hash, check_password_hash


def set_password(t_pwd):
    # 对密码进行hash加密
    pwd = generate_password_hash(t_pwd)
    return pwd
#
#
# def check_password(t_pwd, data_pwd):
#     # 验证密码     data_pwd: 数据库中的密码
#     return check_password_hash(t_pwd, data_pwd)


# 创建模型类
class User(db.Model):
    __tablename__ = 't_user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), unique=True, nullable=False)
    pwd = db.Column(db.String(128))

    @property
    def password(self):
        return self.pwd

    @password.setter
    def password(self, t_pwd):
        # 对密码进行hash验证
        self.pwd = generate_password_hash(t_pwd)

    def check_password(self, t_pwd):
        # 验证密码
        return check_password_hash(self.pwd, t_pwd)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'pwd': self.pwd,
        }


class Data(db.Model):
    __tablename__ = 't_data'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 省份
    province = db.Column(db.String(32))
    # 市区
    downtown = db.Column(db.String(64))
    # 介绍
    introduce = db.Column(db.String(128))
    # 详细地址
    address = db.Column(db.String(128))
    # 房屋面积
    area = db.Column(db.String(128))
    # 朝向
    orientation = db.Column(db.String(128))
    # 格局
    pattern = db.Column(db.String(128))
    # 每月租金
    rent = db.Column(db.String(128))
    # 链接
    link = db.Column(db.String(128))

    def to_dict(self):
        return {
            'id': self.id,
            'province': self.province,
            'downtown': self.downtown,
            'introduce': self.introduce,
            'address': self.address,
            'area': self.area,
            'orientation': self.orientation,
            'pattern': self.pattern,
            'rent': self.rent,
            'link': self.link
        }


class Datas(db.Model):
    __tablename__ = 't_data_all'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # 省份
    province = db.Column(db.String(32))
    # 市
    city = db.Column(db.String(32))
    # 区
    downtown = db.Column(db.String(64))
    # 介绍
    introduce = db.Column(db.String(128))
    # 详细地址
    address = db.Column(db.String(128))
    # 房屋面积
    area = db.Column(db.String(128))
    # 朝向
    orientation = db.Column(db.String(128))
    # 格局
    pattern = db.Column(db.String(128))
    # 每月租金
    rent = db.Column(db.String(128))
    # 链接
    link = db.Column(db.String(128))

    def to_dict(self):
        return {
            'id': self.id,
            'province': self.province,
            'city': self.city,
            'downtown': self.downtown,
            'introduce': self.introduce,
            'address': self.address,
            'area': self.area,
            'orientation': self.orientation,
            'pattern': self.pattern,
            'rent': self.rent,
            'link': self.link
        }
