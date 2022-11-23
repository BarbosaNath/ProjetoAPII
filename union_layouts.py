import tags, products
import PySimpleGUI as sg
from   PySimpleGUI        import Window, Button, Text, Column, VerticalSeparator
from   image_manipulation import resize
from   functions          import swap_columns
from   union_functions    import *



# Creatring a custom theme
sg.LOOK_AND_FEEL_TABLE['FotoShopping'] = {  'BACKGROUND': '#f6fcff',
                                            'TEXT':       '#000000',
                                            'INPUT':      '#ffffff',
                                            'TEXT_INPUT': '#000000',
                                            'SCROLL':     '#f6fcff',
                                            'BUTTON':    ('#f6fcff', '#4d3efc'),
                                            'PROGRESS':  ('#f6fcff', '#4d3efc'),
                                            'BORDER': 1,
                                            'SLIDER_DEPTH': 0, 
                                            'PROGRESS_DEPTH': 0, 
                                          }
# set the default theme to our own
sg.theme("FotoShopping")


icone = resize('icone.png',    40)
logo  = resize('res/logo.png', 500)


layout_central=[ [VerticalSeparator(),sg.Image(logo)] ]

# Layout da tela inicial --------------------------------------------------------------------------------------------------------------------------------------
# X-------------------------------------X
# | Bem Vindo!                          |
# | |img| [Log Out]                     |
# | [Produtos]                          |
# | [Consultar Filtros]                 |
# | [Cadastrar Filtros]                 |
# X-------------------------------------X
tela_inicial=[  [Text('Bem Vindo!')],
                [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                [botao(         'Produtos', 'tela_inicial',           'modulos')],
                [botao('Consultar Filtros', 'tela_inicial', 'consultar_filtros')],
                [Button('Cadastrar Filtro')],
              ]


# Layout de Modulos -------------------------------------------------------------------------------------------------------------------------------------------
# X-------------------------------------X
# | |img| [Log Out]                     |
# | Qual tipo de produto irá trabalhar? |
# | [Tipo1]                             |
# | [Tipo2]                             |
# | ...                                 |
# | [TipoN]                             |
# | [Cadastrar novo modulo] [Voltar]    |
# X-------------------------------------X
menu_modulos=[  [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                [Text('Qual tipo de produto irá trabalhar?')]  ]

popular(menu_modulos, products.get_all_products(), lambda i: Button(i.capitalize(), k=lambda window: trocar_tela(window, 'modulos', f'modulo_{i}')))

menu_modulos.append([botao('Cadastrar modulo', 'modulos', 'cadastro_modulo'), Button('Voltar', k=lambda window: trocar_tela(window, 'modulos', 'tela_inicial'), button_color=('white','purple'))])


# Layout de Modulo Especifico ---------------------------------------------------------------------------------------------------------------------------------
modulos = {}
for modulo in products.get_all_products():
    modulos[modulo] = [ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                        [Text('Filtros:', size=(10,1))]  ]

    for grupo in tags.get_all_groups():
        modulos[modulo].append([sg.Text(f'{grupo.capitalize()}: ', s=(8, 1)), 
                                sg.Combo(tags.get_tag_group(grupo), s=(15, 22), enable_events=True, readonly=True, k=f'combo-{grupo}')])
    modulos[modulo].append([Button("Pesquisar")])
    modulos[modulo].append([botao('Menu Principal', f"modulo_{modulo}", 'modulos')])


# Layout de Cadastro de Módulo --------------------------------------------------------------------------------------------------------------------------------
cadastro_modulo=[   [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Cadastre o tipo de produto')],
                    [Text('Tipo:'), sg.Input(s=15)],
                    [Text('Defina os filtros a serem ultilizados:')]    ]

cadastro_modulo += gerar_checkboxes(tags.get_all_groups(), 2) + \
                [  [botao ('Cadastrar filtro', 'cadastro_modulo', 'cadastrar_filtros')],
                   [Button('Criar')],
                   [botao ('Menu Principal', 'cadastro_modulo', 'modulos')]  ]


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
cadastrar_filtros=[ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Qual grupos de filtros deseja criar?')],
                    [Text('Grupo:'), sg.Input(s=15)],
                    [Text('Defina os filtros a serem ultilizados:')],
                    [Text('Filtro:'), sg.Input(s=15)],
                    [Button('Adicionar')],
                    [Button('Criar Grupo', button_color=('white', 'green'))],
                    [botao('Menu Principal', 'cadastrar_filtros', 'tela_inicial')]
                   ]


consultar_filtros=[ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Filtros disponiveis:')],
                    [sg.Combo(tags.get_all_groups(), s=(15, 22), enable_events=True, readonly=True,  k='all_tags')],
                    [Button('Editar Filtros')],
                    [botao('Voltar', 'consultar_filtros', 'tela_inicial')]
                   ]
