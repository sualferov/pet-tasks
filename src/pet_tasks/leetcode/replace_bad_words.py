def relace_bad_words(text: str, bad_words: str) -> str:
    """Заменяет плохие слова в предложении."""
    """
    Входная строка содержит только буквы, пробелы и символы .,!?
    """
    text_words = text.split()
    bad_words_list = bad_words.split(',')
    res_words = []

    for word in text_words:
        found_word = ''
        for bad_word in bad_words_list:
            if word.lower() == bad_word.lower():
                found_word = '#' * len(word)
                break
            if word.lower() == f'{bad_word.lower()}.':
                found_word = f'{"#" * len(bad_word)}.'
                break
            if word.lower() == f'{bad_word.lower()},':
                found_word = f'{"#" * len(bad_word)},'
                break
            if word.lower() == f'{bad_word.lower()}!':
                found_word = f'{"#" * len(bad_word)}!'
                break
            if word.lower() == f'{bad_word.lower()}?':
                found_word = f'{"#" * len(bad_word)}?'
                break

        res_words.append(found_word or word)

    return ' '.join(res_words)
