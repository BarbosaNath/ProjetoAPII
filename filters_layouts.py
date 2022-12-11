import PySimpleGUI as sg
from image_manipulation import resize
import tags
from functions import gerar_botao_logout, Botao

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
    _filtros = [
        gerar_botao_logout('consultar_filtros'),
        [sg.Text('Filtros disponiveis:')]
    ]

    for group in tags.get_all_groups():
        _filtros.append([sg.Text(group.capitalize()), sg.Push(), sg.Button('➕', k=("adicionar_ao_grupo", group)), sg.Button("❌", key=tuple(("delete_filter_group", group)), button_color=('white', 'darkred'))])
        for tag in tags.get_tag_group(group):
            tag=tag[0]
            _filtros.append([sg.Text('    ▸ '+tag.capitalize()), sg.Push(), sg.Button('⌫', key=tuple(("delete_filter", group, tag)), button_color=('white', 'darkred'))])
    _filtros.append([sg.Button('Adicionar grupo de filtros', k="botao_adicionar_grupo", button_color=('white', 'green'), s=24)])
    _filtros.append([Botao('Voltar', 'consultar_filtros', 'tela_inicial', s=24)])
    return _filtros

# --------------------------------------------------------------------------------------------------------------------------#

def cadastrar_grupo_filtros():
    _cadastrar_grupo_filtros=[
        gerar_botao_logout('cadastrar_grupo_filtros'),
        [sg.Text('Qual grupo de filtros deseja criar?')],
        [sg.Text('Grupo:'), sg.Input(s=15, key="create_new_tag_group_name")],
        [sg.VPush()],
        [sg.Button('Adicionar', key="submit_create_tag_group", button_color=('white', 'green'), s=17), Botao('Voltar', "tela_cadastrar_grupo_filtro", "consultar_filtros", s=5)]
    ]
    return _cadastrar_grupo_filtros

# --------------------------------------------------------------------------------------------------------------------------#

def cadastrar_filtro():
    _cadastrar_filtro=[
        gerar_botao_logout('cadastrar_filtro'),
        [sg.Text('Selecione o grupo de deseja adicionar um filtro:')],
        [sg.Text('Grupo:'), sg.Combo( tags.get_all_groups(), k="combo_cadastro_filtro", s=(15, 22), enable_events=True, readonly=True)],
        [sg.VPush()],
        [sg.Text('Qual filtro deseja adicionar a esse grupo?')],
        [sg.Input(s=15, k="nome_novo_filtro")],
        [sg.VPush()],
        [sg.Button('Adicionar', key="submit_cadastro_filtro", button_color=('white', 'green'), s=17), Botao('Voltar', "tela_cadastrar_filtro", "consultar_filtros", s=5)]
    ]
    return _cadastrar_filtro

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
