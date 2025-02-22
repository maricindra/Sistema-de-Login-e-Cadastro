import customtkinter as ctk
import tkinter as tk
from Cadastro import JanelaCadastro
import mysql.connector

#Configurações do banco de dados

def Interface(Logar):
     login = Logar.get()

     # Janela principal/ Definindo a Cor do Fundo do programa:
     # ctk.set_appearance_mode("Dark")
     # #Defindo cores de botões, widgets, rotulos e entrada de texto:
     # ctk.set_default_color_theme("dark-blue")
     janela = ctk.CTk()
     janela.geometry("500x280")

     # Widgets da janela principal 
     texto_titulo = ctk.CTkLabel(janela, text="Fazer Login")
     texto_titulo.pack(padx=10, pady=10)

     email = ctk.CTkEntry(janela, placeholder_text="Seu E-mail")
     email.pack(padx=10, pady=5)

     senha = ctk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
     senha.pack(padx=10, pady=5)

     # Botões
     botao_login = ctk.CTkButton(janela, text="Logar", command = login)
     botao_login.pack(padx=10, pady=5)

     botao_cadastro = ctk.CTkButton(janela, text="Cadastrar", command=abrir_janela_cadastro)
     botao_cadastro.pack(padx=10, pady=5)

     def abrir_janela_cadastro():
       janela_cadastro = Cadastro.JanelaCadastro(janela)
       janela_cadastro.mainloop()  # Inicia o loop da janela de cadastro

     janela.mainloop() #DECLARA O FINAL DO CODIGO da tela Login:

def Banco_de_dados():
  conector = mysql.connector.connect(
  host="localhost",
  user="root",
  password ="1234",
  database="SISTEMA")

  cursor = conector.cursor()

  #Comandos SQL: Cursor BD
  verificar_cpf = "SELECT COUNT(*) FROM usuarios WHERE cpf = %s;"
  verificar_email = "SELECT COUNT(*) FROM usuarios WHERE email = %s;"
  verificar_senha = "SELECT COUNT(*) FROM usuarios WHERE senha = %s;"
  
  def Validar_Novos_dados( cpf_verificado):
   novo_cpf = JanelaCadastro.cpf.get()
   cursor.execute = (verificar_cpf, (novo_cpf))
   cpf_verificado = cursor.fecthone([0])


   senha1 = JanelaCadastro.senha1.get()
   senha2 = JanelaCadastro.senha2.get()
  
   if senha1 != senha2:
     print("Senhas Não correspondem")
     return False
        
   if cpf_verificado > 1:
     print("Cpf Já cadastrado")
     return False
        
   else:
     print("Bem vindo ao Sistema! Sucesso no Cadastro! ")
  
       
  def Logar(email,senha):
       cursor.execute = (verificar_email, (email) ) 
       email_verificado = cursor.fetchone()[0]

       cursor.execute = (verificar_senha, (senha) )
       senha_verificada = cursor.fetchone()[0]

       if email_verificado == 0:  
         print("Email incorreto")
         return False 
       
       if senha_verificada > 0:
         print("login bem sucedido")
      
       else:
         print("Senha incorreta")
         return False  # Falha no login


   




