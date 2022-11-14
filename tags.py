import database.database as db
    

def get_all_groups():
    return db.get_all_tables("database/tag_groups.db")


def create_tag_group(tag_group_name, data):
    db.create_table("database/tag_groups.db", tag_group_name, data)


def remove_tag_group(tag_group_name):
    db.remove_table("database/tag_groups.db", tag_group_name)


def get_tag_group(tag_group_name):
    return db.get_table("database/tag_groups.db", tag_group_name)


def edit_tag_group(tag_group_name, what, to, where):
    db.edit_element("database/tag_groups.db", tag_group_name, what, to, where)


def add_tags_to_group(tag_group_name, tag):
    db.add_to_db("database/tag_groups.db", tag_group_name, {"tag": tag})
    
    

if __name__ == "__main__":
    create_tag_group("tamanho", ["tag TEXT NOT NULL PRIMARY KEY"])
    create_tag_group("cor"    , ["tag TEXT NOT NULL PRIMARY KEY"])

    add_tags_to_group("cor",   "branco")
    add_tags_to_group("cor",    "preto")
    add_tags_to_group("cor", "vermelho")
    add_tags_to_group("cor",     "azul")

    print(get_all_groups())
    
    print(get_tag_group("tamanho"))
    print(get_tag_group("cor"))
