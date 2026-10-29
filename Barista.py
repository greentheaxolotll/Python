class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Order:
    TAX_RATE = 0.07

    def __init__(self, receipt):
        self.receipt = receipt

    def add_item(self, item):
        self.receipt.append(item)

    def calculate_subtotal(self):
        subtotal = 0
        for item in self.receipt:
            subtotal += item.price
        return subtotal

    def calculate_taxes(self):
        return round(self.calculate_subtotal() * Order.TAX_RATE, 3)

    def calculate_total(self):
        return round(self.calculate_subtotal() + self.calculate_taxes(), 3)

    def print_receipt(self):
        print("CROSSROAD'S CAFE")
        print("----------------")
        for item in self.receipt:
            print(item.name + ": " + str(item.price))
        print("----------------")
        print("taxes: " + str(self.calculate_taxes()))
        print("----------------")
        print("Total: " + str(self.calculate_total()))

    # main() calls the misspelled name, so keep it working
    print_reciept = print_receipt


def main():

    menu = [
        MenuItem("bagel", 3.00),
        MenuItem("burrito", 5.00),
        MenuItem("ramen", 1.50),
        MenuItem("gum", 0.50)
    ]

    order1 = Order([])
    order1.add_item(menu[1])
    order1.add_item(menu[1])
    order1.add_item(menu[3])

    total = order1.calculate_total()
    print("The total due is " + str(total))

    order1.print_reciept()


if __name__ == '__main__':
    main()