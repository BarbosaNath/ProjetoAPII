import database.database as db

db_path = "database/modules.db"

def create_module(module_name, tag_groups):
    db.create_table('database/modules.db', module_name, [
        'code TEXT NOT NULL PRIMARY KEY',
        'image TEXT', 
        'tags TEXT',
        'inventory INT'
        ])
    db.create_table(db_path, 'modules', ['name TEXT NOT NULL PRIMARY KEY','tag_groups TEXT'])
    db.add_to_db(db_path, 'modules', {'name' : module_name, 'tag_groups': tag_groups})

def get_all_modules():
    _temp = db.get_all_tables(db_path)
    _temp.remove('modules')
    return _temp

def remove_module(module_name):
    db.remove_table(db_path, module_name)
    db.remove_element_where(db_path, 'modules', 'name', f"'{module_name}'")

def get_module(module_name, image=False):
    return db.get_table_as_dict(db_path, module_name, 'code' if not image else 'image')

def edit_module(module_name, what, to, where):
    db.edit_element(db_path, module_name, what, to, where)

def get_tags(module_name):
    return [tag for tag in db.get_table_as_dict(db_path, 'modules', 'name')[module_name]['tag_groups'].split()]

def add_product(module, code, image, tags, inventory): 
    db.add_to_db(db_path, module, {
        'code': code,
        'image' : image,
        'tags' : tags,
        'inventory': inventory
        })

def decreace_inventory(module_name, code):
    db.edit_element(db_path, module_name, 'inventory', db.get_table_as_dict(db_path, module_name, 'code')[code]['inventory']-1, f'code = {code}')

def change_inventory(module_name, code, inventory):
    db.edit_element(db_path, module_name, 'inventory', inventory, f'code = {code}')


#def add_tag(module_name, tag):
#    db.edit_element('database/modules.db', module_name, 'tag_groups', ' '.join(get_tags(module_name).append(tag)), wh


if __name__ == '__main__':
    create_module('roupas', 'tamanho cor')
    create_module('perfumes', 'tamanho')
    create_module('esmaltes', 'cor')
