import sqlite3
import sys
sys.path.insert(0, './')


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

    cursor.execute(command)

    con.commit()
    con.close()


def get_all_tables(database_file):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute("""  SELECT name
                        FROM   sqlite_schema
                        WHERE  type ='table' AND name NOT LIKE 'sqlite_%';
                    """)

    all_tables = cursor.fetchall()

    con.close()

    return [element[0] for element in all_tables]


def remove_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DROP TABLE {table_name};")

    con.commit()
    con.close()


def edit_element(database_file, table_name, what, to, where, equals):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    
    command = f"""UPDATE {table_name} SET {what} = {to} WHERE {where} = ?"""
    cursor.execute(command, [equals])

    con.commit()
    con.close()


def format_if_str(value):
    """Format a value to the correct SQL type 'string' if it is a str"""
    return str(value) if type(value) != str else f"'{value}'"


def reformat_if_str(value):
    """Format a value in the SQL type 'string' to the python str"""
    return value if type(value) != str else value.strip("'")


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
    cursor.execute(command, [format_if_str(item) for item in values.values()])
    con.commit()
    con.close()


def get_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()
    cursor.execute(f"SELECT * FROM {table_name};")
    table_values = [list(values) for values in cursor.fetchall()]

    con.close()
    for i, values in enumerate(table_values):
        for j, value in enumerate(values):
            table_values[i][j] = reformat_if_str(value)

    return [tuple(values) for values in table_values]


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


def remove_element(database_file, table_name, ID):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute(f"DELETE FROM {table_name} WHERE id = {ID} ")

    con.commit()
    con.close()


def remove_element_where(database_file, table_name, where_what, equals):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    command = f"DELETE FROM {table_name} WHERE {where_what} = ?"
    cursor.execute(command, [equals])

    con.commit()
    con.close()


def drop_table(database_file, table_name):
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    cursor.execute (f"DROP TABLE {table_name}")

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
    db = "database/modules.db"
    tab = "modules"
    # print(get_column_details("database/test.db", "usuario"))
    # print(get_column_names("database/test.db", "usuario"
    # print(get_table_as_dict("database/test.db", "usuario", "id"))

    print_table(db, tab)
    # print(f"{get_all_tables(db)             =  }")
    # print(f"{get_table(db, tab)[0]          =  }")
    # print(f"{get_column_details(db, tab)[0:2] =  }")
    # print(f"{get_column_names(db, tab)[0:2]   =  }")

    pass
