import sys
import os

# Garante que o diretório raiz do projeto esteja no path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask import Flask, request, jsonify, render_template
from src.calculadora import Calculadora

app = Flask(
    __name__,
    template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'),
    static_folder=os.path.join(os.path.dirname(__file__), '..', 'static')
)

calculadora = Calculadora()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/calcular', methods=['POST'])
def calcular():
    dados = request.get_json()

    numero1 = dados.get('numero1')
    numero2 = dados.get('numero2')
    operacao = dados.get('operacao')

    if numero1 is None or numero2 is None or operacao is None:
        return jsonify({'erro': 'Parâmetros inválidos'}), 400

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
    except (ValueError, TypeError):
        return jsonify({'erro': 'Os valores devem ser números'}), 400

    operacoes = {
        'soma': calculadora.somar,
        'subtracao': calculadora.subtrair,
        'multiplicacao': calculadora.multiplicar,
        'divisao': calculadora.dividir,
    }

    if operacao not in operacoes:
        return jsonify({'erro': 'Operação inválida'}), 400

    try:
        resultado = operacoes[operacao](numero1, numero2)
        # Retorna int se o resultado for inteiro, float caso contrário
        if resultado == int(resultado):
            resultado = int(resultado)
        return jsonify({'resultado': resultado})
    except ValueError as e:
        return jsonify({'erro': 'Não é possível dividir por zero'}), 400


if __name__ == '__main__':
    app.run(debug=True, port=5000)
