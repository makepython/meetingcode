# add strategy bank example

class NoDiscountStrategy:
    def apply(self, price):
        return price


class DiscountStrategy:
    def __init__(self, rate):
        self._rate = rate
    def apply(self, price):
        return price * self._rate


class Bill:
    def __init__(self, customer):
        self._customer = customer
        self._total = 0.0
        self.discount_strategy = NoDiscountStrategy()

    def charge(self, amount):
        self._total += self.discount_strategy.apply(amount)

    def invoice(self):
        print(f"{self._customer}: {self._total}")


bill = Bill("Gates")
bill.charge(100)
bill.invoice()
bill.discount_strategy = DiscountStrategy(0.8)
bill.charge(100)
bill.invoice()

