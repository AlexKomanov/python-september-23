import pytest


def test_one_and_one():
    num_1 = 1
    num_2 = 1
    result = 2
    print(f"\nResult is {num_2 + num_1}")  # requires -s flag
    assert num_1 + num_2 == result


def test_five_minus_one():
    num_1 = 5
    num_2 = 1
    result = 4
    assert num_1 - num_2 == result


@pytest.mark.regression
def test_five_divided_by_zero():
    with pytest.raises(Exception) as exception:
        num_1 = 5
        num_2 = 0
        res = num_1 / num_2 == 0

    assert exception.typename == 'ZeroDivisionError'
    assert str(exception.value) == 'division by zero'


test_data = [(1, 5, 6), (10, 5, 15), (1, 0, 1), (20, 40, 60), (10, 500, 510)]


@pytest.mark.parametrize("num_1, num_2, result", test_data)
def test_sum_parameters(num_1, num_2, result):
    assert num_1 + num_2 == result
