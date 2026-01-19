def compress_runs(text: str) -> str:
    result = ""
    count = 0
    current = text[0]
    for t in text:
        if current == t:
            count += 1
        else:
            result += str(count) + current
            count = 1
        current = t
    result += str(count) + current
    return result
