# Projeto-calculadora

## Curso EBAC - Calculadora em Python

Este projeto foi desenvolvido como atividade prática do curso de TI da EBAC.

## Como executar o projeto

>Abra o Ubuntu ou outro terminal compatível com Bash.

Acesse a pasta onde estão os arquivos do projeto:
 
`cd projeto-calculadora-py`

>Dê permissão de execução para o arquivo .sh:

`chmod +x calculadora.sh`

>Execute o arquivo:

```./calculadora.sh```

>O arquivo calculadora.sh inicia o programa main.py.

## Explicação do código Python

O arquivo main.py contém uma calculadora desenvolvida em Python.

Primeiramente, o programa solicita ao usuário dois números.

Depois, apresenta quatro opções de operações matemáticas:

Soma
Subtração
Multiplicação
Divisão

O usuário escolhe a operação desejada e o programa realiza o cálculo.

O código utiliza estruturas condicionais if, elif e else para identificar qual operação foi escolhida.

Também existe uma verificação para impedir a divisão por zero. Caso o segundo número seja zero na operação de divisão, o programa apresenta uma mensagem de erro.

O código também possui tratamento de erro utilizando try e except, evitando que o programa seja encerrado caso o usuário digite um valor que não seja um número.

A função calcular() concentra a lógica principal da calculadora.

Por fim, o trecho:

if __name__ == "__main__":
    calcular()

faz com que a função calcular() seja executada quando o arquivo main.py for executado diretamente.

Arquivos do projeto
main.py - código da calculadora em Python.
calculadora.sh - arquivo executável responsável por iniciar o programa Python.
README.md - documentação do projeto.
