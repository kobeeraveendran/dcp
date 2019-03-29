class Log:

    def __init__(self, n):
        self.orders = []
        self.size = n

    def record(self, order_id):
        self.orders.append(order_id)

    def get_last(self, i):
        return self.orders[self.size - i]


test1 = Log(3)
test1.record(1234)
test1.record(8936)
test1.record(7925)

print(test1.orders)
print(test1.get_last(1))
print(test1.get_last(2))
print(test1.get_last(3))
