from datetime import datetime, timedelta


class Data:
    def __init__(
            self,
            data_abertura: datetime,
            periodo: timedelta
    ) -> None:
        self.data_abertura = data_abertura
        self.periodo = periodo
