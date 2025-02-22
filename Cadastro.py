import customtkinter as ctk
import tkinter as tk
from Login import Entrada_de_dados



class JanelaCadastro(ctk.CTkToplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Cadastro")
        self.geometry("500x390")
        self.attributes('-topmost', True) 

        #Entradas
        texto = ctk.CTkLabel(self , text = "Cadastro")
        texto.pack(padx=10,pady=10)
        
        nome = ctk.CTkEntry(self ,placeholder_text="Seu Nome: ", show="")
        nome.pack(padx=1, pady=10) 
        
        email = ctk.CTkEntry(self ,placeholder_text="Seu E-mail", show="")
        email.pack(padx=1, pady=10)
        
        cpf = ctk.CTkEntry(self ,placeholder_text="Seu CPF", show="")
        cpf.pack(padx=1, pady=10)
        
        senha = ctk.CTkEntry(self,placeholder_text="Sua senha", show="*")
        senha.pack(padx=1, pady=10)
        
        senha2 = ctk.CTkEntry(self,placeholder_text="Confirme sua senha", show="")
        senha2.pack(padx=1, pady=10)
                    

        #Botões:
        
        botaocad = ctk.CTkButton(self ,text="Cadastrar")
        botaocad.pack(padx=1, pady=10)


    def Validar_Novos_dados(senha, senha2, cpf_verificado):

        if senha != senha2:
            print("Senhas Não correspondem")
            return False
        
        if cpf_verificado > 1:
            print("Cpf Já cadastrado")
            return False
        
        else:
            print("Bem vindo ao Sistema! Sucesso no Cadastro! ")

        
JanelaCadastro.mainloop()




