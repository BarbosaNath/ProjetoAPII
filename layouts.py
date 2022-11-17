import PySimpleGUI as sg
from functions import resize
from math import ceil
import tags

# set the default theme to "Reddit"
sg.theme("Reddit")
# Debug(sg.theme("DarkGrey2")) # Exemplo de Debug()


bg_left  = [[sg.Image(resize('res/bglphb', .1),pad=(0,0))]]
bg_right = [[sg.Image(resize('res/bgrphb', .1),pad=(0,0))]]


# Login ---------------------------------------------------------------------------------------
# X---------------------------------------------X
# | Usuário: [                                ] |
# | Senha:   [                                ] |
# | [Entrar] [Cancelar] [Não possui uma conta?] |
# X---------------------------------------------X
login = [[sg.Text("Usuário:", size=(10, 1)), sg.InputText('', key='login_user')],
         [sg.Text("Senha:"  , size=(10, 1)), sg.InputText('', key='login_password', password_char='•')],
         [sg.Button("Entrar", key='proceed_login', border_width=0, size=(7, 1)),sg.Button("Cancelar", border_width=0, size=(7, 1)),sg.Button("Não possui uma conta?",key='create_account',border_width=0,button_color=('DodgerBlue3', 'white'))]]


#Criar conta------------------------------------------------------------------------------------
# X-----------------------------X
# | Usuário:         [        ] |
# | E-mail:          [        ] |
# | Senha:           [        ] |
# | Confirmar Senha: [        ] |
# |  [Criar conta]   [Cancelar] |
# X-----------------------------X
create_account = [[sg.Text("Usuário:", size=(15, 1)), sg.InputText('', key='create_user')], 
                  [sg.Text("E-mail:", size=(15, 1)),  sg.InputText('', key='create_email')],
                  [sg.Text("Senha:", size=(15, 1)),   sg.InputText('', key='create_password',password_char='•')],
                  [sg.Text("Confirmar senha:", size=(15, 1)),sg.InputText('',key='create_repeat_password',password_char='•')],
                  [sg.Button("Criar conta", border_width=0),sg.Button("Cancelar",key='back_to_login-A',border_width=0)]]

# ---------------------------------------------------------------------------------------
#Menu de opções
main_menu = [[sg.Button("Log out",key='back_to_login-B')],
            [sg.FileBrowse()]]



# Tela de Cadastro de Produtos -----------------------------------------------------
# x------------------------------------------x
# | Tipo do produto:  [                    ] |
# | Tipos de tags:    [ ] tipo 1  [ ] tipo 2 |
# |                   [ ] tipo 3  [ ] tipo N |
# x------------------------------------------x

def register_product():
    tag_groups = tags.get_all_groups()
    register = [ 
        [sg.Text("Tipo de Produto:"), sg.InputText('', key='type_product')],
        [sg.Text("Tipos de tags:")],
    ]

    linhas = ceil(len(tag_groups) / 4)
    for j in range(linhas):
        register.append([sg.Checkbox(group.replace("_", " ").capitalize(), s=(10,1)) for i, group in enumerate(tag_groups) if i % linhas == j])
        

    register.append([sg.Button("Enviar"), sg.Button("Cancelar")])

    return register

if __name__ == "__main__":
    window = sg.Window("Teste", register_product())

    while True:
        event, value = window.read()
        if event == sg.WIN_CLOSED or event == "Cancelar": break
    
    window.close()
