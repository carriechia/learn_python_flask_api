class BaseConfig:
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost:8889/api_test?unix_socket=/Applications/MAMP/tmp/mysql/mysql.sock'

