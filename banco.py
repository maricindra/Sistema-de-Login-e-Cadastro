import mysql.connector                               # Usando o conector do Mysql com Python. Digitar no Terminal: pip install mysql-connector-python

class SGBD:                                          # Criando a Classe SGBD, atribuindo atributos e funcionalidades.
    def __init__(self):
        self.conector = mysql.connector.connect(     # Instanciando ou tornando a função " mysql.connector.connect() " na variavel Conector, sendo que essa variavel esta associada a classe SGBD, de forma que acesse suas prorias proriedades, mais tarde.
            host="localhost",                        # Indica que a conexão ao Banco de Dados é Local, ou seja na propria maquina.
            user="root",                             # Root = Administrador, ou seja usuario administrador.
            password="1234",                         # Senha
            database="SISTEMA"    )                   # Base de Dados que esta acessando, Lembrando que: DATABASE/ BASE DE DADOS > TABELA > ColunaxLinha = dados; 
                                                     # Para teste: acesse o database: USE SISTEMA; CREATE TABLE USUARIOS ( EMAIL varchar(80), SENHA varchar(15) NOT NULL , CPF varchar(12 ou 13) Primary Key , NOME Varchar(100) );
                                                     # Para testar: INSERT INTO (CPF, EMAIL, SENHA, NOME) VALUES ( 'marininha44@gmail.com'  ,   'marininha44' , '17333635777'  , 	'Marina Happyninger');
        
    


        self.cursor = self.conector.cursor()              # Criando o cursor, esse cursor percorre o banco de dados, podendo ser chamado de consultor. 
                                                          # Necessario o uso do Self, pois é uma funcionalidade da propria classe, que será atribuida dinamicamente, mais tade.


        
        if self.conector.is_connected():                  # Teste que verifica se há conexão do MYSQL na classe SGBD, por meio da varivel conector, utilizando a função .is_connecter(),
            print("Conectado ao banco de Dados")
        else:                                              # Teste que verifica se há conexão do MYSQL
            print("Falha ao conectar ao banco de Dados")






    def esta_conectado(self):                                         # Metodo da classe SGBD que realiza o teste de conexão por meio do comando: .is_connected()
        return self.conector and self.conector.is_connected()

    
    def fechar_conexao(self):                                        # Metodo usado após usar o cursor. Desse modo não comprometer o uso excessivo do banco, fechando a conexão, após o uso.
        if self.esta_conectado():                                    # Teste que identifica conexão Ligada ao banco
            self.cursor.close()                                      # Função que fecha o Cursor/ Consultor  de  query/ pesquista.
            self.conector.close()                                    # Função que fecha a conexão com o banco.
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

    def verificar_cpf_existe(self, cpf):
        if self.esta_conectado():
            query = "SELECT COUNT(*) FROM usuarios WHERE email = %s;"
            self.cursor.execute(query, (cpf,))
            resultado = self.cursor.fetchone()
            return resultado[0] > 0

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

    def Inserir_usuario(self, cpf, email, senha, nome):
        if self.esta_conectado():
            sql = "INSERT INTO usuarios (cpf, email, senha, nome) VALUES (%s, %s, %s , %s)"
            self.cursor.execute(sql, (cpf, email, senha, nome))
            self.conector.commit()
            print("Usuário cadastrado com sucesso!")
            return True
        else:
            print("Erro: Não há conexão válida com o banco de dados.")
            return False





   




