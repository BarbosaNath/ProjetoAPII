import database.database as db
    
def create_module(database_file, module_name, data):
    db.create_table(database_file, module_name, data)

def remove_module(database_file, module_name):
    db.remove_table(database_file, module_name)

def get_module(database_file, module_name):
    return db.get_table_as_dict(database_file, module_name, "id")

def edit_module(database_file, module_name, what, to, where):
    db.edit_element(database_file, module_name, what, to, where)
