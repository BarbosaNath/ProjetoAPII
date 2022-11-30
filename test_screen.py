from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from PIL import Image
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

def swap_columns(window, column1, column2):
    window[column1].update(visible=False)
    window[column2].update(visible=True)

tela_login=[
    [sg.Image(filename=resize('icone',0.1)), Text('Seja Bem-Vindo')],
    [sg.Push()],
    [sg.Text("Usuário:", size=(10, 1)), sg.InputText('', key='login_user')],
    [sg.Text("Senha:"  , size=(10, 1)), sg.InputText('', key='login_password', password_char='•')],
    [sg.Push()],
    [sg.Button("Entrar", key='proceed_login', border_width=0, size=(7, 1)),sg.Button("Cancelar", border_width=0, size=(7, 1))],
    [sg.Button("Criar conta", border_width=0, size=(9, 1))]
]
    
tela_inicial=[
    [Text('Bem Vindo!')],
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', key='sair', button_color=('white','purple'))],
    [Button('Produtos')],
    [sg.Push()],
    [Button('Consultar Filtros')],
    [sg.Push()],
    [Button('Cadastrar Filtro')],
]

modulos=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Qual tipo de produto irá trabalhar?')],
    [Button('Roupas')],
    [Button('Cadastrar modulo')],
    [sg.Push()],
    [Button('Voltar', button_color=('white','purple'))],
]

layout_central=[ [VerticalSeparator(),sg.Image(resize('res/logo',.6))] ]

modulo_roupas=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [sg.Push()],
    [Button('Adicionar Roupas')],
    [Text('Filtros:', size=(10,1)), ],
    [sg.Text("Tamanhos:")],
    [sg.Combo(
                tags.get_tag_group('tamanho'),
                s=(15, 22),
                enable_events=True,
                readonly=True,
                k='Tamanho',
            ),
    ],
    [Text('Cores')],
    [sg.Combo(
                tags.get_tag_group('cor'),
                s=(15, 22),
                enable_events=True,
                readonly=True,
                k='Cor',
            ),
    ],
    [sg.Push()],
    [Button("Pesquisar")],
    [Button('Menu Principal')]
]

cadastro_modulo=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Cadastre o tipo de produto')],
    [Text('Tipo:'), sg.Input(s=15)],
    [Text('Defina os filtros a serem ultilizados:')],
    [sg.Checkbox('Tamanhos'), sg.Checkbox('Modelos')],
    [sg.Checkbox('Cores'), sg.Checkbox('Sexo')],
    [Button('Cadastrar filtro')],
    [sg.Push()],
    [Button('Criar')],
    [Button('Menu Principal', key='inicio')]
]

cadastrar_filtros=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Qual grupos de filtros deseja criar?')],
    [Text('Grupo:'), sg.Input(s=15)],
    [sg.Push()],
    [Text('Defina os filtros a serem ultilizados:')],
    [Text('Filtro:'), sg.Input(s=15)],
    [Button('Adicionar')],
    [sg.Push()],
    [Button('Criar Grupo', button_color=('white', 'green'))],
    [sg.Push()],
    [Button('Menu Principal', key='frente')]
]

consultar_filtros=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Filtros disponiveis:')],
    [sg.Combo(
                tags.get_all_groups(),
                s=(15, 22),
                enable_events=True,
                readonly=True,
                k='all_tags',
            ),
    ],
    [sg.Push()],
    [Button('Editar Filtros')],
    [sg.Push()],
    [Button('Voltar', key='retornar')]
]

layout=[
    [Column(tela_inicial, key='tela_inicial', s=(210,500)),
    Column(modulos, key='modulos', s=(210,500), visible=False),
    Column(layout_central, key='col_central'),
    Column(modulo_roupas, key='modulo_roupas', s=(210,500), visible=False),
    Column(cadastro_modulo, key='cadastro_modulo', s=(210,500), visible=False),
    Column(cadastrar_filtros, key='cadastrar_filtros', s=(210,500), visible=False),
    Column(consultar_filtros, key='consultar_filtros', s=(210,500), visible=False),
    Column(tela_login, key='tela_login', s=(210,500), visible=False),
    ]
]

window = Window(
    'Tela principal',
    layout=layout
)

while True:
    event, values = window.read()
    if event == 'Roupas':
        swap_columns(window,'modulos', 'modulo_roupas')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Menu Principal':
        swap_columns(window,'modulo_roupas', 'modulos')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Cadastrar modulo':
        swap_columns(window,'modulos', 'cadastro_modulo')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'inicio':
        swap_columns(window,'cadastro_modulo', 'modulos')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Produtos':
        swap_columns(window,'tela_inicial', 'modulos')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Voltar':
        swap_columns(window,'modulos', 'tela_inicial')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Cadastrar Filtro':
        swap_columns(window,'tela_inicial', 'cadastrar_filtros')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'frente':
        swap_columns(window,'cadastrar_filtros', 'tela_inicial')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'Consultar Filtros':
        swap_columns(window,'tela_inicial', 'consultar_filtros')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'retornar':
        swap_columns(window,'consultar_filtros', 'tela_inicial')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'sair':
        swap_columns(window,'tela_inicial', 'tela_login')
        swap_columns(window,'col_central', 'col_central')
    elif event == 'proceed_login':
        [sg.popup('Olá (Usuario), Bem-vindo ao Foto Shopping')],
        swap_columns(window,'tela_login', 'tela_inicial')
        swap_columns(window,'col_central', 'col_central')
    elif event == sg.WIN_CLOSED:
        break

window.close()

#eu sou lindo
