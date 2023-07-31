"""
 conceito do polimorfismo é permitir que comportamentos comuns a N tipos de classes possam ser definidos de forma
 especifica para cada classe.

Imagine que um sistema bancário, define que uma ContaCorrente e uma ContaPoupaca devem ter saldo, titular, numero da
conta, um método para sacar, depositar e exibir o saldo, mas, cada classe tem suas próprias regras de negócio,
por exemplo, na ContaCorrente, o saque vai ter algum tipo de desconto dependendo de onde for sacado e a ContaPoupanca
o deposito vai ser salvo em outro tipo de saldo interno, etc.

A questão é, possuem comportamentos diferentes mas devem possuir os comportamentos porque ambas são Contas.

Por exemplo, eu posso criar uma classe abstrata chamada Conta e a partir dela definir quais são os atributos e
comportamentos necessários para quem for herdar dela mas as regras de negócio cada classe implementa a sua maneira,
com o caso aqui em que ContaPoupanca herda de Conta (classe abstrata) e implementa suas próprias regras de negócio
(gerando o comportamento polimórfico das Contas):
"""


# de uma forma bem lúdica e rapida podemos ver o polimofismo abaixo, lembrando que nesse caso o polimorfimo, foi o ato
# herda a classe PessoaA em PessoaB e fazer a alteração da fala no metodo se_aprensentar, isso é polimorfismo. (mudar)

class PessoaA:
    def se_apresentar(self):
        print("Olá, sou a pessoa A")


class PessoaB:
    def __init__(self):
        super().__init__()

    def se_aprensentar(self):
        print("Estou alterando esse metodo")


pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_aprensentar()
