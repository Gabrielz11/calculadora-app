class Calculadora:
    def somar(self, a, b):
        if not self._is_integer(a) or not self._is_integer(b):
            raise ValueError("A operação de soma aceita apenas números inteiros")
        return a + b

    def subtrair(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            raise ValueError("Não é possível dividir por zero")
        return a / b

    def executar(self, dados):
        """
        Orquestrador de alto nível.
        Recebe o dicionário bruto e entrega o resultado pronto.
        """
        # 1. Validação de presença
        n1 = dados.get('numero1')
        n2 = dados.get('numero2')
        op = dados.get('operacao')

        if n1 is None or n2 is None or op is None:
            raise ValueError("Os campos numero1, numero2 e operacao são obrigatórios")

        # 2. Conversão e Validação de tipos
        try:
            n1, n2 = float(n1), float(n2)
        except (ValueError, TypeError):
            raise ValueError("Os valores inseridos devem ser numéricos")

        # 3. Mapeamento
        operacoes = {
            'soma': self.somar,
            'subtracao': self.subtrair,
            'multiplicacao': self.multiplicar,
            'divisao': self.dividir,
        }

        if op not in operacoes:
            raise ValueError(f"Operação '{op}' inválida")

        # 4. Execução
        resultado = operacoes[op](n1, n2)

        # 5. Formatação de saída (Limpeza de decimais desnecessários)
        return int(resultado) if resultado == int(resultado) else resultado

    def _is_integer(self, n):
        return n == int(n)
