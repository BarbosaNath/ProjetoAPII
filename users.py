import database.database as db

def is_user_in_db(login_user, login_password):
    # pra pegar a lista de usuarios cadastrados, usa a função db.get_table("arquivo.db", "usuario")
    # se voce usar a função db.get_table_as_dict("arquivo.db", "usuario", "id")
    # dit[id=1]["usuario"]
    usuarios = db.get_table_as_dict("database/test.db", "usuario", "id")
    for id in usuarios:
        if usuarios[id]["name"] == login_user:
            if usuarios[id]["password"] == login_password:
                return True

    return False
