import csv
import mariadb
import os

try:
    db = mariadb.connect(host='localhost',user='admin',passwd='root',db='pgx')

except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cursor = db.cursor(dictionary=True)
