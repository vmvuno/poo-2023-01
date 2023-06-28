def soma_naturais(n: int) -> int:
    c = 1
    s = 0
    while c <= n:
        s += c
        c += 1

    return s


if __name__ == "__main__":
    print(soma_naturais(5))  # pragma: no cover
