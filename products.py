import database.database as db
    
def create_product(product_name):
    db.create_table("database/products.db", product_name, [
        "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT",
        "tag_groups TEXT"
    ])
def remove_product(product_name):
    db.remove_table("database/products.db", product_name)

def get_product(product_name):
    return db.get_table_as_dict("database/products.db", product_name, "id")

def get_all_products():
    return db.get_all_tables("database/products.db")

def edit_product(product_name, what, to, where):
    db.edit_element("database/products.db", product_name, what, to, where)
