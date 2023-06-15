class Permuta:
    def __init__(self, prefixo: str, sequencia: str) -> None:
        self.permutacao(prefixo, sequencia)

    def permutacao(self, prefixo: str, sequencia: str) -> None:
        if len(sequencia) == 1:
            print(prefixo + sequencia)

        else:
            s_linha: str = ""
            p_linha: str = ""

            for i in range(0, len(sequencia)):
                s_linha = sequencia[0:i] + sequencia[(i + 1):]
                p_linha = prefixo + sequencia[i]
                self.permutacao(p_linha, s_linha)


if __name__ == "__main__":
    Permuta("", "abc")  # pragma: no cover
    # A esclusão desta linha na análise de cobertura se dá
    # porque o arquivo de testes já implementa este caso.
