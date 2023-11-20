import os


class Config:
    # 配置MAYSQL参数
    MYSQL_DIALECT = 'mysql'
    MYSQL_DIRVER = 'pymysql'
    MYSQL_NAME = 'root'
    MYSQL_PWD = ''
    MYSQL_HOST = 'localhost'
    MYSQL_PORT = 3306
    MYSQL_DB = 'flask_graduation'
    MYSQL_CHARSET = 'utf8mb4'

    SQLALCHEMY_DATABASE_URI = f'{MYSQL_DIALECT}+{MYSQL_DIRVER}://{MYSQL_NAME}:{MYSQL_PWD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}?charset={MYSQL_CHARSET}'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # 加密的密钥: 盐
    SECRET_KEY = os.urandom(16)


# 开发模式
class DevelopmentConfig(Config):
    DEBUG = True


# 生产模式
class ProductionConfig(Config):
    pass


config_map = {
    'develop': DevelopmentConfig,
    'product': ProductionConfig
}

"""
版本:
pip install pymysql==1.0.2
pip install sqlalchemy==1.3.15
pip install flask-sqlalchemy==2.4.1
pip install itsdangerous==1.1.0
pip install flask_migrate==2.5.3
pip install flask_script==2.0.6
pip install flask==1.1.1
"""
