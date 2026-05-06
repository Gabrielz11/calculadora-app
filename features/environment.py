"""
environment.py — Behave lifecycle hooks

Inicializa o WebDriver apenas para cenários de interface (calculadora_ui.feature).
Para os testes de unidade (calculadora.feature), nenhum navegador é necessário.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def _is_ui_scenario(scenario):
    """Retorna True se o cenário pertence à feature de interface (UI)."""
    return 'calculadora_ui' in scenario.feature.filename


def before_scenario(context, scenario):
    """Abre o Chrome apenas para cenários de UI."""
    if not _is_ui_scenario(scenario):
        return

    options = webdriver.ChromeOptions()
    #options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1280,720")

    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service, options=options)
    context.driver.implicitly_wait(5)
    # WebDriverWait disponível nos steps via context.wait
    context.wait = WebDriverWait(context.driver, 10)


def after_scenario(context, scenario):
    """Fecha o Chrome após cenários de UI."""
    if hasattr(context, 'driver'):
        context.driver.quit()
        del context.driver
