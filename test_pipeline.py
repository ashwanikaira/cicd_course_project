import pytest
from pipeline import clean_amount, total_revenue


def test_clean_amount_rounds_correctly():
    assert clean_amount(10.456) == 10.46


def test_clean_amount_rejects_negative():
    with pytest.raises(ValueError):
        clean_amount(-5)


def test_total_revenue_sums_correctly():
    assert total_revenue([100, 200.5, 50]) == 350.5