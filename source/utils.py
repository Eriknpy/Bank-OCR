def read_file(file_path: str) -> list:
    with open(file_path, 'r') as f:
        lines = f.readlines()
        return [line.strip("\n") for line in lines if line.strip("\n")]


def add(n1: int, n2: int) -> int:
    return n1 + n2


def divide(n1: int, n2: int) -> float:
    return n1 / n2

