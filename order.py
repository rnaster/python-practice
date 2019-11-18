"""
first-class function design pattern practice
"""
from abc import ABC, abstractmethod
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.__total = -1

    def total(self):
        self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        discount = 0
        if self.promotion is not None:
            discount = self.promotion.discount(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


class Promotion(ABC):

    @abstractmethod
    def discount(self, order):
        """
        apply discount to price
        """
        pass


class FidelityPromo(Promotion):
    """
    apply discount 5% of total price to customers who have fidelity 1,000 points
    """

    def discount(self, order):
        return order.total() * 0.05 if order.customer.fidelity >= 1_000 else 0


class BulkItemPromo(Promotion):
    """
    apply discount 10% of total price to customers who order 20 same products
    """

    def discount(self, order):
        discount = 0
        for item in order.cart:
            if item.quantity >= 20:
                discount += item.total() * 0.1
        return discount


class LargeOrderPromo(Promotion):
    """
    apply discount 7% of total price to customers who order 10 or more different kinds of products
    """

    def discount(self, order):
        distinct_items = {item.product for item in order.cart}
        if len(distinct_items) >= 10:
            return order.total() * 0.07
        return 0


if __name__ == '__main__':
    yun = Customer('yun lee', 0)
    seop = Customer('seop park', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]
    print(Order(yun, cart, FidelityPromo()))
    print(Order(seop, cart, FidelityPromo()))
