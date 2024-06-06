class Coffee:
    def __init__(self, name):
        self.name = name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        #else:
         #   raise Exception
    def orders(self):
        return [order for order in Order.all if order.coffee == self]
    
    def customers(self):
        return list({order.customer for order in self.orders()})
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        return sum([order.price for order in self.orders()]) / self.num_orders()

class Customer:
    all=[]
    def __init__(self, name):
        self.name = name
        type(self).all.append(self)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1<=len(value)<=15:
            self._name = value
        #else:
         #   raise Exception
    def orders(self):
        return [order for order in Order.all if order.customer is self]
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def create_order(self, coffee, price):
        return Order(self, coffee, price)
    
class Order:
        all=[]
        def __init__(self, customer, coffee, price):
            self.customer = customer
            self.coffee = coffee
            self.price = price
            type(self).all.append(self)
        @property
        def price(self):
            return self._price
        @price.setter
        def price(self, value):
            if (isinstance(value,float)and 1.0<=value<=10.0) and not hasattr(self,"price"):
                self._price = value
            #else:
             #   raise Exception
        @property
        def customer(self):
            return self._customer
        @customer.setter
        def customer(self, value):
            if isinstance(value, Customer):
                self._customer = value
            #else:
             #   raise Exception
        @property
        def coffee(self):
            return self._coffee
        @coffee.setter
        def coffee(self, value):
            if isinstance(value, Coffee) :
                self._coffee = value
            #else:
            #   raise Exception