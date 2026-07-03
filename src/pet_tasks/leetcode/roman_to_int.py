def roman_to_int(roman_number: str) -> int:
    """Переводит римские цифры в int."""
    roman_map = {
        'i': 1,
        'v': 5,
        'iv': -1,
        'x': 10,
        'ix': -1,
        'l': 50,
        'xl': -10,
        'c': 100,
        'xc': -10,
        'd': 500,
        'cd': -100,
        'm': 1000,
        'cm': -100,
    }

    res_number = 0
    prev = None
    for roman in roman_number.lower()[::-1]:
        res_number += (roman_map.get(f'{roman}{prev}', 0) or roman_map.get(roman, 0))
        prev = roman

    return res_number
