# need to install pillow on pip
from PIL import Image
import PySimpleGUI as sg
from image_manipulation import resize

def swap_columns(window, column1, column2, column3=None):
    window[column1].update(visible=False)
    window[column2].update(visible=True)
    if column3 is not None: swap_columns(window, column3, column3)

trocar_tela  = lambda window, x, y: swap_columns(window, x, y, 'col_central')
swap_screens = lambda window, x, y: swap_columns(window, x, y, 'col_central')
Botao        = lambda   name, x, y: sg.Button(name, k=lambda window: trocar_tela(window, x, y))

def gerar_botao_logout(current_column):
    return [sg.Image(filename=resize('icone.png',0.1)), sg.Button('Log Out', key=lambda window: trocar_tela(window, current_column, 'tela_login') , button_color=('white','purple'))]
