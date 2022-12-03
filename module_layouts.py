import PySimpleGUI as sg
from image_manipulation import resize
from functions import *
import modules as mod
import tags

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

# --------------------------------------------------------------------------------------------------------------------------#

choose_modules=[
    gerar_botao_logout('modulos'),
    [sg.Text('Qual tipo de produto irá trabalhar?')]]

# --------------------------------------------------------------------------------------------------------------------------#

modules=dict()
for module in mod.get_all_modules():
    choose_modules.append([Botao(module.capitalize(), 'modulos',  f'modulo_{module}')])

    modules[module]=[
    gerar_botao_logout(f'modulo_{module}'),
    [sg.Push()],
    [sg.Button(f'Adicionar {module.capitalize()}', k=f'adicionar_{module}')],
    [sg.Text('Filtros:', size=(10,1))],
    [sg.Text("Tamanhos:")],
    [sg.Combo(
                tags.get_tag_group('tamanho'),
                s=(15, 22),
                enable_events=True,
                readonly=True,
                k='Tamanho',
            ),
    ],
    [sg.Text('Cores')],
    [sg.Combo(
                tags.get_tag_group('cor'),
                s=(15, 22),
                enable_events=True,
                readonly=True,
                k='Cor',
            ),
    ],
    [sg.Push()],
    [sg.Button("Pesquisar")],
    [Botao('Menu Principal',  f'modulo_{module}', 'modulos')]
]

choose_modules.append([sg.Button('Cadastrar modulo')])
choose_modules.append([sg.VPush()])
choose_modules.append([sg.Button('Voltar', button_color=('white','purple'))])

# --------------------------------------------------------------------------------------------------------------------------#

cadastro_modulo=[
    gerar_botao_logout('cadastro_modulo'),
    [sg.Text('Cadastre o tipo de produto')],
    [sg.Text('Tipo:'), sg.Input(s=15)],
    [sg.Text('Defina os filtros a serem ultilizados:')],
    [sg.Checkbox('Tamanhos'), sg.Checkbox('Modelos')],
    [sg.Checkbox('Cores'), sg.Checkbox('Sexo')],
    [sg.Button('Cadastrar filtro')],
    [sg.Push()],
    [sg.Button('Criar')],
    [sg.Button('Menu Principal', key='inicio')]
]

# --------------------------------------------------------------------------------------------------------------------------#

adicionar_produtos=[
    gerar_botao_logout('adicionar_produtos'),
    [sg.Text('Adicione um produto:')],
    [sg.Input(s=15)],
    [sg.Push()],
    [sg.Text('Atribua filtros a esse produto:')]]
for group in tags.get_all_groups():
    adicionar_produtos.append([sg.Text(group.capitalize()+':')])
    for tag in tags.get_tag_group(group):
        adicionar_produtos.append([sg.Text(s=2), sg.Checkbox(tag)])
adicionar_produtos.append([sg.Button('Adicionar')])
adicionar_produtos.append([sg.Button("Voltar", key=lambda window: trocar_tela(window, "adicionar_produto", "modulos"))])