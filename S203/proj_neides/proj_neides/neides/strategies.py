from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, price):
        pass

class FixedDiscount(DiscountStrategy):
    def __init__(self, discount_amount):
        self.discount_amount = discount_amount

    def apply_discount(self, price):
        return max(0, price - self.discount_amount)

class PercentageDiscount(DiscountStrategy):
    def __init__(self, discount_percentage):
        self.discount_percentage = discount_percentage

    def apply_discount(self, price):
        return price * (1 - self.discount_percentage / 100)