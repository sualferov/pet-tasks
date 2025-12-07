def longest_prefix(words: list[str]) -> str:
    """Возвращает наибольший общий префикс из списка слов."""

    prefix = ''
    for i in range(min([len(w_) for w_ in words])):
        letters = list(set([word[i] for word in words]))
        if len(letters) > 1:
            return prefix
        prefix += letters[0]
    return prefix
