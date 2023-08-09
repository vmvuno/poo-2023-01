from typing import Union


# Classe não mostrada no modelo,
# Implementada para atender o item 3:
# Alguns brinquedos são pagos, outros são usados gratuitamente
class Brinquedo:
    def __init__(self,
                 nome: str,
                 idade_minima: Union[int, None],
                 idade_maxima: Union[int, None],
                 peso_minimo: Union[float, None],
                 peso_maximo: Union[float, None],
                 requer_bilhete: bool) -> None:

        self.nome = nome
        self.idade_minima = idade_minima
        self.idade_maxima = idade_maxima
        self.peso_minimo = peso_minimo
        self.peso_maximo = peso_maximo
        self.requer_bilhete = requer_bilhete
