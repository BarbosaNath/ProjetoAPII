import PySimpleGUI as sg
from image_manipulation import resize
import tags
from functions import gerar_botao_logout

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

def filtros():
    return [
        gerar_botao_logout('col_filtros'),
        [sg.Button('Cadastrar filtro', button_color=('white','green'))],
        [sg.Button('Editar filtro', button_color=('white','blue'))],
        [sg.Button('Consultar filtro', button_color=('white','pink'))],
        [sg.Button('Excluir filtro', button_color=('white','red'))],
        [sg.VPush()],
        [sg.Button('Voltar')],
        [sg.Button('Menu Principal')],
    ]

# --------------------------------------------------------------------------------------------------------------------------#

def cadastrar_filtros():
    _cadastrar_filtros=[
        gerar_botao_logout('cadastrar_filtros'),
        [sg.Text('Qual grupos de filtros deseja criar?')],
        [sg.Text('Grupo:'), sg.Input(s=15)],
        [sg.VPush()],
        [sg.Text('Defina os filtros a serem ultilizados:')],
        [sg.Text('Filtro:'), sg.Input(s=15)],
        [sg.Button('Adicionar')],
        [sg.VPush()],
        [sg.Button('Criar Grupo', button_color=('white', 'green'))],
        [sg.VPush()],
        [sg.Button('Menu Principal', key='frente')]
    ]
    return _cadastrar_filtros

# --------------------------------------------------------------------------------------------------------------------------#

def consultar_filtros():
    _consultar_filtros=[
        gerar_botao_logout('consultar_filtros'),
        [sg.Text('Filtros disponiveis:')],
        [sg.Combo(
                    tags.get_all_groups(),
                    s=(15, 22),
                    enable_events=True,
                    readonly=True,
                    k='all_tags',
                ),
        ],
        [sg.Push()],
        [sg.Button('Editar Filtros')],
        [sg.Push()],
        [sg.Button('Voltar', key='retornar')]
    ]
    return _consultar_filtros
# --------------------------------------------------------------------------------------------------------------------------#

def editar_filtros(): 
    return [
        gerar_botao_logout('consultar_filtros'),
        [sg.Text('Filtros disponiveis:')],
        [sg.Combo(  tags.get_all_groups(),
                    s=(15, 22),
                    enable_events=True,
                    readonly=True,
                    k='all_tags')],

        [sg.Push()],
        [sg.Button('Editar Filtros')],
        [sg.Push()],
        [sg.Button('Voltar', key='retornar')]
    ]