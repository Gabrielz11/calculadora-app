import time
from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

BASE_URL = "http://localhost:5000"

# ─── Hooks de ciclo de vida ───────────────────────────────────

def before_scenario(context, scenario):
    """Inicializa o WebDriver antes de cada cenário."""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')          # Rode sem abrir janela
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,720')

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(5)
    context.wait = WebDriverWait(context.driver, 10)


def after_scenario(context, scenario):
    """Fecha o WebDriver após cada cenário."""
    if hasattr(context, 'driver'):
        context.driver.quit()


# ─── Given ───────────────────────────────────────────────────

@given('que estou na página da calculadora')
def step_acessar_pagina(context):
    context.driver.get(BASE_URL)
    context.wait.until(
        EC.presence_of_element_located((By.ID, 'btn-calcular'))
    )


# ─── When ────────────────────────────────────────────────────

@when('eu digito {valor} no primeiro campo')
def step_digitar_numero1(context, valor):
    campo = context.driver.find_element(By.ID, 'numero1')
    campo.clear()
    campo.send_keys(valor)


@when('eu digito {valor} no segundo campo')
def step_digitar_numero2(context, valor):
    campo = context.driver.find_element(By.ID, 'numero2')
    campo.clear()
    campo.send_keys(valor)


@when('eu seleciono a operação {operacao}')
def step_selecionar_operacao(context, operacao):
    select_el = Select(context.driver.find_element(By.ID, 'operacao'))
    select_el.select_by_value(operacao)


@when('eu clico no botão calcular')
def step_clicar_calcular(context):
    btn = context.driver.find_element(By.ID, 'btn-calcular')
    btn.click()


# ─── Then ────────────────────────────────────────────────────

@then('o resultado exibido deve ser {esperado}')
def step_verificar_resultado_ui(context, esperado):
    context.wait.until(
        EC.visibility_of_element_located((By.ID, 'resultado'))
    )
    resultado_el = context.driver.find_element(By.ID, 'resultado')
    texto_obtido = resultado_el.text.strip()
    assert texto_obtido == str(esperado), (
        f"Esperado: '{esperado}', Obtido: '{texto_obtido}'"
    )


@then('deve ser exibida a mensagem "{mensagem}"')
def step_verificar_mensagem_erro_ui(context, mensagem):
    context.wait.until(
        EC.visibility_of_element_located((By.ID, 'resultado'))
    )
    resultado_el = context.driver.find_element(By.ID, 'resultado')
    texto_obtido = resultado_el.text.strip()
    assert mensagem in texto_obtido, (
        f"Mensagem esperada: '{mensagem}', Obtida: '{texto_obtido}'"
    )
