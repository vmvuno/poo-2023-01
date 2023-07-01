from typing import Union


class LinguagemDeProgramação:
    pass


class Projeto:
    def __init__(
            self,
            linguagens: Union[list[LinguagemDeProgramação], None] = None
            ) -> None:

        if linguagens is None:
            self.linguagens = []

        else:
            self.linguagens = linguagens
