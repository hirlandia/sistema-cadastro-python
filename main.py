from funcoes import mostrar_tabela, inserir_products, inserir_customers, inserir_orders, fechar_conexao

import mysql.connector
# integração de mysql com scripts em python
# para usar mysql com python - mysql.connector

# agora as opçoes do nosso sistema
# mostrar tabela products
# mostrar tabela customers
# mostrar tabela orders
# cadastrar products
# cadastrar customers
# cadastrar orders

while True:
    print('1 - ver Products')
    print('2 - ver Customers')
    print('3 - ver Orders')
    print('4 - Cadastrar Products')
    print('5 - Cadastar Customers')
    print('6 - Cadastrar Orders')

    opcao = input('informe a opção desejada')

    if opcao == '1':
        mostrar_tabela('products')
    elif opcao == '2':
        mostrar_tabela('customers')
    elif opcao == '3':
        mostrar_tabela('orders')
    elif opcao == '4':
        inserir_products()
    elif opcao == '5':
        inserir_customers()
    elif opcao == '6':
        inserir_orders()
    else:
        print('tchau')
        fechar_conexao()
        break