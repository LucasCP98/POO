
class CadastroClientes:
    def __init__(self, cpf, nome, sexo, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.sexo = sexo
        self.data_nascimento = data_nascimento
        self.banco_de_dados = {}

    def cadastro(self):
        self.banco_de_dados['cpf'] = self.cpf
        self.banco_de_dados['nome'] = self.nome
        self.banco_de_dados['sexo'] = self.sexo
        self.banco_de_dados['data_nascimento'] = self.data_nascimento

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, dados):
        if isinstance(dados, str):
            dados = int(dados)

        self._cpf = dados


# if __name__ == "__main__":
#     run = CadastroClientes("05427269126", "Lucas Costa Pereira", "M", "12/02/1998")
#     run.cadastro()
#     print(run.banco_de_dados)
#     print(run.banco_de_dados['cpf'])
#     print(run.banco_de_dados['nome'])
#     print(run.banco_de_dados['sexo'])
#     print(run.banco_de_dados['data_nascimento'])
