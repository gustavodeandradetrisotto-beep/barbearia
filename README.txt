=================================================================
 SISTEMA DE AGENDAMENTOS - BARBEARIA NAVALHA DE OURO
 Situação de Aprendizagem - Programação de Aplicativos
 Curso Técnico em Desenvolvimento de Sistemas - SENAI/SC
=================================================================

INTEGRANTES DO GRUPO:
- [NOME DO ALUNO 1]
- [NOME DO ALUNO 2]
- [NOME DO ALUNO 3]

(Substituir pelos nomes reais dos integrantes do trio antes da entrega.)

-----------------------------------------------------------------
DESCRIÇÃO
-----------------------------------------------------------------
Sistema web desenvolvido em Python, utilizando o framework Flask,
banco de dados MySQL e templates Jinja2, para controlar os
agendamentos da Barbearia Navalha de Ouro (cadastro de serviços,
registro de agendamentos e visualização em página web).

-----------------------------------------------------------------
ESTRUTURA DO PROJETO
-----------------------------------------------------------------
barbearia/
├── config.py            -> credenciais de acesso ao banco
├── banco.py             -> função de conexão com o MySQL
├── models.py            -> classe Agendamento (POO)
├── agendamentos.py      -> funções de acesso à tabela agendamentos
├── app.py               -> aplicação Flask (rotas)
├── banco.sql            -> script de criação do banco e dados iniciais
├── README.txt           -> este arquivo
└── templates/
    ├── index.html
    ├── agendamentos.html
    └── detalhe.html

-----------------------------------------------------------------
PRÉ-REQUISITOS
-----------------------------------------------------------------
- Python 3.10 ou superior instalado
- MySQL Server e MySQL Workbench instalados
- Pip (gerenciador de pacotes do Python)

-----------------------------------------------------------------
COMO RODAR O PROGRAMA
-----------------------------------------------------------------
1) Instalar as bibliotecas necessárias:
   pip install flask mysql-connector-python

2) Criar o banco de dados:
   - Abrir o MySQL Workbench.
   - Executar o script "banco.sql" (ele cria o banco "barbearia",
     a tabela "agendamentos" e insere 8 agendamentos de exemplo).

3) Configurar o acesso ao banco:
   - Abrir o arquivo "config.py".
   - Ajustar "user" e "password" com as credenciais do seu MySQL.

4) Executar a aplicação:
   - Pelo terminal, dentro da pasta "barbearia", rodar:
     python app.py

5) Acessar no navegador:
   http://127.0.0.1:5000/

-----------------------------------------------------------------
ROTAS DISPONÍVEIS
-----------------------------------------------------------------
/                                -> página inicial
/agendamentos                    -> lista todos os agendamentos
/agendamentos/status/<status>    -> filtra por status
                                     (Agendado, Concluído ou Cancelado)
/agendamento/<id>                -> detalhe de um agendamento
