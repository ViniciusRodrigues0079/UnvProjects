#Comandos SQL

##AS ANOTAÇÕES NESSE ARQUIVO REFERENCIAM O ARQUIVO Aula.sql QUE ESTÁ NA MESMA PASTA

*Observações: 
- Após o uso de comandos, é necessário utilizar -> ; <-, para indicar o fim do comando
- Para fazer comentários em SQl, é necessário utilizar > -- < para comentários de uma linha e
 -> /*  */ <- para comentários de múltipla linha
-

##Comandos da parte DDL (Data Definition Language)

Principais comandos: 

CREATE: Cria um banco de dados (DATABASE) ou uma tabela (TABLE), definindo nome, atributos (colunas) e restrições (referências 1, 3, 9 e 16)

ALTER: Altera uma tabela, selecionando-a e utilizando outros comandos para editar ela e suas colunas (referência 7)

    ###Subcomandos ALTER

    ADD: Adiciona coluna (referência 8)

    MODIFY: Altera coluna (referência)

    RENAME COLUMN: Renomeia coluna (referência 10)

    DROP COLUMN: Exclui coluna (referência 14)
    
    ADD PRIMARY KEY: Adiciona um campo de chave primária

    ADD CONSTRAINT...FOREIGN KEY: Adiciona um campo de chave estrangeira

    RENAME TO: Renomeia a tabela

    DROP: Exclui uma tabela, incluindo seus registros e suas colunas (referência 19)

    TRUNCATE: Limpa todos os registros de uma tabela, mantendo as colunas

