from behave import given, when, then
from src.calculadora import Calculadora

@given('que iniciei a calculadora')
def step_iniciei_calculadora(context):
    print("Calculadora iniciada")
    context.calculadora = Calculadora()

@when('soma {a:d} e {b:d}')
def step_somar(context, a, b):
    print(f"Soma: {a} + {b}")
    context.resultado = context.calculadora.somar(a, b)

@then('o resultado deve ser {resultado:d}')
def step_verificiar_resultado(context, resultado):
    print(f"Resultado: {context.resultado}")
    assert context.resultado == resultado
    print(f"Esperado: {resultado}, Obtido: {context.resultado}")