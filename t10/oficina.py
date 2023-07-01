from t10.pessoa import Pessoa
from t10.mecanico import Mecanico
from t10.passeio_ciclistico import PasseioCiclistico
from t10.cliente_ciclista import ClienteCiclista


class Oficina:
    def __init__(self,
                 nome: str,
                 cnpj: str,
                 proprietarios: list[Pessoa]) -> None:
        self._nome = nome
        self._cnpj = cnpj
        self._proprietarios = proprietarios
        self._mecanicos: list[Mecanico] = []
        self._eventos: list[PasseioCiclistico] = []
        self._clientes: list[ClienteCiclista] = []

    def contratar(self, mecanico: Mecanico) -> None:
        if mecanico not in self._mecanicos:
            self._mecanicos.append(mecanico)

    def dispensar(self, mecanico: Mecanico) -> None:
        if mecanico in self._mecanicos:
            self._mecanicos.remove(mecanico)

    def criar_evento(self, evento: PasseioCiclistico) -> None:
        if evento not in self._eventos:
            self._eventos.append(evento)

        evento.convidar_clientes(self._clientes)

    def conhecer_cliente(self, cliente: ClienteCiclista) -> None:
        if cliente not in self._clientes:
            self._clientes.append(cliente)
