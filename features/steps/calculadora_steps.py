from behave import given, when, then
from src.calculadora import Calculadora

# ─── Given ───────────────────────────────────────────────────

@given('que iniciei a calculadora')
def step_iniciei_calculadora(context):
    context.calculadora = Calculadora()
    context.erro = None

# ─── When ────────────────────────────────────────────────────

@when('soma {a:g} e {b:g}')
def step_somar(context, a, b):
    context.resultado = context.calculadora.somar(a, b)

@when('subtrair {a:g} e {b:g}')
def step_subtrair(context, a, b):
    context.resultado = context.calculadora.subtrair(a, b)

@when('multiplicar {a:g} e {b:g}')
def step_multiplicar(context, a, b):
    context.resultado = context.calculadora.multiplicar(a, b)

@when('dividir {a:g} e {b:g}')
def step_dividir(context, a, b):
    try:
        context.resultado = context.calculadora.dividir(a, b)
        context.erro = None
    except ValueError as e:
        context.resultado = None
        context.erro = str(e)

# ─── Then ────────────────────────────────────────────────────

@then('o resultado deve ser {esperado:g}')
def step_verificar_resultado(context, esperado):
    assert context.resultado == esperado, (
        f"Esperado: {esperado}, Obtido: {context.resultado}"
    )

@then('deve ocorrer um erro de divisão por zero')
def step_verificar_erro_divisao(context):
    assert context.erro is not None, "Era esperado um erro de divisão por zero, mas nenhum erro ocorreu."
    assert 'zero' in context.erro.lower(), (
        f"Mensagem de erro inesperada: {context.erro}"
    )

@when('tentar somar {a:g} e {b:g}')
def step_tentar_somar_decimal(context, a, b):
    """Delega a validação à própria classe Calculadora e captura o erro se for lançado."""
    try:
        context.resultado = context.calculadora.somar(a, b)
        context.erro = None
    except ValueError as e:
        context.resultado = None
        context.erro = str(e)

@then('deve ocorrer um erro de soma com decimal')
def step_verificar_erro_soma_decimal(context):
    assert context.erro is not None, "Era esperado um erro de soma com decimal, mas nenhum erro ocorreu."
    assert 'inteiros' in context.erro.lower(), (
        f"Mensagem de erro inesperada: {context.erro}"
    )