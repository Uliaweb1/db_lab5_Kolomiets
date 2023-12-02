import psycopg2
import json
from decimal import Decimal

class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, Decimal):
            return float(o)
        return super(DecimalEncoder, self).default(o)

username = 'Kolomiets'
password = '123a1'
database = 'db_lab3'
host = 'localhost'
port = '5432'




conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    cur = conn.cursor()
    for table_name in ['disk','disk_space', 'gpu', 'laptop']:
        query = f'select * from {table_name};'

        cur.execute(query)
        rows = cur.fetchall()

        columns = [column[0] for column in cur.description]

        data = [dict(zip(columns, row)) for row in rows]
        with open(table_name + ".json", 'w') as json_file:
            json.dump(data, json_file, cls=DecimalEncoder, indent = 4)
