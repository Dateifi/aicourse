import pytest


@pytest.mark."something" for pytest -v -m "something"

@pytest.mark.skip(reason="no way of currently testing this") skipif(logic, reason)

@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42),])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

@pytest.fixture(scope="module")
def sample_persons():
    yield [Person("John", "Doe", 35), Person("Jane", "Doe", 34), Person("John", "Smith", 35), Person("Jane", "Smith", 34)]
    close connection

