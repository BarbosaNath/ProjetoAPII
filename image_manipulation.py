# Quando for importar, importar ```import image_manipulation as img```
from PIL import Image, ImageFile
import os
from math import ceil
ImageFile.LOAD_TRUNCATED_IMAGES = True

def convert_to_png(image):
    if ".png" in image: return image

    img_png = Image.open(image) 
    img_png.save(image.replace(".jpg", ".png"))

    return image.replace(".jpg", ".png")
    

# eu so queria que tivesse um overload de verdade no python T-T
def resize(path, size, size_=None) -> str: 
    image_name = path.replace(".png", "").split("/")[-1]

    path_to_img = "/".join(path.split("/")[0:-1])

    new_path=f'{path_to_img}/resized/'

    if not os.path.exists(new_path):
        os.mkdir(new_path)

    if   type(size) == int:
        if size_:
            im = Image.open(path)
            new_size = size, size_
            im.thumbnail(new_size)
            new_path = f"{path_to_img}/resized/{image_name}.png"
            im.save(new_path, "PNG")

        else:
            im = Image.open(path)
            ratio = im.width / im.height
            new_size = size, ceil(size*ratio)
            im.thumbnail(new_size)
            new_path = f"{path_to_img}/resized/{image_name}.png"
            im.save(new_path, "PNG")

    elif type(size) == float:
        im = Image.open(path)
        new_size = ceil(im.width*size), ceil(im.height*size)
        im.thumbnail(new_size)
        new_path = f"{path_to_img}/resized/{image_name}.png"
        im.save(new_path, "PNG")

    elif type(size) in [tuple, list]:
        im = Image.open(path)
        new_size = tuple(size)
        im.thumbnail(new_size)
        new_path = f"{path_to_img}/resized/{image_name}.png"
        im.save(new_path, "PNG")


    return new_path



if __name__ == "__main__":
    resize("res/logo.png", (50, 50))
    resize("res/logo.png", [50, 50])
    resize("res/logo.png",      .5 )
    resize("res/logo.png",      50 )
    resize("res/logo.png",  50, 50 )
