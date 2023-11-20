"""
1. 加密的数据     uid
2. 算法          python模块
2. 密钥          flask_app  SECRET_KEY
"""
# from itsdangerous import URLSafeTimedSerializer as Serializer
from itsdangerous import URLSafeTimedSerializer as Serializer
from flask import current_app, request, app, jsonify
from flask_graduation.models import User
from flask_graduation.utils.message import to_dict_msg
import functools


# 生成token对象
def generate_auth_token(uid, expiration):  # expiration 有效期
    # 创建加密对象
    s = Serializer(current_app.config['SECRET_KEY'])

    return s.dumps({'id': uid})


# 验证token
def verify_auth_token(token_str):
    # 创建解密对象
    s = Serializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token_str)
    except Exception:
        return None
    usr = User.query.filter_by(id=data['id']).first()
    return usr


def login_required(view_func):
    @functools.wraps(view_func)
    def verify_token(*args, **kwargs):
        try:
            token = request.headers['token']
        except Exception:
            return to_dict_msg(10016)
        # 创建解密对象
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token)
        except Exception:
            return to_dict_msg(10017)
        return view_func(*args, **kwargs)

    return verify_token
