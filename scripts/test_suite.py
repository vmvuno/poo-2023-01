import subprocess
import os
import re


def clear() -> None:
    if os.name == 'nt':
        os.system('cls')

    else:
        os.system('clear')


def sep_line() -> None:
    print(f"{'-' * 60}")


def run_style_analysis() -> None:
    print("Análise de conformidade à PEP8 (estilo):")
    subprocess.run("poetry run python -m flake8 --statistics -v",
                   shell=True, check=False)


def run_static_analysis() -> None:
    print("\n\nAnálise estática:")
    subprocess.run("poetry run python -m mypy ./",
                   shell=True, check=False)


def run_tests_and_coverage_analysis() -> None:
    cwd: str = os.getcwd()

    t_folders: list[str] = []
    for file in os.listdir():
        if os.path.isdir(os.path.join(cwd, file)) \
                and re.match(r"t\d{1,2}", file):
            t_folders.append(file)

    print("\n\nTestes unitários e cobertura:\n")

    subprocess.run("poetry run python -m pytest -v --cov=" +
                   " --cov=".join(sorted(t_folders)),
                   shell=True, check=False)

    subprocess.run("poetry run python -m coverage html",
                   shell=True, check=False)


def run_test_suite() -> None:
    """
    Função que reúne todos os testes a serem realizados no diretório
    """
    run_style_analysis()
    sep_line()

    run_static_analysis()
    sep_line()

    run_tests_and_coverage_analysis()
    sep_line()
