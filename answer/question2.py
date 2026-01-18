def fizzbuzz_custom(n: int, rules: list[tuple[int, str]]) -> list[str]:
    result_list: list[str] = []
    for i in range(1, n + 1):
        result = ""
        for div, label in rules:
            if i % div == 0:
                result += label

        if not result:
            result = str(i)
        result_list.append(result)
    return result_list
