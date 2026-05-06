from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

BASE_URL = "http://localhost:5000"


# ─── Given ───────────────────────────────────────────────────

@given("que estou na página da calculadora")
def step_acessar_pagina(context):
    context.driver.get(BASE_URL)
    # Aguarda o botão estar presente antes de prosseguir
    context.wait.until(
        EC.presence_of_element_located((By.ID, "btn-calcular"))
    )


# ─── When ────────────────────────────────────────────────────

@when("eu digito {valor} no primeiro campo")
def step_digitar_numero1(context, valor):
    campo = context.driver.find_element(By.ID, "numero1")
    campo.clear()
    campo.send_keys(str(valor))


@when("eu digito {valor} no segundo campo")
def step_digitar_numero2(context, valor):
    campo = context.driver.find_element(By.ID, "numero2")
    campo.clear()
    campo.send_keys(str(valor))


@when("eu seleciono a operação {operacao}")
def step_selecionar_operacao(context, operacao):
    select = Select(context.driver.find_element(By.ID, "operacao"))
    select.select_by_value(operacao)


@when("eu clico no botão calcular")
def step_clicar_calcular(context):
    context.driver.find_element(By.ID, "btn-calcular").click()


# ─── Then ────────────────────────────────────────────────────

@then("o resultado exibido deve ser {esperado}")
def step_verificar_resultado(context, esperado):
    # Aguarda o elemento ter texto (resultado do fetch assíncrono)
    context.wait.until(
        EC.text_to_be_present_in_element((By.ID, "resultado"), str(esperado))
    )
    resultado = context.driver.find_element(By.ID, "resultado").text
    assert str(esperado) in resultado, f"Esperado '{esperado}', mas obtido '{resultado}'"


@then("o resultado exibido deve conter {parte}")
def step_verificar_resultado_parcial(context, parte):
    # Aguarda qualquer texto aparecer no elemento de resultado
    context.wait.until(
        lambda d: d.find_element(By.ID, "resultado").text.strip() != ""
    )
    resultado = context.driver.find_element(By.ID, "resultado").text
    assert str(parte) in resultado, f"Esperado conter '{parte}', mas obtido '{resultado}'"


@then('deve ser exibida a mensagem "{mensagem}"')
def step_verificar_mensagem_erro(context, mensagem):
    # Aguarda qualquer texto aparecer no elemento de resultado
    context.wait.until(
        lambda d: d.find_element(By.ID, "resultado").text.strip() != ""
    )
    resultado = context.driver.find_element(By.ID, "resultado").text
    assert mensagem in resultado, f"Esperado '{mensagem}', mas obtido '{resultado}'"
