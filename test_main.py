import main
import pytest


@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, 1),
        (1, 0, 1),
        (1, 1, 2),
    )
)
def test_foo(x, y, expected):
    assert main.foo(x, y) == expected
@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, 2),
        (1, 0, 2),
        (1, 1, 3),
    )
)
def test_bar(x, y, expected):
    assert main.bar(x, y) == expected
@pytest.mark.parametrize(
    ("x", "y", "expected"),
    (
        (0, 0, 1),
        (1, 0, 1),
        (2, 3, 8),
    )
)
def test_baz(x, y, expected):
    assert main.baz(x, y) == expected