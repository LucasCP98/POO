# class Cliente:
#     def __init__(self, nome: str):
#         self._nome = nome
#
#     @property
#     def nome(self):
#         return self._nome
#
#
# if __name__ == "__main__":
#     var = Cliente("Carlos")
#     coisa = var.nome
#     print(coisa)
#
class Cliente:
    def __init__(self, numero_1: int, numero_2: int):
        self.numero_1: int = numero_1
        self.numero_2: int = numero_2

    def soma(self):
        return self.numero_1 + self.numero_2


if __name__ == "__main__":
    var = Cliente(1, 1)
    print(var.soma())
