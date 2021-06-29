import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'zoo-db.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'zoo-webapp-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'sidbadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'Zoo$Admin'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'sistorageaccount123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'efG3HZ2TFu4R55TFl8zVe1ZpdsKdFCKRtvG2BBeaSSOwmC0a7knbB35//T7jiBPd7qzSdFDoWlooiJ4Dge4z5Q=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
