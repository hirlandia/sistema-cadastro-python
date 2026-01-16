🗂️ Sistema de Cadastro: Conectando Python a um Banco de Dados Real (MySQL)

Neste projeto, desenvolvi um sistema de cadastro em Python que se comunica diretamente com um banco de dados MySQL. A proposta foi sair do conceito de dados “temporários” e trabalhar com informações persistentes, simulando um cenário real de sistemas corporativos.

O sistema funciona via terminal (CLI) e permite visualizar e inserir dados relacionados a produtos, clientes e pedidos, reforçando a lógica por trás de aplicações que utilizam bancos de dados relacionais.

💡 O Desafio  
O principal desafio foi entender como o Python se conecta a um banco de dados externo e como essa comunicação acontece de forma segura e organizada.  
Mais do que apenas executar comandos SQL, o objetivo foi estruturar o código de maneira clara, separando responsabilidades e garantindo que o usuário tivesse uma experiência simples ao interagir com o sistema.

🔍 O que eu aprendi e apliquei  

1. Conexão com Banco de Dados (A ponte entre Python e MySQL)  
Aprendi a utilizar a biblioteca `mysql-connector-python` para estabelecer a conexão com o banco de dados, entendendo conceitos importantes como:
- Host, usuário, senha e base de dados  
- Criação de cursor para executar comandos SQL  
- Confirmação de transações com `commit()`

2. Organização do Código em Funções  
Para manter o código mais limpo e reutilizável, separei as responsabilidades:
- Um arquivo principal (`main.py`) responsável pelo menu e interação com o usuário  
- Um arquivo de funções (`funcoes.py`) responsável pelas operações no banco  
Isso me ajudou a entender melhor modularização e boas práticas em Python.

3. Operações CRUD na Prática  
Através do sistema, pratiquei operações essenciais:
- Consulta de dados (`SELECT`)
- Inserção de dados (`INSERT`)
- Leitura dinâmica de tabelas
Tudo isso simulando um fluxo próximo ao que acontece em sistemas reais de cadastro.

4. Segurança Básica no Terminal  
Utilizei a biblioteca `getpass` para ocultar a senha do banco durante a digitação, entendendo a importância de não expor informações sensíveis, mesmo em projetos simples.

🛠️ Tecnologias e Bibliotecas  
- Python 3  
- MySQL  
- mysql-connector-python  
- getpass  

🚀 Como executar o projeto  

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/sistema-cadastro-python.git
