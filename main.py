import mysql.connector as cnx








# Função para criar o banco de dados
def criarDatabase(cursor):
    query = 'CREATE DATABASE IF NOT EXISTS comercial;'
    cursor.execute(query)
    cursor.execute('USE comercial;')

# Função para criar uma tabela
def criarTabela(cursor):
    nome_tabela = input("Digite o nome da nova tabela: ")
    
    query = f'''
        CREATE TABLE IF NOT EXISTS {nome_tabela} (
            id_produto INT PRIMARY KEY AUTO_INCREMENT,
            nome_produto VARCHAR(50),
            preco_produto DECIMAL(10, 2)
        );
    '''
    cursor.execute(query)

# Conectando ao MySQL
conexao = cnx.connect(
    host="localhost",
    port=3308,
    user="root",
    password=""  # Adicione a senha, se necessário
)

cursor = conexao.cursor()

# Criando o banco e a tabela
criarDatabase(cursor)
criarTabela(cursor)

# Encerrando a conexão
conexao.commit()
cursor.close()
conexao.close()
