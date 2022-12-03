import database.database as db
db_path="database/images.db"
db_table="images"

def create_db():
    db.create_table(db_path, db_table, [
        "product_code TEXT NOT NULL PRIMARY KEY",
        "path TEXT NOT NULL"
    ])

def get_images():
    images = dict()
    for key, value in db.get_table_as_dict(db_path, db_table, "product_code").items() :
        images[key] = value["path"]
    return images

def add_image(product_code):
    db.add_to_db(db_path, db_table, {"product_code": product_code, "path": f"database/images/{product_code}.png"})


# Create table
create_db()
# Main
if __name__ == "__main__":
    images = get_images ()