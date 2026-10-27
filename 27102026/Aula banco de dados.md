CREATE USER 'aluno'@'localhost' IDENTIFIED BY '123456' -> Cria um usuário com senha

GRANT/REVOKE SELECT ON escola. * TO 'aluno'@'localhost' -> Concede/remove permissão para VISUALIZAR os 
dados de todas as tabelas do SGBD 'escola.'

Permissões: SELECT, INSERT, UPDATE, DELETE, CREATE, ALTER, DROP

Tipos de usuário: Administrador, Desenvolvedor, Operador, Colsulta, Aplicação

*Cada usuário só deve receber as permissões necessárias para fazer seu trabalho

Aspectos importantes da segurança de bancos de dados:
    - Senhas fortes
    - Usuários com privilégios mínimos
    - Backup
    - Controle de acesso
    - Proteção contra SQL Injection

*É possível criar um usuário, definindo suas permissões através do MySQL Workbench