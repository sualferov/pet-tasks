def palindrome_number(number: int) -> bool:
    """Определяет, является ли число палиндромом."""
    str_number = str(number)

    for i, left_digit in enumerate(str_number):
        right_digit = str_number[-1:] if i == 0 else str_number[-i - 1:-i]
        digits_length = len(str_number)
        is_equal = left_digit == right_digit
        if digits_length % 2 == 0 and i + 1 >= digits_length // 2:
            return is_equal
        if digits_length % 2 != 0 and i >= digits_length // 2:
            return True

        if not is_equal:
            return False

    return True


def palindrome_number_v2(number: int) -> bool:
    """Определяет, является ли число палиндромом."""
    return str(number) == str(number)[::-1]
