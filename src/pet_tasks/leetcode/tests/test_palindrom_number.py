import pytest

from pet_tasks.leetcode.palindrome_number import palindrome_number, palindrome_number_v2


@pytest.mark.parametrize(
    ('number', 'exp_res'),
    [
        (121, True),
        (-121, False),
        (123321, True),
        (10, False),
    ],
)
def test_palindrome_number(number: int, exp_res: bool) -> None:
    # act
    res = palindrome_number(number=number)

    # assert
    assert res == exp_res


@pytest.mark.parametrize(
    ('number', 'exp_res'),
    [
        (121, True),
        (-121, False),
        (123321, True),
        (10, False),
    ],
)
def test_palindrome_number_v2(number: int, exp_res: bool) -> None:
    # act
    res = palindrome_number_v2(number=number)

    # assert
    assert res == exp_res
