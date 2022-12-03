from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from PIL import Image
import tags
import modules as mod
from functions import *
from image_manipulation import resize

from filters_layouts import *
from module_layouts import *
from start_layouts import *


sg.LOOK_AND_FEEL_TABLE['FotoShopping'] = {
                                        'BACKGROUND': '#f6fcff',
                                        'TEXT':       '#000000',
                                        'INPUT':      '#ffffff',
                                        'TEXT_INPUT': '#000000',
                                        'SCROLL':     '#f6fcff',
                                        'BUTTON':    ('#f6fcff', '#4d3efc'),
                                        'PROGRESS':  ('#f6fcff', '#4d3efc'),
                                        'BORDER': 1,
                                        'SLIDER_DEPTH': 0, 
                                        'PROGRESS_DEPTH': 0, }
# set the default theme to our own
sg.theme("FotoShopping")








layout=[
    [Column(tela_inicial, key='tela_inicial', s=(210,500)),
    Column(choose_modules, key='modulos', s=(210,500), visible=False),
    Column(layout_central, key='col_central'),
    #Column(modulo_roupas, key='modulo_roupas', s=(210,500), visible=False),
    Column(cadastro_modulo, key='cadastro_modulo', s=(210,500), visible=False),
    Column(cadastrar_filtros, key='cadastrar_filtros', s=(210,500), visible=False),
    Column(consultar_filtros, key='consultar_filtros', s=(210,500), visible=False),
    Column(tela_login, key='tela_login', s=(210,500), visible=False),
    Column(adicionar_produtos, key='adicionar_produtos', scrollable=True, vertical_scroll_only=True, s=(210,500), visible=False),
    ]
]

for module in modules:
    layout[0] += [Column(modules[module], key=f'modulo_{module}', s=(210,500), visible=False)]

window = Window(
    'Tela principal',
    layout=layout
)

while True:
    event, values = window.read()
    if event == 'Roupas':
        swap_columns(window,'modulos', 'modulo_roupas','col_central')
    elif event == 'Menu Principal':
        swap_columns(window,'modulo_roupas', 'modulos','col_central')
    elif event == 'Cadastrar modulo':
        swap_columns(window,'modulos', 'cadastro_modulo','col_central')
    elif event == 'inicio':
        swap_columns(window,'cadastro_modulo', 'modulos','col_central')
    elif event == 'Produtos':
        swap_columns(window,'tela_inicial', 'modulos','col_central')
    elif event == 'Voltar':
        swap_columns(window,'modulos', 'tela_inicial','col_central')
    elif event == 'Cadastrar Filtro':
        swap_columns(window,'tela_inicial', 'cadastrar_filtros','col_central')
    elif event == 'frente':
        swap_columns(window,'cadastrar_filtros', 'tela_inicial','col_central')
    elif event == 'Consultar Filtros':
        swap_columns(window,'tela_inicial', 'consultar_filtros','col_central')
    elif event == 'retornar':
        swap_columns(window,'consultar_filtros', 'tela_inicial','col_central')
    elif event == 'sair':
        swap_columns(window,'tela_inicial', 'tela_login','col_central')
    elif event == 'proceed_login':
        [sg.popup('Olá (Usuario), Bem-vindo ao Foto Shopping')],
        swap_columns(window,'tela_login', 'tela_inicial','col_central')
    elif event == 'adicionar_roupas':
        swap_columns(window,'modulo_roupas', 'adicionar_produtos','col_central')
    elif callable(event):
        event(window)

    elif event == sg.WIN_CLOSED:
        break

window.close()

#eu sou lindo
