from datetime import date
from typing import Union


# Por padrão, novas classes herdam de object,
# portanto, o (object) é opcional
class Pessoa:
    nome: Union[str, None] = None
    nascimento: Union[date, None] = None
