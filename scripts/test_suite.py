import subprocess
from os import system, name


def clear() -> None:
    if name == 'nt':
        system('cls')

    else:
        system('clear')


def sep_line() -> None:
    print(f"{'-' * 60}")


def run_test_suite() -> None:
    """
    Função que reúne todos os testes a serem realizados no diretório
    """

    clear()

    print("Estilo:")
    subprocess.run("poetry run python -m flake8 --statistics -v",
                   shell=True, check=False)

    sep_line()

    print("\n\nAnálise estática:")
    subprocess.run("poetry run python -m mypy ./",
                   shell=True, check=False)

    sep_line()

    print("\n\nTestes unitários e cobertura:\n")
    subprocess.run("poetry run python -m pytest -v "
                   "--cov=t07 "
                   "--cov=t08 "
                   "--cov=t09 "
                   "--cov=t10 ",
                   shell=True, check=False)

    subprocess.run("poetry run python -m coverage html",
                   shell=True, check=False)

    sep_line()
