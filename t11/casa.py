from typing import Union


class Garagem:
    pass


class Banheiro:
    pass


class Quarto:
    pass


class Area:
    pass


class Sala:
    pass


class Casa:
    def __init__(
            self,
            *comodos: Union[Garagem, Banheiro, Quarto, Area, Sala]
    ) -> None:

        self._comodos: list[Union[Garagem, Banheiro, Quarto, Area, Sala]] = []
        self._comodos.extend(comodos)
