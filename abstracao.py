"""
Na programação orientada a objetos, a construção dos objetos é baseada em uma Classe que representa as características
daquele objeto.

Abstração é o princípio de criar uma classe que contenha atributos e métodos que "são comuns a outras classes e que
podem servir como base para serem herdados".

Você abstrai características comuns a N classes e fornece uma classe abstrata que pode ser "herdada e servir de base
para as demais".

Exemplo abaixo:
"""
from abc import ABCMeta, abstractmethod


class Conta(metaclass=ABCMeta):
    _numero = "00000"
    _titular = "root"
    saldo = 0

    @abstractmethod
    def __init__(self, numero: str, titular: str, saldo: float):
        self._numero = numero
        self._titular = titular
        self.saldo = saldo

    @abstractmethod
    def sacar(self, value: float):
        pass

    @abstractmethod
    def depositar(self, value: float):
        pass

    @abstractmethod
    def exibir_saldo(self):
        pass
