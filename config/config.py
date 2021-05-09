import os
from dotenv import load_dotenv
class BaseConfig(object):
    load_dotenv()
    DEBUG = os.environ.get("DEBUG", 'False').lower() == 'true'
    SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get("SQLALCHEMY_TRACK_MODIFICATIONS", 'False').lower() == 'true'
    MYSQL_HOST = os.environ.get("MYSQL_HOST")
    MYSQL_DB = os.environ.get("MYSQL_DB")
    MYSQL_USERNAME = os.environ.get("MYSQL_USERNAME")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", 8889)
    MYSQL_UNIX_SOCKET = os.environ.get("MYSQL_UNIX_SOCKET", "/Applications/MAMP/tmp/mysql/mysql.sock")
    SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s?unix_socket=%s' % (
        MYSQL_USERNAME,
        MYSQL_PASSWORD,
        MYSQL_HOST,
        MYSQL_PORT,
        MYSQL_DB,
        MYSQL_UNIX_SOCKET
    )
    SQLALCHEMY_ECHO = True
    MAIL_SERVER=os.environ.get("MAIL_SERVER")
    MAIL_PROT=os.environ.get("MAIL_PROT")
    MAIL_USE_TLS=os.environ.get("MAIL_USE_TLS")
    MAIL_USERNAME=os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD=os.environ.get("MAIL_PASSWORD")
    MAIL_DEFAULT_SENDER=os.environ.get("MAIL_DEFAULT_SENDER")
    MAIL_TEST_RECIPIENTS=os.environ.get("MAIL_TEST_RECIPIENTS")

