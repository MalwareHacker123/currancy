import pytest
from currency import CurrencyConverter

@pytest.fixture
def converter():
    exchange_rates = {
        "USD": 1.0,
        "EUR": 0.92,
        "GBP": 0.78,
        "JPY": 150.50,
        "INR": 83.30
    }
    return CurrencyConverter(exchange_rates)

def test_same_currency_conversion(converter):
    assert converter.convert(100, "USD", "USD") == 100.0

def test_usd_to_eur_conversion(converter):
    assert converter.convert(100, "USD", "EUR") == 92.0

def test_invalid_currency_raises_error(converter):
    with pytest.raises(ValueError):
        converter.convert(100, "INVALID", "USD")