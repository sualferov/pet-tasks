import pytest

from pet_tasks.leetcode.valid_parentheses import valid_parentheses


@pytest.mark.parametrize(
    ('text', 'exp_res'),
    [
        ('(', False),
        ('()', True),
        ('()[]{}', True),
        ('(]', False),
        ('([])', True),
        ('([)]', False),
        ('((', False),
        ('){', False),
    ],
)
def test_valid_parentheses(text: str, exp_res: bool) -> None:
    assert valid_parentheses(text) == exp_res
