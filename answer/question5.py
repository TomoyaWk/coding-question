def is_balanced(text: str) -> bool:
    stack: list[str] = []
    brac: dict = {"[": "]", "{": "}", "(": ")"}
    for t in list(text):
        if t in brac.keys():
            # 開きカッコ
            stack.append(t)
        elif t in brac.values():
            # 閉じカッコのとき
            # スタックの一番上が対応していなければFalse
            # スタックが空ならFalse
            if len(stack) == 0 or t != brac.get(stack[-1]):
                return False
            else:
                # 正しく対応した開きカッコは取り除く
                stack.pop()
    if len([s for s in stack if s in brac.keys()]) > 0:
        return False
    return True
