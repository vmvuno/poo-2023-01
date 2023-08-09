from __future__ import annotations

from t22.pessoa import Pessoa


# Para uma melhor organização,
# classes afins foram agrupadas num mesmo arquivo/módulo
#
# Pelo modelo, uma pessoa pode ser associada a um visitante ou trabalhador,
# mas não ficou claro, pelo minicontexto, como a pessoa estaria associada
# a um visitante ou trabalhandor.
# Portanto, julgou-se adequado substituir a associação entre pessoa e visitante
# no modelo por uma relação de herança, visto que um visitante é uma pessoa.
class Visitante(Pessoa):
    def __init__(
        self,
        criancas: set[Crianca]
    ) -> None:
        pass


class Crianca(Visitante):
    def __init__(
            self,
            acompanhantes: set[Visitante]
    ) -> None:
        self.acompanhantes = acompanhantes


class Parente(Visitante):
    pass


# Indicado no modelo como Outro
# O nome "Outro" não é descritivo, por isso foi alterado
class Familiar(Parente):
    pass


class Pai(Parente):
    pass
