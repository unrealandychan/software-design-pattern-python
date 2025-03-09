# Open Close Principle
# A class should be open for extension but closed for modification

# Wrong Example
class DiscountCalculator:
    @staticmethod
    def apply_discount(total: float, discount_type: str) -> float:
        if discount_type == "Christmas":
            return total * 0.5
        elif discount_type == "Easter":
            return total * 0.2
        elif discount_type == "New Year":
            return total * 0.3
        else:
            return total


# It seems that the above code is correct, but it violates the Open Close Principle. The above code violates the Open
# Close Principle because if we want to add a new discount type, we have to modify the class.
calculator = DiscountCalculator()
print(calculator.apply_discount(100, "Christmas"))
print(calculator.apply_discount(100, "Easter"))
print(calculator.apply_discount(100, "New Year"))


# Right Example
class Discount:
    def apply_discount(self, total: float) -> float:
        return total


class ChristmasDiscount(Discount):
    def apply_discount(self, total: float) -> float:
        return total * 0.5


class EasterDiscount(Discount):
    def apply_discount(self, total: float) -> float:
        return total * 0.2


class NewYearDiscount(Discount):
    def apply_discount(self, total: float) -> float:
        return total * 0.3


class DiscountCalculatorNew:

    def __init__(self, discount: Discount):
        self.discount = discount

    def apply_discount(self, total: float) -> float:
        return self.discount.apply_discount(total)


discount = ChristmasDiscount()
calculator = DiscountCalculatorNew(discount)
print(calculator.apply_discount(100))

discount = EasterDiscount()
calculator = DiscountCalculatorNew(discount)
print(calculator.apply_discount(100))

discount = NewYearDiscount()
calculator = DiscountCalculatorNew(discount)
print(calculator.apply_discount(100))
