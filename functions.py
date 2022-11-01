# need to install pillow on pip
import Image # on linux 
# from PIL import Image # on windows

# unused
# Não entendo como funciona, so copiei do stack overflow. Ass: Math
def select_text_on_focus(event, canvas, key, text):
    '''Add the function to select text every time you click on  asg.InputText()'''

    if canvas[key].get() == '':
        canvas[key].update(value=text)
    canvas[key].update(select=True)


# unused
# Não entendo como funciona, so copiei do stack overflow. Ass: Math
def update_selection(canvas, key, text):
    '''Used to apply the select_text_on_focus() on an especific sg.InputText()'''

    canvas[key].Widget.bind("<FocusIn>", lambda event: select_text_on_focus(event, canvas, key, text))
    canvas[key].update(select=True)




def resize(image: str, ratio: float) -> str:
    '''resize and returns an image
       image: str -> Path to the image (DO NOT INCLUDE THE EXTENSION).
       ratio: float -> How much do you want to resize. Should be a fraction of 100 (i.e.: 10/100).
        '''
    im = Image.open(image+".png")
    size = int(im.width*ratio), int(im.height*ratio) # calculates what the size of image should be based on the image and ratio provided
    im.thumbnail(size) # resize image based on $size
    im.save(image+"_res.png", "PNG") # image must be saved on drive unfortunately 
    return image+"_res.png" # since the usecase needs a path to the image, then it is provided here

def get_size_reduce(image, ratio) -> tuple:
    ''' Returns the size of the image provided after the ratio is  applied.
        image: str -> Path to the image (INCLUDE THE EXTENSION).
        ratio: float -> How much do you want to resize. Should be a fraction of 100 (i.e.: 10/100).
        '''

    image = Image.open(image)
    return (int(image.width*ratio), int(image.height*ratio))