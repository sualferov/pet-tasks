def valid_parentheses(text: str) -> bool:
    """Проверяет корректность скобок."""
    if len(text) % 2 != 0:
        return False

    p_map = {
        ')': '(',
        ']': '[',
        '}': '{',
    }

    open_p: list[str] = []
    for p_ in text:
        if op_p := p_map.get(p_):
            curr_open = open_p.pop(-1) if open_p else None
            if op_p != curr_open:
                return False
        else:
            open_p.append(p_)

    return len(open_p) == 0
