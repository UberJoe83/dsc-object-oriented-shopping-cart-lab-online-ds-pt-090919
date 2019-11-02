class ShoppingCart:
    # write your code here
    
    def __init__(self, emp_discount=None):
        self.total = 0
        self.employee_discount = emp_discount
        self.items = []
        
    def add_item(self, name, price, quantity=1):
        for x in list(range(quantity)):
            self.items.append({"name": name, "price": price})
            self.total += price
        return self.total
       
    def mean_item_price(self):
        num_items = len(self.items)
        total = self.total
        mean = total/num_items
        return mean      

    def median_item_price(self):
        prices = [item["price"] for item in self.items]
        length = len(prices)
        if (length % 2 == 0):
            mid_1 = int(length/2)
            mid_2 = mid_1 - 1
            median = (prices[mid_1] + prices[mid_2]) / 2
            return median
        mid = int(length / 2)
        return prices[mid]

    def apply_discount(self):
        if self.employee_discount:
            discount = self.employee_discount / 100
            dis_tot = self.total * (1 - discount)
            return dis_tot
        else:
            return "Sorry, there is no discount to apply to your cart."

    def void_last_item(self):
        if self.items:
            out_item = self.items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= out_item["price"]