# Essas funções servem basicamente pra não poluir o programa quando ele for """lançado"""
DEBUG = False
Debug = lambda function: function if DEBUG == True else None # Sempre que adicionar alguma coisa so pra testar, coloca um ```Debug(print("So pra testar"))``` (o print pode ser qualquer coisa) 
Log   = lambda *text: print(*text) if DEBUG == True else None # Se for pra debugar com print, usa Log("So pra testar")
