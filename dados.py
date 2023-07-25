from dados_clientes import CadastroClientes

print("* Cadastro de Clientes *")


def tela_de_cadastro():
    cpf = input("Cpf: ")
    nome = input("Nome: ")
    sexo = input("Sexo: ")
    data_nascimento = input("Data de nascimento: ")
    print(f"Inserção de dados concluida, enviando dados do Clinte: {nome}")
    return cpf, nome, sexo, data_nascimento

    # Clientes = CadastroClientes(cpf, nome, sexo, data_nascimento)
    # Clientes.cadastro()
    # print(Clientes.banco_de_dados)

    # Depois pegamos os dados que estarão armazenados na variavel run e inserimos no banco.


if __name__ == "__main__":
    tela_de_cadastro()
