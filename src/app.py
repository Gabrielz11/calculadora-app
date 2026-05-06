import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
from src.calculadora import Calculadora

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

calculadora = Calculadora()

# ─── MANIPULADORES GLOBAIS DE ERRO (A forma profissional) ──────

@app.errorhandler(ValueError)
def handle_bad_request(e):
    """Captura qualquer ValueError e transforma em 400 automaticamente."""
    return jsonify({'erro': str(e)}), 400

@app.errorhandler(Exception)
def handle_internal_error(e):
    """Captura erros inesperados e transforma em 500."""
    return jsonify({'erro': 'Erro interno no servidor'}), 500


# ─── ROTAS ───────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    """
    Rota ULTRA MAGRA. 
    Ela apenas recebe, chama o serviço e entrega. 
    O tratamento de erro é feito globalmente pelos handlers acima.
    """
    resultado = calculadora.executar(request.get_json())
    return jsonify({'resultado': resultado})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
