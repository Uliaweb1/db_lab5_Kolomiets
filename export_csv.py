import psycopg2
import csv

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

        with open(table_name + ".csv", 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(columns)
            for row in rows:
                csv_writer.writerow(row)
