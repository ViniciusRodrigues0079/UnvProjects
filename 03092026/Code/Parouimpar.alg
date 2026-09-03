algoritmo "Primeiro Programa"

var

numero : inteiro
resultado : real

inicio

numero <- 0
resultado <- 0
escreval("digite um numero inteiro: ")
leia (numero)
resultado <- numero mod 2
se resultado = 1 entao
escreval("Ímpar")
senao
escreval("Par")
fimse
fimalgoritmo