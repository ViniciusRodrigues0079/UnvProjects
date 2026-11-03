#Dados SQL

##AS ANOTAÇÕES NESSE ARQUIVO REFERENCIAM O ARQUIVO Aula.sql QUE ESTÁ NA MESMA PASTA

*Observações: 
- Após o uso de comandos, é necessário utilizar -> ; <-, para indicar o fim do comando
-

##Tipos de dados

INT: Define o tipo de dado inteiro em uma coluna, podendo ser exclusivamente um número inteiro entre 
2³¹-1 (2147483647) e -2³¹ (2147483648), que são os valores mais extremos que um atributo INT consegue suportar (referências 4, 8, 17 e 21)

VARCHAR (1...255): Define o tipo de dado VARCHAR em uma coluna, podendo ser um texto que vai de 0 caracteres (1 se restringido pelo NOT NULL) até o máximo definido no comando, nesse caso, 255. Caso o total de caracteres exceda o limite pré-definido, o campo será convertido em TEXT (referências 5, 6, 16 e 22)

CHAR (1...255): Define o tipo de dado char em uma coluna, podendo ser um texto que vai exclusivamente de 0 caracteres (1 se restringido pelo NOT NULL) até o máximo definido no comando, nesse caso, 255 (referência 27)

DECIMAL (10, 2): Define o tipo de dado decimal em uma coluna, com o formato 1234.56, sendo o número 10 o máximo de dígitos do número e 2 o máximo de dígitos após a vírgula (casas decimais) (referência 24)

DATE: Define o tipo de dado data em uma coluna, com o formato 2026.11.03 (referências 18 e 25)

DATETIME: Define o tipo de dado data e hora em uma coluna, com o formato 2026.11.03 10:29:00, utilizando formato 24h (sem referência)

BOOLEAN: Define o tipo de dado booleano em uma coluna, podendo ser exclusivamente TRUE ou FALSE (referência 26)

