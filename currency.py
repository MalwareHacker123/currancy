class CurrencyConverter:
    def __init__(self, exchange_rates=None):
        self.exchange_rates = exchange_rates or {
            "USD": 1.0,
            "EUR": 0.92,
            "GBP": 0.78,
            "JPY": 150.50,
            "INR": 83.30
        }

    def convert(self, amount, from_currency, to_currency):
        if amount <= 0:
            raise ValueError("NO")
        if from_currency not in self.exchange_rates or to_currency not in self.exchange_rates:
            raise ValueError("Invalid currency provided stupid.")
            
        amount_in_usd = amount / self.exchange_rates[from_currency]
        return amount_in_usd * self.exchange_rates[to_currency]

        return round(result, 2)

    def add_rate(self, currency, rate):
        self.exchange_rates[currency] = rate


# Protect interactive prompts from running during pytest imports
if __name__ == "__main__":
    cash = input("how much money do you want to convert: ")
    cashf = float(cash)
    f = input("What currency do you currently have (USD, EUR, GBP, JPY, INR): ").strip().upper()
    r = input("What currency do you want to have (USD, EUR, GBP, JPY, INR): ").strip().upper()
    
    result = CurrencyConverter().convert(cashf, f, r)
    print(f"Converted amount: {result}")