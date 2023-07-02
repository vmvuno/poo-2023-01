from typing import Union


class Livro:
    pass


class CD:
    pass


class Compartimento:
    def __init__(self, conteudo: list[Union[Livro, CD]]) -> None:
        tipos_guardados = {item.__class__ for item in conteudo}

        if len(tipos_guardados) > 1:
            raise ValueError('Só é possível guardar um tipo de item por vez')

        if 'Livro' in tipos_guardados \
           and len(conteudo) > 3:
            raise ValueError('Só é possível guardar até três livros')

        if 'CD' in tipos_guardados \
                and (
                    len(conteudo) < 8
                    and len(conteudo) != 7
                    and len(conteudo) != 4
                    and len(conteudo) != 2
                    ):

            raise ValueError(
                'Só é possível guardar, 2, 4, 7 ou mais de 7 CDs por vez'
            )

        self._conteudo = conteudo


class Prateleira:
    def __init__(self) -> None:
        self._compartimentos: list[Compartimento] = []

    def adicionar_compartimento(
            self,
            conteudo: list[Union[Livro, CD]]
            ) -> None:

        self._compartimentos.append(
            Compartimento(conteudo)
        )

    def remover_compartimento(self, compartimento: Compartimento) -> None:
        self._compartimentos.remove(compartimento)


class Armario:
    def __init__(self, n_prateleiras: int) -> None:
        if n_prateleiras < 1:
            raise ValueError(
                'Um armário deve possuir, pelo menos, uma prateleira'
                )

        self._prateleiras: list[Prateleira] = \
            [Prateleira() for i in range(n_prateleiras)]
