import database.database as db
    
def create_product(database_file, product_name, data):
    db.create_table(database_file, product_name, data)

def remove_product(database_file, product_name):
    db.remove_table(database_file, product_name)

def get_product(database_file, product_name):
    return db.get_table_as_dict(database_file, product_name, "id")

def edit_product(database_file, product_name, what, to, where):
    db.edit_element(database_file, product_name, what, to, where)
