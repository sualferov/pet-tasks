import pytest

from pet_tasks.leetcode.roman_to_int import roman_to_int


@pytest.mark.parametrize(
    ('roman', 'exp_res'),
    [
        ('III', 3),
        ('VIII', 8),
        ('LVIII', 58),
        ('IV', 4),
    ],
)
def test_roman_to_int(roman: str, exp_res: int) -> None:
    assert roman_to_int(roman) == exp_res
