Feature: Calculadora Web — Interface do Usuário
    Para realizar cálculos pelo navegador
    Como um usuário da aplicação web
    Eu quero interagir com a interface da calculadora e ver os resultados na tela

    Scenario: Somar dois números pela interface
        Given que estou na página da calculadora
        When eu digito 5 no primeiro campo
        And eu digito 3 no segundo campo
        And eu seleciono a operação soma
        And eu clico no botão calcular
        Then o resultado exibido deve ser 8

    Scenario: Subtrair dois números pela interface
        Given que estou na página da calculadora
        When eu digito 10 no primeiro campo
        And eu digito 4 no segundo campo
        And eu seleciono a operação subtracao
        And eu clico no botão calcular
        Then o resultado exibido deve ser 6

    Scenario: Multiplicar dois números pela interface
        Given que estou na página da calculadora
        When eu digito 5 no primeiro campo
        And eu digito 2 no segundo campo
        And eu seleciono a operação multiplicacao
        And eu clico no botão calcular
        Then o resultado exibido deve ser 10

    Scenario: Dividir dois números pela interface
        Given que estou na página da calculadora
        When eu digito 20 no primeiro campo
        And eu digito 5 no segundo campo
        And eu seleciono a operação divisao
        And eu clico no botão calcular
        Then o resultado exibido deve ser 4

    Scenario: Divisão por zero pela interface
        Given que estou na página da calculadora
        When eu digito 10 no primeiro campo
        And eu digito 0 no segundo campo
        And eu seleciono a operação divisao
        And eu clico no botão calcular
        Then deve ser exibida a mensagem "Não é possível dividir por zero"
