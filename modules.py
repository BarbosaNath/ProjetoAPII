import database.database as db

def create_module(module_name):
    db.create_table('database/modules.db', module_name, ['code TEXT NOT NULL PRIMARY KEY','tag_groups TEXT'])

def get_all_modules():
    return db.get_all_tables("database/modules.db")

def remove_module(module_name):
    db.remove_table('database/modules.db', module_name)

def get_module(module_name):
    return db.get_table_as_dict('database/modules.db', module_name, "id")

def edit_module(module_name, what, to, where):
    db.edit_element('database/modules.db', module_name, what, to, where)

def get_tags(module_name):
    return [tag for tag in db.get_table_as_dict('database/modules.db', module_name, "id")['tag_groups'].split()]

#def add_tag(module_name, tag):
#    db.edit_element('database/modules.db', module_name, 'tag_groups', ' '.join(get_tags(module_name).append(tag)), wh

create_module('roupas')