# # Перевод в верхний и нижний регистр. Выделить и нажать:
# # CTRL + K, CTRL + U
# # CTRL + K, CTRL + L


# написать скрипт, который создает таблицу с пользователями с полями
# id, name, lastname, deleted_flg

import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
	CREATE TABLE if not exists users(
		id integer primary key autoincrement,
		name varchar(128),
		lastname varchar(128),
		deleted_flg integer default 0
	)
''')

# создать функцию add_user которая в качестве аргументов 
# принимает name и lastname и добавляет пользователя
def add_user(name, lastname):
	cursor.execute('''
		INSERT INTO users (name, lastname) values(?, ?)
	 ''', [name, lastname])

	conn.commit()

# написать функцию show_users которая выводит построчно данные с пользователями
def show_users():
	cursor.execute('SELECT * from users')
	for user in cursor.fetchall():
		print(f'{user}')

# add_user('Анатолий', 'Ушанов')
# add_user('Максим', 'Грибов')
# add_user('Антон', 'Куликов')

# добавить функцию delete_user, которая получает id пользователя
# и реализует логическое удаление данного пользоватея
def delete_user(id):
	cursor.execute('''
		UPDATE users
		set deleted_flg = ?
		where id = ?
	''', [1, id])
	conn.commit()

delete_user(1)

# создать представление, которое выводит только не удаленных пользователей
# с полями name и lastname
def create_view():
	cursor.execute('''
		CREATE VIEW if not exists v_users as 
			SELECT id, name, lastname 
			from users 
			where deleted_flg = 0
	''')
	# conn.commit()


# create_view()
# cursor.execute('SELECT * from v_users')
# for user in cursor.fetchall():
# 	print(f'{user}')

# show_users()























































