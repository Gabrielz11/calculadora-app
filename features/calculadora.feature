Feature: Operações Básicas da calculadora
    Para realizar cálculos simples
    Como um usuário
    Eu quero usar a calculadora para somar, subtrair, multiplicar e dividir

    Scenario: Somar dois números
        Given que iniciei a calculadora
        When soma 5 e 3
        Then o resultado deve ser 8