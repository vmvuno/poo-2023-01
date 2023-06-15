from abc import ABCMeta


class Pessoa(metaclass=ABCMeta):
    def __init__(self, nome: str, endereco: str) -> None:
        self.nome = nome
        self.endereco = endereco


class PessoaFisica(Pessoa):
    def __init__(self,
                 nome: str,
                 endereco: str,
                 cpf: str,
                 cor_pele: str) -> None:
        super().__init__(nome, endereco)
        self.cpf = cpf
        self.cor_pele = cor_pele


class PessoaJuridica(Pessoa):
    def __init__(self,
                 nome: str,
                 endereco: str,
                 cnpj: str,
                 nome_fantasia: str) -> None:
        super().__init__(nome, endereco)
        self.cnpj = cnpj
        self.nome_fantasia = nome_fantasia
