import customtkinter as ctk
import tkinter as tk
from banco import SGBD


#No Mysql:
# User: marininha44@gmail.com  | Senha: marininha44


janela = ctk.CTk()
ctk.set_appearance_mode("dark")

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

                #Dentro da Plataforma

            else:
                print("Senha incorreta.")
                texto_informativo = ctk.CTkLabel(janela, text="Senha incorreta", text_color="red")
                texto_informativo.pack(padx=10, pady=10)

        else:
            print("Email incorreto.")
            texto_informativo2 = ctk.CTkLabel(janela, text="Email incorreto", text_color="red")
            texto_informativo2.pack(padx=10, pady=10)


    else:
        print("Erro: Não há conexão com o banco de dados. Não é possível logar.")


def Janela_Cadastro():
    janela_cadastro = tk.Toplevel(janela)
    janela_cadastro.geometry("300x600")
    ctk.set_appearance_mode("dark")
    janela_cadastro.title("Cadastro de Usuário")


    texto_cadastro = ctk.CTkLabel(janela_cadastro, text="Realizar Cadastro", bg_color=" ")
    texto_cadastro.pack(padx=10, pady=10)

    texto_dados = ctk.CTkLabel(janela_cadastro, text="Seus dados:")
    texto_dados.pack(padx=10, pady=10)

    nome_cadastro_entry = ctk.CTkEntry(janela_cadastro, placeholder_text="Seu Nome: ")
    nome_cadastro_entry.pack(padx=10, pady=10)

    email_cadastro_entry = ctk.CTkEntry(janela_cadastro, placeholder_text="Seu E-mail")
    email_cadastro_entry.pack(padx=10, pady=10)

    cpf_cadastro_entry = ctk.CTkEntry(janela_cadastro, placeholder_text="Seu CPF")
    cpf_cadastro_entry.pack(padx=10, pady=10)

    senha_cadastro_entry = ctk.CTkEntry(janela_cadastro, placeholder_text="Sua senha", show="*")
    senha_cadastro_entry.pack(padx=10, pady=10)

    senha2_cadastro_entry = ctk.CTkEntry(janela_cadastro, placeholder_text="Confirme sua senha", show="*")
    senha2_cadastro_entry.pack(padx=10, pady=10)

    mensagem_cadastro = ctk.CTkLabel(janela_cadastro, text="", text_color="red")
    mensagem_cadastro.pack(padx=10, pady=10)

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


