HOST = '8.210.229.44'
PORT = '3306'
DATABASE = 'dcqchat'
USERNAME = 'root'
PASSWORD = 'dcq.159357'

DB_URI = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
