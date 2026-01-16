import mysql.connector
# o getpass é um módelo para mascarar a senha
import getpass
# inserir no sistema as credenciais do banco de dados
user_host = input('informe o host')
user_user = input('informe o usuário')
user_password = getpass.getpass('informe a senha')
user_db = input('Informe o banco de dados')
conexao = mysql.connector.connect(
    host = user_host,
    user = user_user,
    password = user_password,
    database= user_db
)
# para executar a conexão com o banco de dados
cursor = conexao.cursor()

def mostrar_tabela(nome_tabela):
    print("Tabela:", nome_tabela)
    cursor.execute(f"select * from {nome_tabela}")
    # para coletar os resultados
    resultados = cursor.fetchall()
    
    # obter as colunas
    colunas = [desc[0] for desc in cursor.description]
    
    #exibir os nomes das colunas
    print(" | ".join(colunas))
    # id | nome | blabla
    # -------------------
    print('-' * 50)
    
    #exbir os dados (linhas)
    for linhas in resultados:
        print(" | ".join(str(item) for item in linhas))
        
        
        
    # o comando descption coleta os cabeçalhos de uma tabela
    # o comando fatchall coleta todas as linhas de uma tabela

def inserir_products():
    product_id = int(input("Informe o ID do produto: ")) #placeholder 1
    nome = input("Informe o nome do produto: ") #placeholder 2
    price = float(input("Informe o preço do produto: ")) #placeholder 3


    # Criar o script de SQL
    sql = "Insert into products(product_id, nome, price) values (%s, %s, %s)"
    # o % representa um placeholder, um espaço reservado para os valores que serão inseridos posteriormente
    
    #executar o script
    cursor.execute(sql, (product_id, nome, price))
    
    #confirmar tudo que fizemos
    #conexao.commit()
    #print('Seus dados foram inseridos!')
def inserir_customers():
    py_customer_id = int(input("Informe o Id do cliente: ")) #placeholder 1
    py_nome = input("Informe o nome do cliente: ") #placeholder 2
    
    sql = "Insert into customers(customer_id,nome) values (%s, %s)"
    
    cursor.execute(sql, (py_customer_id, py_nome))
    
    conexao.commit()
    print("Seus dados foram inseridos!")
    
def inserir_orders():
    py_order_id = int(input("Informe o Id do pedido: ")) #placeholder 1
    py_order_date = input("Data do pedido (YYYY-MM-DD): ") #placeholder 2
    py_customer_id = int(input("Informe o ID do cliente: ")) #placeholder 3
    py_product_id = int(input("Informe o ID do produto: ")) #placeholder 4
    py_quantity = int(input("Informe a quantidade: ")) #placeholder 5
    py_total_decimal = float(input("Informe o total: ")) #placeholder 6
    
    sql = "Insert into orders(order_id, order_date, customer_id, product_id, quantity, total_decimal) values (%s, %s, %s, %s, %s, %s)"
    
    cursor.execute(sql, (py_order_id, py_order_date, py_customer_id, py_product_id, py_quantity, py_total_decimal))

    
def fechar_conexao():
    cursor.close()
    conexao.close()
    print("Seus dados foram inseridos!")
    conexao.commit()
