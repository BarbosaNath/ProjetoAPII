import sqlite3


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


def add_to_db(database_file, table_name, values: dict):
    """Adicionar ao arquivo de Data Base"""

    # Conecta ao banco de dados
    con = sqlite3.connect(database_file)
    cursor = con.cursor()

    # Separa o comando em varias partes de forma que a função seja indiferente ao tamanho da tabela
    command_0 = f"INSERT INTO {table_name} ("
    command_1 = ") VALUES ("

    # Adiciona à coluna da tabela o valor
    for key in list(values.keys())[:-1]:
        command_0 += f"{key}, "
        command_1 += "{}, ".format(values[key] if type(values[key]) is not str
                                   else f"'{values[key]}'")
    command_0 += f"{list(values.keys())[-1]}"
    command_1 += "{}".format(
        values[list(values.keys())[-1]] if type(values[list(values.keys(
        ))[-1]]) is not str else f"'{values[list(values.keys())[-1]]}'")
    command = command_0 + command_1 + ");"

    # Executa o commando
    cursor.execute(command)
    con.commit()
    con.close()


create_table("database/test.db", "usuario", [
    "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT",
    "name VARCHAR(60)",
    "email VARCHAR(100) NOT NULL",
    "password VARCHAR(80) NOT NULL"
])

#add_to_db("test.db", "usuario", {
#    "id": 0,
#    "name": "Lanjar",
#    "email": "Lanjar@hotmail.com",
#    "password": "12345678"
#})

#add_to_db("test.db", "usuario", {
#    "id": 1,
#    "email": "Jarlan@hotmail.com",
#    "password": "12345678"
#})

#print("LISTAR USUÁRIOS")
#con = sqlite3.connect("test.db")
#cursor = con.cursor()
#cursor.execute("SELECT * FROM usuario;")
#for linha in cursor.fetchall():
#    print("--------------------------")
#    print("Id:", linha[0])
#    print("Nome:", linha[1])
#    print("Email:", linha[2])
#    print("Senha:", linha[3])
#    print("--------------------------")
#con.close()
