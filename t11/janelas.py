class Janela:
    def __init__(self, area_total: float) -> None:
        self.area_total = area_total


class JanelaComVidro(Janela):
    def __init__(self, area_total: float, area_do_vidro: float) -> None:
        super().__init__(area_total)
        self.area_com_vidro = area_do_vidro
        self.area_sem_vidro = area_total - area_do_vidro
