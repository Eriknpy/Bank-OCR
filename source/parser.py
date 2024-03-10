def text_to_number(lines: list[str]):
    result = []
    for i in range(len(lines)):
        if i == 0:
            result.append(lines[i])

    print(result)