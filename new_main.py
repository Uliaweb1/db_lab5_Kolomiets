import psycopg2
import matplotlib.pyplot as plt

username = 'Kolomiets'
password = '123a1'
database = 'db_lab5'
host = 'localhost'
port = '5432'

query_1a = '''
DROP VIEW IF EXISTS itemsByBrandCount;
create view itemsByBrandCount as
select brand as brand, count(*) as count
from laptop 
group by brand
order by brand;
'''
query_1b = '''
select * from itemsByBrandCount;
'''

query_2a = '''
DROP VIEW IF EXISTS items_by_display_size_count;
create view items_by_display_size_count as
select display_size as display_size, count(*) as count
from laptop
group by display_size
order by display_size;
'''

query_2b = '''
select * from items_by_display_size_count;
'''

query_3a = '''
DROP VIEW IF EXISTS total_cost_of_laptops_with_display_size;
create view total_cost_of_laptops_with_display_size as
select display_size as display_size, sum(discount_price) as total_cost
from laptop
group by display_size
order by display_size;
'''

query_3b = '''
select * from total_cost_of_laptops_with_display_size;
'''


conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    cur = conn.cursor()

    cur.execute(query_1a)
    cur.execute(query_1b)
    brand = []
    total = []

    for row in cur:
        brand.append(row[0])
        total.append(row[1])

    x_range = range(len(brand))

    # figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)

    # bar_ax.bar(x_range, total, label='Total')
    # bar_ax.set_title('Кількість ноутбуків за брендом')
    # bar_ax.set_xlabel('Бренд')
    # bar_ax.set_ylabel('Кількість')
    # bar_ax.set_xticks(x_range)
    # bar_ax.set_xticklabels(brand)

    plt.bar(brand, total, label='Total')
    plt.title('Кількість ноутбуків за брендом')
    plt.xlabel('Бренд')
    plt.ylabel('Кількість')
    plt.xticks(brand)
    # plt.xticklabels(brand)
    # plt.show()
    plt.savefig("new_graphs1.png")
    plt.close()

    cur.execute(query_2a)
    cur.execute(query_2b)
    display_size = []
    total = []

    for row in cur:
        display_size.append(row[0])
        total.append(row[1])

    # pie_ax.pie(total, labels=display_size, autopct='%1.1f%%')
    # pie_ax.set_title('Частка ноутбуків з діагоналлю')

    plt.pie(total, labels=display_size, autopct='%1.1f%%')
    plt.title('Частка ноутбуків з діагоналлю')
    # plt.show()
    plt.savefig("new_graphs2.png")
    plt.close()

    cur.execute(query_3a)
    cur.execute(query_3b)
    display_size = []
    total_price = []

    for row in cur:
        display_size.append(row[0])
        total_price.append(row[1])

    # graph_ax.plot(display_size, total_price, marker='o')
    # graph_ax.set_xlabel('Розмір екрану')
    # graph_ax.set_ylabel('Сумарна вартість ноутбуків')
    # graph_ax.set_title('Сумарна вартість ноутбуків від розміру екрану')

    plt.plot(display_size, total_price, marker='o')
    plt.xlabel('Розмір екрану')
    plt.ylabel('Сумарна вартість ноутбуків')
    plt.title('Сумарна вартість ноутбуків від розміру екрану')

    for qnt, price in zip(display_size, total_price):
        # graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')
        plt.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')

    # plt.show()
    plt.savefig("new_graphs3.png")
    plt.close()

# mng = plt.get_current_fig_manager()
# mng.resize(1800, 600)

# plt.show()