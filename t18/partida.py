from typing import Union
import re


class Jogador:
    def __init__(self,
                 nome: str) -> None:

        self.nome = nome

    def __str__(self) -> str:
        return self.nome


class Peca:
    def __init__(self,
                 notacao: str) -> None:

        if len(notacao) > 1:
            notacao = notacao[0]

        if notacao == 'D':
            self.nome = 'Rainha'

        elif notacao == 'R':
            self.nome = 'Rei'

        elif notacao == 'T':
            self.nome = 'Torre'

        elif notacao == 'B':
            self.nome = 'Bispo'

        elif notacao == 'C':
            self.nome = 'Cavalo'

        else:
            self.nome = 'Peão'

    @property
    def pronome_possessivo(self) -> str:
        if self.nome in {'Rainha', 'Torre'}:
            return 'sua'

        return 'seu'

    def __str__(self) -> str:
        return self.nome


class Posicao:
    def __init__(self,
                 coluna: str,
                 linha: int) -> None:
        self.coluna = coluna
        self.linha = linha

    def __str__(self) -> str:
        return f'{self.coluna.lower()}{self.linha}'


class Lance:
    def __init__(self,
                 jogador: Jogador,
                 peca: Peca,
                 destino: Posicao,
                 captura: bool,
                 cheque: bool,
                 cheque_mate: bool) -> None:
        self.jogador = jogador
        self.peca = peca
        self.destino = destino
        self.captura = captura
        self.cheque = cheque
        self.cheque_mate = cheque_mate

    def __str__(self) -> str:
        return_str = f'{self.jogador} move '
        return_str += f'{self.peca.pronome_possessivo} {self.peca} '
        return_str += f'para a casa {self.destino}'

        if self.captura:
            if self.cheque or self.cheque_mate:
                return_str += ', '

            else:
                return_str += ' e '

            return_str += 'captura uma peça'

        if self.cheque:
            return_str += ' e coloca seu adversário em cheque'

        elif self.cheque_mate:
            return_str += ', concluindo o jogo, com um cheque-mate'

        return return_str


class Rodada:
    def __init__(self,
                 numero: int,
                 lance_brancas: Lance,
                 lance_pretas: Union[Lance, None]) -> None:
        self.numero = numero
        self.lances = (lance_brancas, lance_pretas)

    def __str__(self) -> str:
        return_str = f'Rodada {self.numero}:'
        return_str += f'\n{self.lances[0]}'

        if self.lances[1] is not None:
            return_str += f'\n{self.lances[1]}\n\n'

        return return_str


class Partida:
    def __init__(self,
                 brancas: Jogador,
                 pretas: Jogador) -> None:
        self.rodadas: list[Rodada] = []
        self.jogador_brancas = brancas
        self.jogador_pretas = pretas

    def ler_jogadas_de_arquivo(self,
                               caminho_do_arquivo: str) -> None:

        with open(caminho_do_arquivo, 'r', encoding='utf8') as file_handle:
            data = file_handle.readlines()

        lances: list[Lance] = []
        for i in range(0, len(data)):
            notacao = data[i].strip()

            captura = 'x' in notacao
            cheque = False
            cheque_mate = False

            if i % 2 == 0:
                jogador = self.jogador_brancas
                lances = []
            else:
                jogador = self.jogador_pretas

            search = re.search(
                r'(?P<peca>[TCBRD]?[a-e]?)x?'
                r'(?P<destino>[a-h][1-8])'
                r'(?P<cheque_tag>[+#])?',
                notacao
                )

            if search is not None:
                peca = Peca(search['peca'])
                destino = Posicao(str(search['destino'][0]),
                                  int(search['destino'][1]))

                cheque_tag = search['cheque_tag']
                if cheque_tag == '+':
                    cheque = True

                elif cheque_tag == '#':
                    cheque_mate = True

                lances.append(
                    Lance(jogador,
                          peca,
                          destino,
                          captura,
                          cheque,
                          cheque_mate
                          )
                    )

            if i % 2 == 1 or cheque_mate:
                if len(lances) == 2:
                    self.rodadas.append(
                        Rodada((i//2) + 1, lances[0], lances[1])
                    )

                else:
                    self.rodadas.append(
                        Rodada((i//2) + 1, lances[0], None)
                    )

    def __str__(self) -> str:
        return_str = ''
        return_str += f'Brancas: {self.jogador_brancas}\n'
        return_str += f'Pretas : {self.jogador_pretas}\n\n'

        for rodada in self.rodadas:
            return_str += str(rodada)

        return return_str


if __name__ == '__main__':
    partida_imortal = Partida(
        brancas=Jogador('Adolf Anderssen'),
        pretas=Jogador('Lionel Kiesseritzky')
        )

    partida_imortal.ler_jogadas_de_arquivo('imortal.txt')
    print(partida_imortal)
