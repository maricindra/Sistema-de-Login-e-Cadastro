import customtkinter as ctk
import tkinter as tk
from banco import SGBD


janela = ctk.CTk()
banco_dados = SGBD()

def Logar():
    email = email_login.get()
    senha = senha_login.get()

    if banco_dados.esta_conectado():
        if banco_dados.verificar_email_existe(email):
            if banco_dados.verificar_senha(email, senha):
                print("Login bem-sucedido!")
                janela2 = ctk.CTk()
                janela2.geometry("500x280")
                texto_janela2 = ctk.CTkLabel(janela2, text="Bem vindo a Plataforma")
                texto_janela2.pack(padx=10, pady=10)
                janela2.mainloop()
            else:
                print("Senha incorreta.")
                texto_informativo = ctk.CTkLabel(janela, text="", text_color="red")
                texto_informativo.pack(padx=10, pady=10)

        else:
            print("Email incorreto.")
            texto_informativo = ctk.CTkLabel(janela, text="", text_color="red")
            texto_informativo.pack(padx=10, pady=10)


    else:
        print("Erro: Não há conexão com o banco de dados. Não é possível logar.")


def Janela_Cadastro():
    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.geometry("300x600")

    janela_cadastro.title("Cadastro de Usuário")



    texto_cadastro = ctk.CTkLabel(janela_cadastro, text= "Realizar Cadastro")
    texto_cadastro.pack(padx=10, pady=10)

    janela_cadastro.mainloop()

janela.geometry("500x280")

texto_titulo = ctk.CTkLabel(janela, text="Fazer Login")
texto_titulo.pack(padx=10, pady=10)

email_login = ctk.CTkEntry(janela, placeholder_text="Seu E-mail")
email_login.pack(padx=10, pady=5)

senha_login = ctk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha_login.pack(padx=10, pady=5)

        # Botões
botao_login = ctk.CTkButton(janela, text="Logar", command=Logar)  # Chama logar
botao_login.pack(padx=10, pady=5)

botao_cadastro = ctk.CTkButton(janela, text="Cadastrar", command = Janela_Cadastro)
botao_cadastro.pack(padx=10, pady=5)

janela.mainloop()

if __name__ == "__main__":
    pass




