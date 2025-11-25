import pytest

from pet_tasks.leetcode.replace_bad_words import relace_bad_words


@pytest.mark.parametrize(
    ('text', 'bad_words', 'exp_text'),
    [
        (
            'Кот, из-за которого пришлось купить новую посуду',
            'кот,новую',
            '###, из-за которого пришлось купить ##### посуду',
        ),
        (
            'Книга не показалась ему особенно занимательной, модерну он предпочитал постмодерн.',
            'модерн,книга,особенно',
            '##### не показалась ему ######## занимательной, модерну он предпочитал постмодерн.',
        ),
    ],
)
def test_replace_bad_words(text: str, bad_words: str, exp_text: str) -> None:
    # act
    res = relace_bad_words(text=text, bad_words=bad_words)

    # assert
    assert res == exp_text
