import PySimpleGUI as sg
from image_manipulation import resize

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

def tela_login():
    return [
        [sg.Image(filename=resize('icone.png',0.1)), sg.Text('Seja Bem-Vindo')],
        [sg.Text("Usuário:", size=6), sg.InputText(key='login_user', s=18)],
        [sg.Text("Senha:"  , size=6), sg.InputText(key='login_password', password_char='•', s=18)],
        [sg.Button("Entrar", key='proceed_login', border_width=0, size=15), sg.Button("Cancelar", key="buton_cancel_login", button_color=('white','purple') ,border_width=0, size=7)],
        [sg.Button("Criar conta", key="button_create_acc", border_width=0, button_color=("#4d3efc", "#f6fcff"))]
    ]

def tela_inicial():
    return [
        [sg.Image(filename=resize('icone.png',0.1)), sg.Button('Log Out', key='sair', button_color=('white','purple'))],
        [sg.Sizer(v_pixels=50)],
        [sg.Button('Módulos', s=24, k='Produtos')],
        [sg.Button('Filtros',  s=24, k='Consultar Filtros')],
        # [sg.Button('Cadastrar Filtro')],
    ]
#-------------------------------------------------------------------------------------------------------
def layout_central():
    return [ [sg.VerticalSeparator(),sg.Image(resize('res/logo.png',.6))] ]
#-------------------------------------------------------------------------------------------------------
def create_acc():
    return [[sg.Text("Usuário:", size=6), sg.InputText(key='create_user')],
            [sg.Text("Senha:", size=6), sg.InputText(key='create_password', password_char='•')],
            [sg.Button("Criar conta", key="submit_create_acc", s=15),sg.Button("Cancelar",key='cancel_submit_create_acc', s=7, button_color=("white", "purple"))]]
