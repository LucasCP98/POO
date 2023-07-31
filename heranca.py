"""
A herança consiste em determinar que uma classe existe por si mesma, porém, ela é uma outra classe em sua essência...
Por exemplo, uma ContaCorrente existe mas ela é uma Conta.

Quando a herança é utilizada, a classe que herda, automaticamente, possui os atributos e métodos definidos na classe da
qual herdou.

Por exemplo, imagine que o sistema bancário tenha uma uma regra geral para deposito e exibição de saldo para todos os
tipos de conta somente o saque muda de conta para conta. Nesse caso, podemos criar uma classe Conta com as
características comuns das outras Contas, e as outras contas, irão herdar essas características:
"""

from util import Cliente


# ------------------------------------------------------------------------------------------------------------
# Para aplicar a herança em Python, basta referênciar a classe que se quer herdar entre parenteses:
class ContaPoupaca(Cliente):

    def __init__(self, numero_1: int, numero_2: int):
        super().__init__(numero_1, numero_2)


f = ContaPoupaca(34, 34)
print(f.soma())

# ------------------------------------------------------------------------------------------------------------
# forma diferente de outro exemplo:
# class Conta():
#     _numero = "00000"
#     _titular = "root"
#     saldo = 0
#
#     def __init__(self, numero: str, titular: str, saldo: float):
#         self._numero = numero
#         self._titular = titular
#         self.saldo = saldo
#
#     def depositar(self, value: float):
#         # Regra para fazer o depósito...
#
#     def exibir_saldo(self):
#         # Exiba o saldo...
#
# # Para aplicar a herança em Python, basta referênciar a classe que se quer herdar entre parenteses:
# class ContaPoupaca(Conta):
#
#     def __init__(self, numero: str, titular: str, saldo: float):
#         super().__init__(numero, titular, saldo)
#
#     def sacar(self, value: float):
#         if value <= self._saldo:
#             self._saldo -= value
#             return True
#
#         return False
#
#     def titular(self):
#         return self._titular
#
#     def numero(self):
#         return self._numero
