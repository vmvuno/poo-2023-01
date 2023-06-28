from t07.interface import InterfaceProvaFormal, InterfaceProvaFormal2
from typing import Union


# A classe herda da interface, obedecendo os métodos e atributos lá declarados.
class ProvaComIdentificacaoPithonico(InterfaceProvaFormal):
    __nome: Union[None, str] = None

    # Implementação de nome enquanto propriedade ao invés da função getNome
    @property
    def nome(self) -> Union[None, str]:
        return self.__nome


class ProvaComIdentificacaoConvencional(InterfaceProvaFormal2):
    __nome: Union[None, str] = None

    def get_nome(self) -> Union[None, str]:
        return self.__nome
