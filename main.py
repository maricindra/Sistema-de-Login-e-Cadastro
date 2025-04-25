import customtkinter as ctk  # importando e renomeando a biblioteca CustomTkinter = ctk.
import tkinter as tk         # importando e renomeando a biblioteca Tkinter = tk.
from banco import SGBD       # Importando a Classe SGBD do arquivo banco.


#No Mysql - teste de login
# User: marininha44@gmail.com  | Senha: marininha44




janela = ctk.CTk()                # Criando a variavel para armazenar a funcionalidade do Customtkinter, Abrir janela.
janela.title("Login")             # Funcionalidade que da titulo a Janela, nome da Janela
ctk.set_appearance_mode("dark")   # Funcionalidade do CTk para interface da Janela
janela.geometry("500x280")        # Proporção da Janela ( Largura x Altura )


banco_dados = SGBD()              # Renomeando a Classe SGBD para a variavel: banco_dados, nesse arquivo.




# Criando a função de Logar() , nessa função estará armazenado uma serie de ações após utilizar o botão do CTK, sendo armazendo no: Command = Logar(). Possibilitando o Login na plataforma.

def Logar():                                
    email = email_login.get()               # Obtendo a variavel global por meio da função get() 
    senha = senha_login.get()               # Obtendo a variavel global por meio da função get() 

    if banco_dados.esta_conectado():                           # Ainda, no metodo Logar(), a variavel acessa o metodo de conexão com banco de dados
        if banco_dados.verificar_email_existe(email):          # A variavel banco_dados acessa o metodo de verificar_email encapsulado na classe SGBD, que foi configurado no arquivo banco.
            if banco_dados.verificar_senha(email, senha):      # A variavel banco_dados acessa o metodo de verificar_senha encapsulado na classe SGBD, que foi configurado no arquivo banco.
                print("Login bem-sucedido!")                   # Incluido para teste no terminal, no entanto, não aparece na interface
                
                #Após o Login na plataforma
                janela2 = ctk.CTk()                            # Caso os testes ( Banco conectado, email verificado no mysql, senha verificada no mysql, forem >= 1. O acesso a plataforma será iniciado em uma nova Janela.
                janela2.geometry("500x280")                    # Proporção da Janela2
                texto_janela2 = ctk.CTkLabel(janela2, text="Bem vindo a Plataforma")       # Texto que informa a entrada na plataforma
                texto_janela2.pack(padx=10, pady=10)                                       # Posição do texto Acima, sem a posição o texto não aparece!
                janela2.mainloop()                                                         # Função que Finaliza codigos e conteúdos dessa janela, famoso ponto virgula , parentese ou chaves.

                

            else:                                                                         # No caso de o email estava certo, no entanto a senha incorreta, Faça:
                print("Senha incorreta.")                                                 # Incluido para teste no terminal, no entanto, não aparece na interface
                texto_informativo = ctk.CTkLabel(janela, text="Senha incorreta", text_color="red")         #Texto que aparece na interface, informando a senha incorreta, da cor vermelha; text color define a cor
                texto_informativo.pack(padx=10, pady=10)                                                   # Posição do texto Acima, sem a posição o texto não aparece!

        else:
            print("Email incorreto.")
            texto_informativo2 = ctk.CTkLabel(janela, text="Email incorreto", text_color="red")
            texto_informativo2.pack(padx=10, pady=10)


    else:
        print("Erro: Não há conexão com o banco de dados. Não é possível logar.")



# Criando a Função Janela_Cadastro, pois essa função será armazenada no botão criado pelo CTK. Nessa modalidade, uma serie de comandos realizará a abertura da janela Cadastro e suas ações junto com sua interface.

def Janela_Cadastro():

