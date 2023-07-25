"""
@property - Getters e Setters - Python Orientado a Objetos
@property (getters) e setters, que são métodos para controlar
(validar) a entrada e saída de dados
dos atributos dos nossos objetos.
"""


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))

        self._preco = valor


# Aqui vamos imaginar que alguém conseguiu alterar o segundo paramentro
# que deveria receber um número e conseguiram trocar por acidente
# o valor inteiro por "R$50", sendo assim o dado que a classe receberá
# vai causar o erro no codigo, para isso que serve @property (getters) e setters
# para: controlar (validar) a entrada e saída de dados
# Para concertar, colocamos um getter e setter validando o dado
# no caso, demos um raplace no RS e trandormando o dado para float.
produto_1 = Produto('Camisa', 'R$50')
produto_1.desconto(10)
print(produto_1.preco)
