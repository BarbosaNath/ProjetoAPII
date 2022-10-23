import Image

def select_text_on_focus(event, canvas, key, text):
    if canvas[key].get() == '':
        canvas[key].update(value=text)
    canvas[key].update(select=True)

def update_selection(canvas, key, text):
    canvas[key].Widget.bind("<FocusIn>", lambda event: select_text_on_focus(event, canvas, key, text))
    canvas[key].update(select=True)

def resize(image, ratio):
    im = Image.open(image+".png")
    size = int(im.width*ratio), int(im.height*ratio)
    im.thumbnail(size)
    im.save(image+"_res.png", "PNG")
    return image+"_res.png"

def get_size_reduce(image, percentage):
    image = Image.open(image)
    return (int(image.width*(percentage/100)), int(image.height*(percentage/100)))