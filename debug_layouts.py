import PySimpleGUI as sg
import database.database as db
from functions import swap_columns
# Main ---------------------------------------------------------------------------------------
# X-------------------------X
# | [Mostrar DB] [Cancelar] |
# X-------------------------X
main = [[sg.Button("Mostrar DB", key=lambda window: swap_columns(window, "col-main", "col-show"), border_width=0, size=(7, 1)), sg.Button("Cancelar", key="cancel", border_width=0, size=(7, 1))]]
def generate_main():
    return [[sg.Button("Mostrar DB", key=lambda window: swap_columns(window, "col-main", "col-show"), border_width=0, size=(7, 1)), sg.Button("Cancelar", key="cancel", border_width=0, size=(7, 1))]]


# Show DataBase ------------------------------------------------------------------------------
# X--------------------X
# | text text ... text |
# | text text ... text |
# | ...  ...  ... ...  |
# | text text ... text |
# X--------------------X
def update_show(column):
    show = []
    
    for e in db.get_table("database/test.db", "usuario"):
        show.append([])
        for i in e:
            show[len(show)-1].append(sg.Text(f"{i}", size=(7, 1)))
            
    show.append([ sg.Button("Voltar",    key=lambda window: swap_columns(window, column, "col-main"), border_width=0, size=(7, 1)),
                  sg.Button("Atualizar", key="update", border_width=0, size=(7, 1))
    ])
    return show
