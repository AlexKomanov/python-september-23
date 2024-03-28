import pytest
from source.accumulator import Accumulator


@pytest.fixture
def accumulator_2():
    return Accumulator(1)
