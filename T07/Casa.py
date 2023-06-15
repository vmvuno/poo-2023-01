class Casa:
    def __init__(self) -> None:
        print("Mais uma casa...")


if __name__ == "__main__":
    c = Casa()  # pragma: no cover
    # A esclusão desta linha na análise de cobertura se dá
    # porque o arquivo de testes já implementa este caso.
