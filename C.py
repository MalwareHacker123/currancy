class CurrencyConverter:
    def __init__(self, exchange_rates=None):
        # Use provided rates if given, otherwise fall back to defaults
        self.exchange_rates = exchange_rates or {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.78,
            "JPY": 150.50,
            "INR": 83.30
        }

    def convert(self, amount, from_currency, to_currency):
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency code provided.")
            
        # Convert source currency to base (USD), then to target currency
        amount_in_usd = amount / self.exchange_rates[from_currency]
        return amount_in_usd * self.exchange_rates[to_currency]

# Usage
cash = input("how much money do you want to convert")
cashf = float(cash)
f = input("What currency do you currently have. USD, EUR, GBP ,JPY, INR ")
r = input("What currency do you want to have. USD, EUR, GBP, JPY, INR ")
print(CurrencyConverter().convert(cashf, f, r))  