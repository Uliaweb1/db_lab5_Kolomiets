import psycopg2
import csv
import matplotlib.pyplot as plt

username = 'Kolomiets'
password = '123a1'
database = 'db_lab5'
host = 'localhost'
port = '5432'

query_recreate_tables = '''
DROP table if exists disk CASCADE;
DROP table if exists gpu CASCADE;
DROP table if exists Laptop CASCADE;
DROP table if exists disk_space CASCADE;

CREATE TABLE disk
(
  capacity VARCHAR(20) NOT NULL,
  type VARCHAR(100) NOT NULL,
  disk_id INT NOT NULL,
  PRIMARY KEY (disk_id)
);

CREATE TABLE gpu
(
  Name VARCHAR(100) NOT NULL,
  vendor VARCHAR(100) NOT NULL,
  vram VARCHAR(20),
  gpu_id INT NOT NULL,
  PRIMARY KEY (gpu_id)
);

CREATE TABLE Laptop
(
  brand VARCHAR(100) NOT NULL,
  laptop_name VARCHAR(100),
  display_size NUMERIC(5,1) NOT NULL,
  processor_type VARCHAR(100) NOT NULL,
  discount_price NUMERIC(20) NOT NULL,
  old_price NUMERIC(20) NOT NULL,
  ratings_5max NUMERIC(5,1),
  laptop_id INT NOT NULL,
  gpu_id INT,
  PRIMARY KEY (laptop_id),
  FOREIGN KEY (gpu_id) REFERENCES gpu(gpu_id)
);

CREATE TABLE disk_space
(
  relation_id INT NOT NULL,
  laptop_id INT NOT NULL,
  disk_id INT NOT NULL,
  PRIMARY KEY (relation_id),
  FOREIGN KEY (laptop_id) REFERENCES Laptop(laptop_id),
  FOREIGN KEY (disk_id) REFERENCES disk(disk_id),
  UNIQUE (laptop_id, disk_id)
);
'''
conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    cur = conn.cursor()

    cur.execute(query_recreate_tables)

    with open('Final_Dataframe.csv', newline='', encoding='utf-8') as csvfile:
        table = csv.DictReader(csvfile)
        insert_into_laptop = "INSERT INTO Laptop(laptop_id, brand, laptop_name, display_size, processor_type, gpu_id, discount_price, old_price,ratings_5max)"
        i=1
        for row in table:
            cur.execute(insert_into_laptop + f'VALUES({i}, \'{row["brand"]}\', \'{row["laptop_name"]}\', {row["display_size"]}, \'{row["processor_type"].strip()}\', {"NULL"}, {row["discount_price"]}, {row["old_price"]}, {"NULL"});')
            i = i + 1
