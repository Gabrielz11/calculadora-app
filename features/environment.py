"""
environment.py — Behave lifecycle hooks

Os hooks before_scenario/after_scenario para os testes de UI (Selenium)
estão aqui centralizados para evitar duplicação entre os arquivos de steps.
"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def before_scenario(context, scenario):
    """Inicializa o WebDriver antes de cada cenário marcado com @ui."""
    # Apenas inicializa o driver para cenários de UI (feature calculadora_ui)
    if 'ui' in scenario.tags or 'calculadora_ui' in scenario.feature.filename:
        options = webdriver.ChromeOptions()
        # options.add_argument('--headless')  # Descomente para rodar sem janela
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-gpu')
        options.add_argument('--window-size=1280,720')

        service = Service(ChromeDriverManager().install())
        context.driver = webdriver.Chrome(service=service, options=options)
        context.driver.implicitly_wait(5)
        context.wait = WebDriverWait(context.driver, 10)


def after_scenario(context, scenario):
    """Fecha o WebDriver após cada cenário de UI."""
    if hasattr(context, 'driver'):
        context.driver.quit()
        del context.driver
