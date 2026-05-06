<h1 align="center">🧮 Calculadora App</h1>

<p align="center">
  Calculadora web com arquitetura limpa, desenvolvida com Python + Flask e validada por testes automatizados BDD com Behave e Selenium.
</p>

<p align="center">
  [![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
  [![Behave](https://img.shields.io/badge/Behave-BDD-green?style=for-the-badge)](https://behave.readthedocs.io/)
  [![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
  [![License](https://img.shields.io/badge/Licença-MIT-blue?style=for-the-badge)](LICENSE)
</p>

---

## 📋 Tabela de Conteúdos

- [Sobre](#-sobre)
- [Funcionalidades](#-funcionalidades)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Pré-requisitos](#-pré-requisitos)
- [Como Rodar](#-como-rodar)
- [Contribuição](#-contribuição)
- [Licença](#-licença)

---

## 📖 Sobre

O **Calculadora App** é uma aplicação web de calculadora com foco em boas práticas de engenharia de software. O projeto foi desenvolvido para demonstrar:

- **Arquitetura Limpa**: separação total entre camada de domínio (lógica de negócio), camada web (Flask) e camada de apresentação (HTML/CSS/JS).
- **Skinny Routes**: rotas Flask com responsabilidade única, sem lógica de negócio misturada.
- **Global Error Handling**: erros tratados de forma centralizada, sem `try/except` espalhado pelo código.
- **BDD (Behavior-Driven Development)**: comportamento da aplicação descrito em linguagem natural (Gherkin) e validado em dois níveis: testes unitários e testes de interface E2E com Selenium.

### Estrutura do Projeto

```
calculadora-app/
│
├── src/
│   ├── calculadora.py        # Domínio: toda a lógica de negócio e regras
│   └── app.py                # Web: rotas Flask e error handlers globais
│
├── templates/
│   └── index.html            # Interface HTML da calculadora
│
├── static/
│   ├── style.css             # Estilos e design da interface
│   └── script.js             # Lógica de interação do usuário (fetch API)
│
├── features/
│   ├── calculadora.feature       # Cenários BDD de unidade (sem navegador)
│   ├── calculadora_ui.feature    # Cenários BDD de interface E2E (Selenium)
│   ├── environment.py            # Ciclo de vida do WebDriver
│   └── steps/
│       ├── calculadora_steps.py      # Steps dos testes de unidade
│       └── calculadora_ui_steps.py   # Steps dos testes de interface
│
├── requirements.txt
└── README.md
```

---

## ⚡ Funcionalidades

| Funcionalidade | Descrição |
|---|---|
| ➕ **Soma** | Soma dois números **inteiros** (decimais são rejeitados por regra de negócio) |
| ➖ **Subtração** | Subtrai dois números, suportando resultados negativos |
| ✖ **Multiplicação** | Multiplica dois números, incluindo negativos |
| ➗ **Divisão** | Divide dois números com suporte a resultado decimal |
| 🚫 **Divisão por zero** | Bloqueia a operação e exibe mensagem de erro adequada |
| ⌨️ **Atalho Enter** | Permite calcular pressionando Enter nos campos de input |
| 📱 **Interface Responsiva** | Layout adaptado para diferentes tamanhos de tela |

---

## 🛠️ Tecnologias Utilizadas

### Backend
| Tecnologia | Uso |
|---|---|
| **Python 3.x** | Linguagem principal |
| **Flask** | Framework web — roteamento e servidor HTTP |

### Frontend
| Tecnologia | Uso |
|---|---|
| **HTML5** | Estrutura semântica da interface |
| **CSS3** | Estilização com design dark mode e glassmorphism |
| **JavaScript (Vanilla)** | Comunicação com a API via `fetch` assíncrono |

### Testes
| Tecnologia | Uso |
|---|---|
| **Behave** | Framework BDD — interpreta os cenários Gherkin |
| **Gherkin** | Linguagem para descrição dos cenários em linguagem natural |
| **Selenium** | Automação do navegador para testes E2E |
| **WebDriver Manager** | Gerencia automaticamente o driver do Chrome |

---

## ✅ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

- [Python 3.8+](https://www.python.org/downloads/)
- [Google Chrome](https://www.google.com/chrome/) (necessário para os testes E2E com Selenium)
- `pip` (gerenciador de pacotes do Python — incluído com o Python)

> **Recomendado:** utilizar um ambiente virtual para isolar as dependências do projeto.

---

## 🚀 Como Rodar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/calculadora-app.git
cd calculadora-app
```

### 2. Crie e ative um ambiente virtual (recomendado)

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Inicie o servidor Flask

```bash
python src/app.py
```

A aplicação estará disponível em: **http://localhost:5000**

---

### 5. Executando os Testes BDD

> ⚠️ Mantenha o servidor Flask rodando em um terminal antes de executar os testes.

#### Todos os testes (unidade + interface E2E):
```bash
behave
```

#### Apenas testes de unidade (rápido, sem navegador, sem Flask):
```bash
behave features/calculadora.feature
```

#### Apenas testes de interface E2E (abre o Chrome):
```bash
behave features/calculadora_ui.feature
```

#### Resultado esperado:
```
2 features passed, 0 failed, 0 skipped
24 scenarios passed, 0 failed, 0 skipped
126 steps passed, 0 failed, 0 skipped
~ Took 0min 30.218s
```

> 💡 **Dica:** Para rodar os testes sem abrir o Chrome visualmente (modo headless),
> abra o arquivo `features/environment.py` e remova o comentário da linha:
> ```python
> options.add_argument("--headless")
> ```

---

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um **fork** do projeto
2. Crie uma branch para sua feature: `git checkout -b feature/minha-feature`
3. Faça o commit das suas alterações: `git commit -m 'feat: adiciona minha feature'`
4. Faça o push para a branch: `git push origin feature/minha-feature`
5. Abra um **Pull Request**

> Certifique-se de que todos os testes BDD passam antes de abrir o Pull Request.

---

## 📄 Licença

Este projeto está sob a licença **MIT**. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

<p align="center">
  Desenvolvido com ❤️ utilizando Python · Flask · BDD
</p>
