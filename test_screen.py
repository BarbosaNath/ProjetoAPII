from PySimpleGUI import Window, Button, Text, Column, VerticalSeparator
import PySimpleGUI as sg
from PIL import Image
import tags
import modules as mod
from functions import swap_columns

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

layout_central=[ [VerticalSeparator(),sg.Image(resize('res/logo',.6))] ]

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

choose_modules=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Qual tipo de produto irá trabalhar?')]]

modules=dict()
for module in mod.get_all_modules():
    funcao_foda=lambda window:swap_columns(window,'modulos', f'modulo_{module}', 'col_central')
    choose_modules.append([Button(module.capitalize(), key=funcao_foda)])
    funcao_2=lambda window:swap_columns(window, f'modulo_{module}', 'modulos', 'col_central')
    modules[module]=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [sg.Push()],
    [Button(f'Adicionar {module.capitalize()}', k=f'adicionar_{module}')],
    [Text('Filtros:', size=(10,1))],
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
    [Button('Menu Principal', key=funcao_2)]
]

choose_modules.append([Button('Cadastrar modulo')])
choose_modules.append([sg.VPush()])
choose_modules.append([Button('Voltar', button_color=('white','purple'))])

modulo_roupas=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [sg.Push()],
    [Button('Adicionar Roupas',k='adicionar_roupas')],
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

adicionar_produtos=[
    [sg.Image(filename=resize('icone',0.1)), Button('Log Out', button_color=('white','purple'))],
    [Text('Adicione um produto:')],
    [sg.Input(s=15)],
    [sg.Push()],
    [Text('Atribua filtros a esse produto:')]]
for group in tags.get_all_groups():
    adicionar_produtos.append([sg.Text(group.capitalize()+':')])
    for tag in tags.get_tag_group(group):
        adicionar_produtos.append([sg.Text(s=2), sg.Checkbox(tag)])
adicionar_produtos.append([Button('Adicionar')])

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
