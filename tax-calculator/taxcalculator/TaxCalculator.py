# coding: UTF-8
class calculator():

    def __init__(self):
        print 'Initializing calculator class...'
        self.price = raw_input("Please enter price: ")
        self.quantity = raw_input("Please enter quantity: ")
        self.state = raw_input("Please enter state: ").upper()

    def calculate_total_price(self, price, quantity, state):
        tax_list = {"UT" : 1.0685, "NV" : 1.08, "TX" : 1.0625, "AL" : 1.04, "CA" : 1.0825}

        while state not in tax_list:
            print "Inserted state is not correct! Please try again."
            print "Correct state values are: "
            for key, value in tax_list.iteritems():
                print key

            self.state = raw_input("Please enter state: ").upper()
            state = self.state
        else:
            tax = tax_list.get(state)

        try:
            total_price = int(price) * int(quantity) * tax;
            return total_price;
        except ValueError:
            print "ERROR 404 - Price or quantity is invalid!"
            quit()

    def calc_price_with_discount(self, total_price):
        if (total_price > 50000):
            discount = 0.85
        elif (total_price > 10000):
            discount = 0.90
        elif (total_price > 7000):
            discount = 0.93
        elif (total_price > 5000):
            discount = 0.95
        elif(total_price > 1000):
            discount = 0.97
        else: discount = 1

        price_with_discount = float(total_price) * discount;

        print "Total price with tax and discounts is: " + str(price_with_discount) + " euros";

if __name__ == "__main__":
    calculator = calculator()
    total_price = calculator.calculate_total_price(calculator.price, calculator.quantity, calculator.state)
    calculator.calc_price_with_discount(total_price)

