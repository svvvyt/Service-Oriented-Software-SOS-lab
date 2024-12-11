from flask import Flask
import pymysql
from pprint import pprint

app = Flask(__name__)

MARIADB_HOST = "mariadb-service"
MARIADB_USER = "root"
MARIADB_PASSWORD = "example"
MARIADB_DB = "mysql"

@app.route('/')
def index():
    connection = pymysql.connect(
        host=MARIADB_HOST,
        user=MARIADB_USER,
        password=MARIADB_PASSWORD,
        database=MARIADB_DB
    )
    try:
        with connection.cursor() as cursor:
            cursor.execute("SHOW DATABASES")
            databases = cursor.fetchall()
            return str(databases)
    finally:
        connection.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
