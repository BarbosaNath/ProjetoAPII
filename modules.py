import database.database as db

db_path = "database/modules.db"

def create_module(module_name):
    db.create_table('database/modules.db', module_name, [
        'code TEXT NOT NULL PRIMARY KEY',
        'tag_groups TEXT',
        'inventory INT'
        ])

def get_all_modules():
    return db.get_all_tables(db_path)

def remove_module(module_name):
    db.remove_table(db_path, module_name)

def get_module(module_name):
    return db.get_table_as_dict(db_path, module_name, "id")

def edit_module(module_name, what, to, where):
    db.edit_element(db_path, module_name, what, to, where)

def get_tags(module_name):
    return [tag for tag in db.get_table_as_dict(db_path, module_name, "id")['tag_groups'].split()]

def add_product(module, code: str, tag_groups: str, inventory: int): 
    db.add_to_db(db_path, module, {
        'code': code,
        'tag_groups': tag_groups,
        'inventory': inventory
        })
   
def decreace_inventory(module_name, code):
    db.edit_element(db_path, module_name, 'inventory', db.get_table_as_dict(db_path, module_name, 'code')[code]['inventory']-1, f'code = {code}')

def change_inventory(module_name, code, inventory):
    db.edit_element(db_path, module_name, 'inventory', inventory, f'code = {code}')


#def add_tag(module_name, tag):
#    db.edit_element('database/modules.db', module_name, 'tag_groups', ' '.join(get_tags(module_name).append(tag)), wh

create_module('roupas')
create_module('perfumes')
create_module('esmaltes')
create_module('fim')