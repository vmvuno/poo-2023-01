import os
import subprocess


def get_line_count() -> None:
    subprocess.run(
        'poetry run pygount --suffix=py '
        '--folders-to-skip=scripts --format=summary '
        f'{os.getcwd()}',
        shell=True,
        check=True
    )
