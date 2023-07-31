"""
_______ explicação da pesquisa ________
O princípio de encapsulamento consiste em "esconder" a parte funcional dos objetos de forma que quem estiver
utilizando não tenha que conhecer mais do que o necessário para utiliza-lo.

Por exemplo, ao dirigir um carro, se quisermos que o carro pare de andar, não é preciso, conhecer toda a mecânica do
funcionamento por dentro do veículo para que possamos frear. Basta pisar no freio, o freio é o encapsulamento do
comportamento de frear de um carro.

Na orientação a objetos, estruturamos as classes de forma a encapsular toda regra de negócio e parte funcional
relacionada a classe dentro de métodos e atributos, de forma que quem utilize, apenas diga oque quer fazer.
_______ explicação da pesquisa ________

_______ Minha explicação ________
Encapsulamento, é uma parte da programação Orientada a objetos, que serve para 'Esconder' certas partes do código.
Por exemplo, esconder sua classe atributo ou método. E no Python diverge muito da forma que é feita em outras
linguagens.
public => atributo ou método que podem ser acessados dentro e fora da classe.
protected => atributo ou método que podem ser acessados dentro apenas dentro da classe, ou das filhas (herança)
private => atributo ou método só está disponivel dentro da classe.
_______ Minha explicação ________
Exemplo abaixo:
"""


class BaseDeDados:
    # Construtor do Python.
    def __init__(self):
        # FIXME: protected _
        # A variavel com o _ não deve ser acessada, a variavel
        # foi acessada para ser acessada dentro da classe.
        # Serve tanto para atributo quanto metodo, ex: self._dados
        # ou def _inserir_cliente(self, id_cliente, nome):
        # FIXME: private __
        # O private é como se o python falasse para não acessar de maneira nenhuma
        # para acessar bd._BaseDeDados__dados
        # Para acessar sem que afete a variavel ou o meto podemos criar uma função com o
        # decorator @property def dados(self): return self.__dados
        self.__dados = {}

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id_cliente, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id_cliente: nome}
        else:
            self.__dados['clientes'].update({id_cliente: nome})

    def lista_clientes(self):
        for id_cliente, nome in self.__dados['clientes'].items():
            print(id_cliente, nome)

    def apaga_clientes(self, id_clientes):
        del self.__dados['clientes'][id_clientes]


if __name__ == "__main__":
    bd = BaseDeDados()
    bd.inserir_cliente(1, "Lucas")
    bd.inserir_cliente(2, "Silba")
    bd.inserir_cliente(3, "Alves")
    bd.inserir_cliente(4, "Teste")
    print(bd.dados)


