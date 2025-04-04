import mysql.connector

class SGBD:
    def __init__(self):
        self.conector = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="SISTEMA"
        )
        self.cursor = self.conector.cursor()
        if self.conector.is_connected():
            print("Conectado ao banco de Dados")
        else:
            print("Falha ao conectar ao banco de Dados")

    def esta_conectado(self):
        return self.conector and self.conector.is_connected()

    def fechar_conexao(self):
        if self.esta_conectado():
            self.cursor.close()
            self.conector.close()
            print("Conexão com o banco de dados fechada.")
        else:
            print("Não há conexão para fechar.")

    def verificar_email_existe(self, email):
        if self.esta_conectado():
            query = "SELECT COUNT(*) FROM usuarios WHERE email = %s;"
            self.cursor.execute(query, (email,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0
        else:
            print("Erro: Não há conexão válida com o banco de dados.")
            return False

    def verificar_senha(self, email, senha):
        if self.esta_conectado():
            query = "SELECT senha FROM usuarios WHERE email = %s;"
            self.cursor.execute(query, (email,))
            resultado = self.cursor.fetchone()
            if resultado:
                return resultado[0] == senha
            return False
        else:
            print("Erro: Não há conexão válida com o banco de dados.")
            return False

    def inserir_usuario(self, cpf, email, senha):
        if self.esta_conectado():
            sql = "INSERT INTO usuarios (cpf, email, senha) VALUES (%s, %s, %s)"
            self.cursor.execute(sql, (cpf, email, senha))
            self.conector.commit()
            print("Usuário cadastrado com sucesso!")
            return True
        else:
            print("Erro: Não há conexão válida com o banco de dados.")
            return False

    def Logar(self, email, senha_digitada):
        if self.verificar_email_existe(email):
            if self.verificar_senha(email, senha_digitada):
                return True
            else:
                print("Senha incorreta")
                return False
        else:
            print("Email incorreto")
            return False

# Exemplo de uso (remova se estiver sendo usado como módulo)
if __name__ == "__main__":
    db = SGBD()
    if db.esta_conectado():
        print("Conexão ativa para testes.")
        # Faça testes aqui
        db.fechar_conexao()
    else:
        print("Falha na conexão para testes.")


   




