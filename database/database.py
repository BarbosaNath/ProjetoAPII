import sqlite3
import sys
sys.path.insert(0, './')
from debug import Log


def create_table(database_file, table_name, values, not_exists=True):
    """ 
    Create Table
    """

    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    command = "CREATE TABLE {} {} ( \n".format(
        "IF NOT EXISTS" if not_exists else "", table_name)

    for value in values[:-1]:
        command += f"\t {value}, \n"
    command += f" {values[-1]} \n );"

    Log(command)
    cursor.execute(command)

    con.commit()
    con.close()


def format_if_str(value):
    """Format a value to the correct SQL type 'string' if it is a str"""
    return str(value) if type(value) != str else f"'{value}'"


def add_to_db(database_file, table_name, values: dict):
    """Adicionar ao arquivo de Data Base
    add_to_db("foo.db", "bar", {
        "column1": "value1",
        "column2": "value2",
        .
        .
        .
        "columnN": "valueN"
    })
    """

    # Conecta ao banco de dados
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    # Separa o comando em varias partes de forma que a função funcione indiferentemente do tamanho da tabela
    command = f"INSERT INTO {table_name} ("
    # INSERT INTO (

    # Adiciona o valor à coluna da tabela
    for key in list(values.keys())[:-1]:
        command += f"{key}, "
        # INSERT INTO (column1, column2, ..., columnN-1, 

    command += f"{list(values.keys())[-1]}) VALUES (" + ("?, " * (len(values)-1)) + "?);"
    # INSERT INTO (column1, column2, ..., columnN-1, columnN) VALUES (?, ?, ..., ?, ?);

    # Executa o commando
    Log(command)
    cursor.execute(command, [format_if_str(item) for item in values.values()])
    con.commit()
    con.close()


def list_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    list_fetchall = cursor.fetchall()

    con.close()
    return list_fetchall


def print_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")

    for i in cursor.fetchall():
        print("--------------------------")
        for e in i:
            print(e, end=" | ")
        print()

    con.close()


def remove_table_line(database_file, table_name, id):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE id = {id} ")

    con.commit()
    con.close()


def remove_table_where(database_file, table_name, where):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE {where}")

    con.commit()
    con.close()


# __main__ ------------------------------------------------------------------------------
if __name__ == "__main__":
    create_table("database/test.db", "usuario", [
        "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT",
        "name VARCHAR(60)",
        "email VARCHAR(100) NOT NULL",
        "password VARCHAR(80) NOT NULL"
    ])
    
    for i in range(5):
        add_to_db("database/test.db", "usuario", {
            "name": f"jose{i}",
            "email": f"jose{i}@email.com",
            "password": f"{i}"
        })

    print_table("database/test.db","usuario")
