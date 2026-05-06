/**
 * script.js — Calculadora App
 * Responsável por capturar os dados do formulário,
 * enviar para a API Flask e exibir o resultado.
 */

async function calcular() {
  const numero1 = document.getElementById('numero1').value.trim();
  const numero2 = document.getElementById('numero2').value.trim();
  const operacao = document.getElementById('operacao').value;
  const btn = document.getElementById('btn-calcular');
  const container = document.getElementById('resultado-container');
  const resultadoEl = document.getElementById('resultado');
  const labelEl = document.getElementById('resultado-label');

  // Validação básica no front
  if (numero1 === '' || numero2 === '') {
    exibirErro('Por favor, preencha os dois campos.');
    return;
  }

  // Estado de carregamento
  btn.disabled = true;
  btn.querySelector('.btn-text').textContent = 'Calculando...';

  try {
    const response = await fetch('/calcular', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        numero1: parseFloat(numero1),
        numero2: parseFloat(numero2),
        operacao: operacao,
      }),
    });

    const dados = await response.json();

    if (!response.ok || dados.erro) {
      exibirErro(dados.erro || 'Erro desconhecido.');
    } else {
      exibirResultado(dados.resultado);
    }
  } catch (error) {
    exibirErro('Erro ao conectar com o servidor. Verifique se o Flask está rodando.');
  } finally {
    btn.disabled = false;
    btn.querySelector('.btn-text').textContent = 'Calcular';
  }
}

function exibirResultado(valor) {
  const container = document.getElementById('resultado-container');
  const resultadoEl = document.getElementById('resultado');
  const labelEl = document.getElementById('resultado-label');

  container.classList.remove('hidden', 'erro', 'sucesso');
  // Força re-render da animação
  void container.offsetWidth;

  container.classList.add('sucesso');
  labelEl.textContent = 'Resultado';
  resultadoEl.textContent = valor;
}

function exibirErro(mensagem) {
  const container = document.getElementById('resultado-container');
  const resultadoEl = document.getElementById('resultado');
  const labelEl = document.getElementById('resultado-label');

  container.classList.remove('hidden', 'erro', 'sucesso');
  void container.offsetWidth;

  container.classList.add('erro');
  labelEl.textContent = 'Erro';
  resultadoEl.textContent = mensagem;
}

// Permite acionar o cálculo com Enter nos campos de input
document.addEventListener('DOMContentLoaded', () => {
  const inputs = document.querySelectorAll('.input');
  inputs.forEach(input => {
    input.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') calcular();
    });
  });
});
