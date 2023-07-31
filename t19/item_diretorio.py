from typing import Union


class Arquivo:
    pass


class ItemDiretorio:
    pass


class Diretorio(ItemDiretorio):
    def __init__(self,
                 conteudo_diretorio: list[Union[Arquivo,
                                                ItemDiretorio]]) -> None:
        self.conteudo = conteudo_diretorio
