from source.accumulator import Accumulator
import pytest


@pytest.fixture()
def accumulator():
    return Accumulator()


@pytest.mark.sanity
def test_accumulator_init(accumulator_2, accumulator):
    assert accumulator_2.count == 1
    assert accumulator.count == 0


@pytest.mark.regression
def test_accumulator_add_one(accumulator):
    accumulator.add_accumulators()
    assert accumulator.count == 1


@pytest.mark.regression
def test_accumulator_one_add_three(accumulator):
    accumulator.add_accumulators()
    accumulator.add_accumulators(3)
    with pytest.raises(AssertionError) as exception:
        assert accumulator.count == 3

    assert exception.typename == 'AssertionError'


@pytest.mark.sanity
def test_accumulator_add_five(accumulator):
    accumulator.add_accumulators(5)
    assert accumulator.count == 5


@pytest.mark.regression
def test_accumulator_add_ten(accumulator):
    accumulator.add_accumulators(10)
    assert accumulator.count == 10
