# Cоздание таблицы со столбцом по умолчанию
#
# Создайте таблицу в БД на основе схемы из
# предыдущей задачи. При создании таблицы
# предусмотрите для поля Name значение по умолчанию "Noname"
#
import sqlite3
import prettytable

with sqlite3.connect(":memory:") as con:
    cur = con.cursor()
    sqlite_query = """CREATE TABLE animals
                        (id integer primary key autoincrement,
                        AnimalType nvarchar(20),
                        Sex nvarchar(20), 
                        name nvarchar(20) constraint name_1 default 'Noname',
                        DateOfBirth date,
                        Age float,
                        Weight decimal) """
    cur.execute(sqlite_query)
# Не удаляйте этот код, он используется
# для вывода заголовков созданной таблицы


def print_result(sqlite_query):
    cur.execute(sqlite_query)
    result_query = ('SELECT * from animals')
    table = cur.execute(result_query)
    mytable = prettytable.from_db_cursor(table)
    mytable.max_width = 30
    print(mytable)


if __name__ == '__main__':
    print_result(sqlite_query)
