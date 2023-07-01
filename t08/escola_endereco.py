from typing import Union


class Endereco:
    def __init__(self,
                 logradouro: str,
                 cep: str,
                 numero: Union[int, None]) -> None:

        self.logradouro = logradouro
        self.cep = cep
        self.numero = numero


class Escola:
    def __init__(self,
                 nome: str,
                 capacidade_para_alunos: int,
                 endereco: Endereco):

        self.nome = nome
        self.capacidade = capacidade_para_alunos
        self.endereco = endereco
