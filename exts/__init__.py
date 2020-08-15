import pymysql

from settings import MysqlConfig

db = pymysql.connect(
    host=MysqlConfig.remote_host,
    user=MysqlConfig.username,
    password=MysqlConfig.password,
    database=MysqlConfig.database,
    charset='utf8'
)