from typing import Union


class Pessoa:
    # Python não implementa o controle de acesso a variáveis
    #
    # Por conveção, variáveis iniciadas por underscore
    # não devem ser acessadas diretamente,
    # mesmo que a linguagem permita
    _dia: Union[int, None] = None
    _mes: Union[int, None] = None
    _ano: Union[int, None] = None

    idade: Union[int, None] = None

    # Python é uma linguagem que implementa tipagem dinãmica,
    # logo, não é necessário declarar tipos
    #
    # Recentemente, a linguagem passou a incluir a possibilidade
    # de anotaçoes de tipo, como visto acima, entretanto,
    # a linguagem não realiza checagem de tipo durante a execução.
