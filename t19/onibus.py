from __future__ import annotations


class Cidade:
    def __init__(self, nome: str) -> None:
        self._nome = nome

    @property
    def nome(self) -> str:
        return self._nome


class Onibus:
    def __init__(self) -> None:
        # No diagrama presente na proposta do exercício, a classe ônibus herda
        # de viagem.
        # Esse comportamento não é adequado, visto que um ônibus não é
        # uma viagem e, conforme o texto do enunciado, um ônibus pode
        # realizar várias viagens.
        #
        # Portanto, na implementação, a classe Onibus tem uma relação
        # de agregação com a classe Viagem.
        self.viagens: list[Viagem] = []

    def adicionar_viagem(self, viagem: Viagem) -> None:
        self.viagens.append(viagem)


class Papel:
    def __init__(self) -> None:
        self.viagens: list[Viagem] = []

    def adicionar_viagem(self, viagem: Viagem) -> None:
        self.viagens.append(viagem)


class Passageiro(Papel):
    def __init__(self) -> None:
        super().__init__()


class Motorista(Papel):
    def __init__(self) -> None:
        super().__init__()


# Vários outros métodos poderiam ser adicionados às classes Onibus e Viagens
# a fim modelar melhor os comportamentos reais, como a ocorrência de paradas,
# embarque e desembarque de passageiros.
# Tais adições, entretanto, não estão inclusas na proposta do exercício.
class Viagem:
    def __init__(self,
                 origem: Cidade,
                 destino: Cidade,
                 passageiros: list[Passageiro],
                 motorista: Motorista,
                 onibus: Onibus
                 ) -> None:
        self.origem = origem
        self.destino = destino
        self.passageiros = passageiros
        self.motorista = motorista

        for passageiro in self.passageiros:
            passageiro.adicionar_viagem(self)

        motorista.adicionar_viagem(self)

        self.onibus = onibus
        onibus.adicionar_viagem(self)
