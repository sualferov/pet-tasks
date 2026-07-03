def longest_prefix(words: list[str]) -> str:
    """Возвращает наибольший общий префикс из списка слов."""
    prefix = ''
    for i in range(min(len(w_) for w_ in words)):
        letters: list[str] = [l_[0] for l_ in {word[i] for word in words}]
        if len(letters) > 1:
            return prefix
        prefix += letters[0]
    return prefix
