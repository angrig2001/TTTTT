import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE if not exists product_hist(
		id integer primary key autoincrement,
		product_id integer,
		title varchar(128),
		price integer,
		start_dttm datetime default current_timestamp,
		end_dttm datetime default (datetime('2999-12-31 23:59:59'))
	)
''')

def add_product(product_id, title, price):
	# закрыть дату актуальности у прошлой записи
	cursor.execute('''
		UPDATE product_hist
		set end_dttm = datetime('now', '-1 second')
		where product_id = ?
			and end_dttm = datetime('2999-12-31 23:59:59')
	''', [product_id])

	#  добавить новую запись
	cursor.execute('''
		INSERT INTO product_hist (product_id, title, price) 
		values(?, ?, ?)
	 ''', [product_id, title, price])

	conn.commit()

# add_product(1, 'Велосипед', 45000)
# add_product(1, 'Велосипед', 50000)
# add_product(1, 'Велосипед', 55000)

# добавить функцию show_products, которая выводит в консоль все записи
def show_product():
	cursor.execute('SELECT * from product_hist')
	for item in cursor.fetchall():
		print(f'{item}')

show_product()















