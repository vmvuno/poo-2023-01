from typing import Union


class Prova:
    # Em códigos orientados a objetos em python,
    # o usual é acessar as variáveis diretamente

    _num_questoes: Union[int, None] = None

    # Uma forma de implementar métodos getters e setters é a utilização
    # de propriedades.
    # Assim, a propriedade retém a mesma forma de acesso esperada na linguagem,
    # adicionando comportamentos esperados da utilização de getters e setters.
    @property
    def num_questoes(self) -> Union[int, None]:
        return self._num_questoes

    @num_questoes.setter
    def num_questoes(self, numero: int) -> None:
        if numero > 0:
            self._num_questoes = numero
