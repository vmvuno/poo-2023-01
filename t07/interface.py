import abc
from typing import Union


# Python não implementa interfaces de forma nativa
# A melhor aproximação possível na linguagem é implementar uma metaclasse
# com métodos e propriedades abstratas
#
# Caso uma classe herde da interface sem implementar os métodos e propriedades,
# erros são elevados/lançados.
class InterfaceProvaFormal(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: object) -> bool:
        return hasattr(subclass, "nome") and not callable(subclass.nome)

    @property
    @abc.abstractmethod
    def nome(self) -> Union[None, str]:
        raise NotImplementedError  # pragma: no cover
        # O erro é excluído da análise de cobertura, uma vez que,
        # ao tentar instanciar uma classe sem este método,
        # é elevado TypeError, pois não é possível instanciar
        # uma classe abstrata com um método abstrato


class InterfaceProvaFormal2(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass: object) -> bool:
        return hasattr(subclass, "get_nome") and callable(subclass.get_nome)

    @abc.abstractmethod
    def get_nome(self) -> Union[None, str]:
        raise NotImplementedError  # pragma: no cover
        # O erro é excluído da análise de cobertura, uma vez que,
        # ao tentar instanciar uma classe sem este método,
        # é elevado TypeError, pois não é possível instanciar
        # uma classe abstrata com um método abstrato
