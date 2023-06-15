from __future__ import annotations
from datetime import date
from typing import Union


class Pessoa:
    _nascimento: Union[date, None] = None
    _nome: Union[str, None] = None
    _pai: Union[Pessoa, None] = None
    _mae: Union[Pessoa, None] = None
