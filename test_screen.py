from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from image_manipulation import resize
from functions import swap_columns
import tags

def gerar_checkboxes(filtros, por_linha):
    checkboxes =[]

    for i in range(0, len(filtros), por_linha):
        linha = []

        for j in range(por_linha):
            linha.append(sg.Checkbox(filtros[i+j], s=(7,1), k='cb-filtro-{i=}-{j=}'))

        checkboxes.append(linha)

    return checkboxes


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

trocar_tela = lambda window, x, y: swap_columns(window, x, y, 'col_central')

icone = resize('icone.png',    0.1)
logo  = resize('res/logo.png', 0.5)


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
                [Button('Produtos',          k=lambda window: trocar_tela(window, 'tela_inicial', 'modulos'))],
                [Button('Consultar Filtros', k=lambda window: trocar_tela(window, 'tela_inicial', 'consultar_filtros'))],
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
modulos=[   [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
            [Text('Qual tipo de produto irá trabalhar?')],
            [Button('Roupas',           k=lambda window: trocar_tela(window, 'modulos', 'modulo_roupas'))],
            [Button('Cadastrar modulo', k=lambda window: trocar_tela(window, 'modulos', 'cadastro_modulo')), Button('Voltar',           k=lambda window: trocar_tela(window, 'modulos', 'tela_inicial'), button_color=('white','purple'))],
         ]


# TODO: Fazer isso generico
modulo_roupas=[ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                [Text('Filtros:', size=(10,1))]
               ]

for grupo in tags.get_all_groups():
    modulo_roupas.append([sg.Text(f'{grupo.capitalize()}: ', s=(8, 1)), 
                          sg.Combo(tags.get_tag_group(grupo), s=(15, 22), enable_events=True, readonly=True, k=f'combo-{grupo}')])
modulo_roupas.append([Button("Pesquisar")])
modulo_roupas.append([Button('Menu Principal', k=lambda window: trocar_tela(window, 'modulo_roupas', 'modulos'))])


cadastro_modulo=[   [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Cadastre o tipo de produto')],
                    [Text('Tipo:'), sg.Input(s=15)],
                    [Text('Defina os filtros a serem ultilizados:')]
                 ]
for linha in gerar_checkboxes(tags.get_all_groups(), 2):
    cadastro_modulo.append(linha)

cadastro_modulo.append([Button('Cadastrar filtro', k=lambda window: trocar_tela(window, 'cadastro_modulo', 'cadastrar_filtros'))])
cadastro_modulo.append([Button('Criar')])
cadastro_modulo.append([Button('Menu Principal',   k=lambda window: trocar_tela(window, 'cadastro_modulo', 'modulos'))])


cadastrar_filtros=[ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Qual grupos de filtros deseja criar?')],
                    [Text('Grupo:'), sg.Input(s=15)],
                    [Text('Defina os filtros a serem ultilizados:')],
                    [Text('Filtro:'), sg.Input(s=15)],
                    [Button('Adicionar')],
                    [Button('Criar Grupo', button_color=('white', 'green'))],
                    [Button('Menu Principal', k=lambda window: trocar_tela(window, 'cadastrar_filtros', 'tela_inicial'))]
                   ]


consultar_filtros=[ [sg.Image(icone), Button('Log Out', button_color=('white','purple'))],
                    [Text('Filtros disponiveis:')],
                    [sg.Combo(tags.get_all_groups(), s=(15, 22), enable_events=True, readonly=True,  k='all_tags')],
                    [Button('Editar Filtros')],
                    [Button('Voltar', k=lambda window: trocar_tela(window, 'consultar_filtros', 'tela_inicial'))]
                   ]


layout=[ [  Column(tela_inicial,      k='tela_inicial',      s=(210,500)),
            Column(modulos,           k='modulos',           s=(210,500), visible=False),
            Column(modulo_roupas,     k='modulo_roupas',     s=(210,500), visible=False),
            Column(cadastro_modulo,   k='cadastro_modulo',   s=(210,500), visible=False),
            Column(cadastrar_filtros, k='cadastrar_filtros', s=(210,500), visible=False),
            Column(consultar_filtros, k='consultar_filtros', s=(210,500), visible=False),
            Column(layout_central,    k='col_central'),
          ]
        ]


window = Window('Tela principal', layout=layout)


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED: break
    elif callable(event):
        event(window)

window.close()
