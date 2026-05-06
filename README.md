# Calculadora App - BDD com Behave

Este é um projeto simples de uma calculadora em Python, desenvolvido para demonstrar o uso de **BDD (Behavior-Driven Development)** utilizando o framework **Behave**.

## 🚀 Funcionalidades

A calculadora suporta as seguintes operações:
- Soma
- Subtração
- Multiplicação
- Divisão (com tratamento de erro para divisão por zero)

## 🛠️ Tecnologias Utilizadas

- **Python 3.x**
- **Behave**: Framework para testes BDD.

## 📁 Estrutura do Projeto

```text
calculadora_app/
├── features/               # Arquivos .feature com os cenários BDD
│   └── calculadora.feature
├── features/steps/         # Implementação dos passos (step definitions)
│   └── calculadora_steps.py
├── src/                    # Código fonte da calculadora
│   └── calculadora.py
├── .gitignore
├── requirements.txt
└── README.md
```

## ⚙️ Como Executar

### 1. Pré-requisitos

Certifique-se de ter o Python instalado. É recomendável utilizar um ambiente virtual.

### 2. Instalação das Dependências

Instale o framework Behave através do pip:

```bash
pip install -r requirements.txt
```

### 3. Executando os Testes

Para rodar os testes BDD e verificar se as operações da calculadora estão funcionando conforme o esperado, execute o comando abaixo na raiz do projeto:

```bash
behave
```

O Behave irá ler os arquivos na pasta `features/` e executar os passos definidos em `features/steps/`.

## 🧪 Exemplo de Cenário

O arquivo `calculadora.feature` define cenários como:

```gherkin
Scenario: Somar dois números
    Given que iniciei a calculadora
    When soma 5 e 3
    Then o resultado deve ser 8
```
