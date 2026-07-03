import pytest

from pet_tasks.leetcode.longest_prefix import longest_prefix


@pytest.mark.parametrize(
    ('words', 'exp_res'),
    [
        (['flower', 'flow', 'flight'], 'fl'),
        (['dog', 'racecar', 'car'], ''),
        (['a'], 'a'),
    ],
)
def test_longest_prefix(words: list[str], exp_res: str) -> None:
    assert longest_prefix(words) == exp_res
