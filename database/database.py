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


def get_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    table_values = cursor.fetchall()

    con.close()
    return table_values


def get_table_as_dict(database_file, table_name, indexer=None):
    """ Retorna uma lista de dicionarios ou um dicionario de dicionarios.
        database_file : str -> Caminho para o arquivo de banco de dados
        table_name    : str -> Nome da tabela que deseja acessar
        indexer       : str -> Nome da coluna que indexará o dicionario 
                                    por exemplo, se for passado 'nome' como indexer,
                                    o programador que for utilizar a tabela acessará 
                                    determinado elemento da seguinte maneira
                                    ```tabela['Claudio Junior']['idade']```
                                    no lugar de ```tabela[0]['idade']```
                               caso nada seja informado, uma lista de dicionario sera retornada.
    """
    table = get_table(database_file, table_name)
    names = get_column_names(database_file, table_name)

    for i in range(len(table)):
        table[i] = {names[index]: table[i][index] for index in range(len(table[i]))}

    if indexer is not None:
        table = {element[indexer]: element for element in table}

    return table

    



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

def get_column_details(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    # cursor.execute(f"SELECT name FROM sys.columns WHERE object_id = OBJECT_ID('{table_name}');")
    # cursor.execute(f"SELECT sql FROM sqlite_master WHERE tbl_name = '{table_name}' AND type = 'table'")
    cursor.execute(f"PRAGMA table_info('{table_name}');")

    column_details = cursor.fetchall()
    con.close()
    return column_details

def get_column_names(database_file, table_name):
    return tuple(details[1] for details in get_column_details(database_file, table_name))

def remove_table_line(database_file, table_name, ID):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE id = {ID} ")

    con.commit()
    con.close()


def remove_table_where(database_file, table_name, where):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE {where}")

    con.commit()
    con.close()

create_table("database/test.db", "usuario", [
    "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT",
    "name VARCHAR(60)",
    "email VARCHAR(100) NOT NULL",
    "password VARCHAR(80) NOT NULL"
])

# __main__ ------------------------------------------------------------------------------
if __name__ == "__main__":
    # print(get_column_details("database/test.db", "usuario"))
    # print(get_column_names("database/test.db", "usuario"))
    
    tabela = get_table_as_dict("database/test.db", "usuario", "id")

    for e in tabela:
        print(tabela[e])
    print(tabela[11]['email'])
