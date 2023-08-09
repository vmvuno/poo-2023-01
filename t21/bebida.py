from t21.preco import Preco


class Bebida:
    def __init__(self,
                 nome: str,
                 preco: Preco) -> None:
        self.nome = nome
        self.preco = preco