# Função Tentar_cadastro que será realizada ao clicar no botão do CTk, armazenado no 'Command'. É Necessario, primeiro criar a função para armazena-la no comando da interface.
    def Tentar_Cadastro():
        cpf = cpf_cadastro.get()
        senha1 = senha1_cadastro.get()
        senha2 = senha2_cadastro.get()
        email = email_cadastro.get()
        nome = nome_cadastro.get()

        if banco_dados.esta_conectado():
            # Se estiver conectado, prossiga verificando se há email no Sistema:
            if banco_dados.verificar_email_existe(email):
                print("Email Já cadastrado")
                informe_Cad = ctk.CTkLabel(janela_cadastro, text=" Email Cadastrado")
                informe_Cad.pack(padx=10, pady=10)


            # Se Existe o email no sistema, não verificará se o CPF esta no sistema.
            elif banco_dados.verificar_cpf_existe(cpf):
                print("CPF Já cadastrado")
                informe_Cad = ctk.CTkLabel(janela_cadastro, text=" CPF já Cadastrado")
                informe_Cad.pack(padx=10, pady=10)


            # Caso o email e o CPF sejam unicos, prossiga para a verificação da senha:
            else:

                if senha1 == senha2:
                    senha = senha1
                    Novo_usuario = banco_dados.Inserir_usuario(cpf,email,senha, nome)
                    informe_Cad = ctk.CTkLabel(janela_cadastro, text=" Bem vindo! Novo usuário Cadastrado")
                    informe_Cad.pack(padx=10, pady=10)

                    janela_cadastro.destroy() # Caso chegue nesse teste: Se as senhas forem iguais = inserir no Banco de dados e fechar Janela_Cadastro.


                
                else:
                    print("Senhas não coincidem")
                    informe_Cad = ctk.CTkLabel(janela_cadastro, text="Senhas não coincidem")
                    informe_Cad.pack(padx=10, pady=10)

        else:
            print(" Erro: Não há conexão válida com o banco de dados. ")
            informe_Cad = ctk.CTkLabel(janela_cadastro, text="Não há conexão válida com o banco de dados")
            informe_Cad.pack(padx=10, pady=10)

# Janela - Cadastro - Interface de Cadastro
 
    janela_cadastro = ctk.CTkToplevel(janela)
    janela_cadastro.geometry("300x600")
    janela_cadastro.title("Cadastro de Usuário")

    texto_cadastro = ctk.CTkLabel(janela_cadastro, text="Crie seu Cadastro:")
    texto_cadastro.pack(padx=10, pady=10)

    texto_dados = ctk.CTkLabel(janela_cadastro, text=" Seus dados:")                                                    # CTkLabel - Permite a visualização de textos na interface, sua estrutura é: ( Janela= "" , texto= "" , bg_colour = "")
    texto_dados.pack(padx=10, pady=10)

    nome_cadastro= ctk.CTkEntry(janela_cadastro, placeholder_text="Seu Nome: ")                                         # CTkEntry - Permite a entrada de dados.
    nome_cadastro.pack(padx=10, pady=10)                                                                                

    email_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Seu E-mail")
    email_cadastro.pack(padx=10, pady=10)

    cpf_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Seu CPF")
    cpf_cadastro.pack(padx=10, pady=10)

    senha1_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Sua senha", show="*")
    senha1_cadastro.pack(padx=10, pady=10)

    senha2_cadastro = ctk.CTkEntry(janela_cadastro, placeholder_text="Confirme sua senha", show="*")
    senha2_cadastro.pack(padx=10, pady=10)

# Botão do CTK que armazena o comando Tentar_Cadastro, ou seja um conjunto de verificações que possibilita a entrada desse novo dado no banco de dados.

    botao_cadastro = ctk.CTkButton(janela_cadastro, text="Realizar Cadastrar", command=Tentar_Cadastro, bg_color="DarkBlue")
    botao_cadastro.pack(padx=10, pady=5)

    mensagem_cadastro = ctk.CTkLabel(janela_cadastro, text="", text_color="red")
    mensagem_cadastro.pack(padx=10, pady=10)

    janela_cadastro.mainloop()                                                                                          # Função que Finaliza codigos e conteúdos dessa janela= Janela_cadastro. Famoso ponto virgula , parentese ou chaves.



# Janela - Interface do Login

texto_titulo = ctk.CTkLabel(janela, text="Fazer Login")
texto_titulo.pack(padx=10, pady=10)

email_login = ctk.CTkEntry(janela, placeholder_text="Seu E-mail")
email_login.pack(padx=10, pady=5)

senha_login = ctk.CTkEntry(janela, placeholder_text="Sua senha", show="*")
senha_login.pack(padx=10, pady=5)

botao_login = ctk.CTkButton(janela, text="Logar", command=Logar)  # Chama logar
botao_login.pack(padx=10, pady=5)

botao_cadastro = ctk.CTkButton(janela, text="Cadastrar", command = Janela_Cadastro)
botao_cadastro.pack(padx=10, pady=5)

janela.mainloop()    #  # Função que Finaliza codigos e conteúdos dessa janela: Janela principal, famoso ponto virgula , parentese ou chaves.



