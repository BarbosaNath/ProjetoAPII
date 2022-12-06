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
        [sg.Text("Usuário:", size=(10, 1)), sg.InputText('', key='login_user')],
        [sg.Text("Senha:"  , size=(10, 1)), sg.InputText('', key='login_password', password_char='•')],
        [sg.Button("Entrar", key='proceed_login', border_width=0, size=(7, 1)),sg.Button("Cancelar", key="buton_cancel_login", border_width=0, size=(7, 1))],
        [sg.Button("Criar conta", key="button_create_acc", border_width=0, size=(9, 1))]
    ]

def tela_inicial():
    return [
        [sg.Text('Bem Vindo!')],
        [sg.Image(filename=resize('icone.png',0.1)), sg.Button('Log Out', key='sair', button_color=('white','purple'))],
        [sg.Button('Produtos')],
        [sg.Button('Consultar Filtros')],
        # [sg.Button('Cadastrar Filtro')],
    ]
#-------------------------------------------------------------------------------------------------------
def layout_central():
    return [ [sg.VerticalSeparator(),sg.Image(resize('res/logo.png',.6))] ]
#-------------------------------------------------------------------------------------------------------
def create_acc():
    return [[sg.Text("Usuário:", size=(15, 1)), sg.InputText('', key='create_user')],
                  [sg.Text("Senha:", size=(15, 1)),   sg.InputText('', key='create_password',password_char='•')],
                  [sg.Text("Confirmar senha:", size=(15, 1)),sg.InputText('',key='create_repeat_password',password_char='•')],
                  [sg.Button("Criar conta", key="submit_create_acc", border_width=0),sg.Button("Cancelar",key='cancel_submit_create_acc',border_width=0)]]
