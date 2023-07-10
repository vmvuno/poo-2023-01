class Pagamento:
    pass


class Hora(Pagamento):
    pass


class Mensal(Pagamento):
    pass


class Contrato(Pagamento):
    pass


class Tarefa:
    def __init__(self, pagamento: Pagamento) -> None:
        self.pagamento = pagamento


class Trabalhador:
    def __init__(self, trabalho: Tarefa) -> None:
        self.trabalho_desempenhado = trabalho
