Feature: Calculadora Web

  Background:
    Given que estou na página da calculadora

  # ==================== SOMA ====================

  Scenario: Somar dois números positivos
    When eu digito 5 no primeiro campo
    And eu digito 3 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then o resultado exibido deve ser 8

  Scenario: Somar com zero
    When eu digito 7 no primeiro campo
    And eu digito 0 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then o resultado exibido deve ser 7

  Scenario: Somar dois números negativos
    When eu digito -4 no primeiro campo
    And eu digito -6 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then o resultado exibido deve ser -10

  Scenario: Somar positivo com negativo
    When eu digito 10 no primeiro campo
    And eu digito -3 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then o resultado exibido deve ser 7

  Scenario: Somar números decimais não é permitido
    When eu digito 1.5 no primeiro campo
    And eu digito 2.5 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then deve ser exibida a mensagem "A operação de soma aceita apenas números inteiros"

  # ==================== SUBTRAÇÃO ====================

  Scenario: Subtrair dois números
    When eu digito 10 no primeiro campo
    And eu digito 4 no segundo campo
    And eu seleciono a operação subtracao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 6

  Scenario: Subtração com resultado negativo
    When eu digito 3 no primeiro campo
    And eu digito 8 no segundo campo
    And eu seleciono a operação subtracao
    And eu clico no botão calcular
    Then o resultado exibido deve ser -5

  Scenario: Subtrair zero
    When eu digito 9 no primeiro campo
    And eu digito 0 no segundo campo
    And eu seleciono a operação subtracao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 9

  Scenario: Subtrair número negativo
    When eu digito 5 no primeiro campo
    And eu digito -3 no segundo campo
    And eu seleciono a operação subtracao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 8

  # ==================== MULTIPLICAÇÃO ====================

  Scenario: Multiplicar dois números
    When eu digito 5 no primeiro campo
    And eu digito 2 no segundo campo
    And eu seleciono a operação multiplicacao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 10

  Scenario: Multiplicar por zero
    When eu digito 9 no primeiro campo
    And eu digito 0 no segundo campo
    And eu seleciono a operação multiplicacao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 0

  Scenario: Multiplicar dois números negativos
    When eu digito -3 no primeiro campo
    And eu digito -4 no segundo campo
    And eu seleciono a operação multiplicacao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 12

  Scenario: Multiplicar positivo por negativo
    When eu digito 6 no primeiro campo
    And eu digito -2 no segundo campo
    And eu seleciono a operação multiplicacao
    And eu clico no botão calcular
    Then o resultado exibido deve ser -12

  # ==================== DIVISÃO ====================

  Scenario: Dividir dois números
    When eu digito 20 no primeiro campo
    And eu digito 5 no segundo campo
    And eu seleciono a operação divisao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 4

  Scenario: Divisão com resultado decimal
    When eu digito 10 no primeiro campo
    And eu digito 3 no segundo campo
    And eu seleciono a operação divisao
    And eu clico no botão calcular
    Then o resultado exibido deve conter 3.33

  Scenario: Dividir zero por número
    When eu digito 0 no primeiro campo
    And eu digito 5 no segundo campo
    And eu seleciono a operação divisao
    And eu clico no botão calcular
    Then o resultado exibido deve ser 0

  # ==================== ERROS ====================

  Scenario: Divisão por zero
    When eu digito 10 no primeiro campo
    And eu digito 0 no segundo campo
    And eu seleciono a operação divisao
    And eu clico no botão calcular
    Then deve ser exibida a mensagem "Não é possível dividir por zero"

  # ==================== EDGE CASES ====================

  Scenario: Somar números muito grandes
    When eu digito 999999 no primeiro campo
    And eu digito 999999 no segundo campo
    And eu seleciono a operação soma
    And eu clico no botão calcular
    Then o resultado exibido deve ser 1999998
