# import pandas as pd
# from flask import Flask
# 
# app = Flask(__name__)
# 
# #Construir as Funcionalidades
# 
# @app.route('/')
# def homepage():
#   return 'Aqui vai ficar a tela inicial do site'
# 
# @app.route('/cadastro')
# def cadastro():
#   return 'Essa vai ser a segunda pagina para cadastro'
# 
# 
# # Para rodar nossa api
# app.run(host= '0.0.0.0')
# 
# 
# 
# # Ler o banco de dados
# banco = pd.read_db('nome do arquivo de banco de dados')