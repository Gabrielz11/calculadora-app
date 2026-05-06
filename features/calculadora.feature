Feature: Operações Básicas da Calculadora
    Para realizar cálculos simples
    Como um usuário
    Eu quero usar a calculadora para somar, subtrair, multiplicar e dividir

    Scenario: Somar dois números
        Given que iniciei a calculadora
        When soma 5 e 3
        Then o resultado deve ser 8

    Scenario: Subtrair dois números
        Given que iniciei a calculadora
        When subtrair 10 e 4
        Then o resultado deve ser 6

    Scenario: Multiplicar dois números
        Given que iniciei a calculadora
        When multiplicar 5 e 2
        Then o resultado deve ser 10

    Scenario: Dividir dois números
        Given que iniciei a calculadora
        When dividir 20 e 5
        Then o resultado deve ser 4

    Scenario: Divisão por zero
        Given que iniciei a calculadora
        When dividir 10 e 0
        Then deve ocorrer um erro de divisão por zero