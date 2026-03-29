from pet_tasks.leetcode.chain_sum_function import chain_sum


def test_chain_sum_1() -> None:
    assert 1 + chain_sum(5)(4)(3) == 13
