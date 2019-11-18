"""
first-class function design pattern practice
"""
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')
promos = []


def promotion(promo_func):
    promos.append(promo_func)
    return promo_func


@promotion
def fidelity_promo(order):
    """
    apply discount 5% of total price to customers who have fidelity 1,000 points
    """
    return order.total() * 0.05 if order.customer.fidelity >= 1_000 else 0


@promotion
def bulk_item_promo(order):
    """
    apply discount 10% of total price to customers who order 20 same products
    """
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * 0.1
    return discount


@promotion
def large_order_promo(order):
    """
    apply discount 7% of total price to customers who order 10 or more different kinds of products
    """
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * 0.07
    return 0


def best_promo(order):
    """
    return max discount
    """
    return max(promo(order) for promo in promos)


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
            discount = self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


if __name__ == '__main__':
    yun = Customer('yun lee', 0)
    seop = Customer('seop park', 1100)
    cart = [LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0)]
    print(Order(yun, cart, fidelity_promo))
    print(Order(seop, cart, fidelity_promo))
