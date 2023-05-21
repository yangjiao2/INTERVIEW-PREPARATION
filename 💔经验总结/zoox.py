class OperationalCost():
    def __init__(self, flat ={
    "economy": 0, "premium": 25, "business": 50,
   }, extra = {
    "economy": 0, "premium": 0, "business": 0.25,
   }):
        self.flat = flat
        self.extra = extra

    def update_flat(self, key, value):
        if key in self.flat:
            self.flat[key] = value

    def update_extra(self, key, value):
        if key in self.extra:
            self.extra[key] = value

    def get_flat(self):
        return self.flat

    def get_extra(self):
        return self.extra

class Airline():
    def __init__(self, airline_name, rate = 0, basic = 0, oc = OperationalCost()):
        self.name = airline_name
        self.rate = rate
        self.basic = basic
        self.oc = oc

    # def setAirline(airline):
    #     self.name = airline_name

    # def setOc(oc):
    #     self.oc = oc

    def get_base_price(self, ):
        return self.oc.base_price if self.oc is not None else None

    def get_additional_price(self, ):
        return self.oc.additional if self.oc is not None else None

    def calculate_price(self, miles, seat):
        price = self.basic + self.rate * miles
        if self.oc is not None:
            flat_cost =  self.oc.get_flat()[seat]
            extra_cost = self.oc.get_extra()[seat]*miles
            oc_cost = flat_cost + extra_cost

            price += oc_cost
        return price


class Delta(Airline):
    def __init__(self, name="delta", rate = 0.5):
        super().__init__(name, rate)
        # self.name = name


class United(Airline):
    def __init__(self, name="united", rate = 0.75):
        super().__init__(name, rate)
        # self.name = name
        self.oc.update_extra("premium", self.oc.get_extra()["premium"] + 0.10)


class Southwest(Airline):
    def __init__(self, name="united", rate = 1, basic = 0, oc = None):
        super().__init__(name, rate)


class LuigiAir(Airline):
    def __init__(self, name="luigiAir", rate= 0, basic = 100,):
        super().__init__(name, rate, 100,)
        # self.name = name

    def calculate_price(self, miles, seat):
        oc_cost = self.oc.get_flat()[seat] + self.oc.get_extra()[seat]*miles
        return max(100, 2* oc_cost)



class Ticket():
    def __init__(self, airline_name, seat, miles):
        self.airline_name = airline_name
        self.seat = seat.lower()
        self.miles = miles
        self.airline = self._construct_airline()

    def _construct_airline(self):
        if self.airline_name == "United":
            return United(self.airline_name)
        elif self.airline_name == "LuigiAir":
            return LuigiAir(self.airline_name)
        elif self.airline_name == "Delta":
            return Delta(self.airline_name)
        elif self.airline_name == "Southwest":
            return Southwest(self.airline_name)
        else:
            raise KeyError("error")

    def calcuate_ticket_cost(self):
        return self.airline.calculate_price(self.miles, self.seat)

test_input = [
"United 150.0 Premium","Delta 60.0 Business","Southwest 1000.0 Economy","LuigiAir 50.0 Business"
]


tickets = []
for line in test_input:
    airline_name, miles, seat = line.split(" ")
    print (airline_name, miles, seat)

    tickets.append(Ticket(airline_name, seat, float(miles)))

print (len(tickets))
for t in tickets:
    print (t.airline_name, t.calcuate_ticket_cost())




----


'''
# Airline Ticket Price Calculator

You're building a tool to calculate the cost of various airplane tickets based on the airline, distance and seating class. Your tool must take in this information as a series of inputs (one ticket calculation per line of input) and produce a list of output costs.

Each airline contains its own cost requirements. Ultimately, the airline is only interested in two major components: the space (seating class) you take on the plane, and the distance you fly. You must generate ticket costs using this gathered data:

Airlines: United, Delta, Southwest, American

## Operating Costs
```
 - Economy:  $0
 - Premium:  $0.10/mile up to a maximum of $25
 - Business: $50 + $0.25/mile
```

## Per-Airline Prices
```
 - United charges $0.50/mile
   + OperatingCost

 - Delta charges $0.9/mile

 - Southwest charges $0.75/mile
   + OperatingCost
   + $0.10/mile for Premium seats

 - American charges the average of 2 * OperatingCost and $1/mile
```

Keep in mind that, while there are only four airlines listed above, your solution should be able to expand to dozens of individual airlines,  whose ticket cost can be based on arbitrary functions of "Operating Costs", miles, and/or seating class.

You can assume that the input will be provided as a list of strings and that there could be millions of lines of input. Each string will provide the Airline, Distance and Seating Class. Please review the examples below:

## Example Input
```
United 150.0 Business
Delta 60.0 Economy
Southwest 1000.0 Premium
American 95.0 Business
```

## Example Output:
```
162.50
54.00
875.00
121.25
```



## Operating Costs
```
 - Economy:  $0
 - Premium:  $0.10/mile up to a maximum of $25
 - Business: $50 + $0.25/mile
```

### Explanation of Output:
```
162.50      (150.0 * (0.5 + 0.25) + 50)
54.00       (60.0 * (0.9))
875.00      (1000.0 * (0.75 + 0.1) + min(25, 1000.0 * .1))
121.25      (((2 * (50 + 0.25 * 95.0)) + (1 * 95.0)) / 2.0)
```

 - United charges $0.50/mile
   + OperatingCost

 - Delta charges $0.9/mile

 - Southwest charges $0.75/mile
   + OperatingCost
   + $0.10/mile for Premium seats

 - American charges the average of 2 * OperatingCost and $1/mile


'''

test_input = [
    "United 150.0 Business",
    "Delta 60.0 Economy",
    "Southwest 1000.0 Premium",
    "American 95.0 Business"
]

class OperatingCost():
    def __init__(self, flat = {
        "Economy": 0,
        "Premium": 0,
        "Business": 50

    }, extra= {
        "Economy": 0,
        "Premium": 0.1,
        "Business": 0.25
    }):
        self.flat = flat
        self.extra = extra

    def get_flat(self):
        return self.flat

    def get_extra(self):
        return self.extra


class Airline():
    def __init__(self, airline_name, rate, oc = None):
        self.airline_name = airline_name
        self.rate = rate
        self.oc = oc


    def calculate_price(self, miles, seat):
        price = self.rate * miles

        if self.oc is not None:
            flat_cost = self.oc.get_flat()[seat]
            if seat == "Premium":
                extra_cost = min(25, self.oc.get_extra()[seat] * miles)
            else:
                extra_cost = self.oc.get_extra()[seat] * miles
            print (price, flat_cost, extra_cost)
            return price + flat_cost + extra_cost

#  - United charges $0.50/mile
#    + OperatingCost

class United(Airline):
    def __init__(self, name="United", rate=0.5, oc = OperatingCost()):
        super().__init__(name, rate, oc)



#  - Delta charges $0.9/mile

class Delta(Airline):
    def __init__(self, name="United", rate=0.9):
        super().__init__(name, rate)


    def calculate_price(self, miles, seat):
        return self.rate * miles

#          - Southwest charges $0.75/mile
#    + OperatingCost
#    + $0.10/mile for Premium seats

#  - Economy:  $0
#  - Premium:  $0.10/mile up to a maximum of $25
#  - Business: $50 + $0.25/mile
class Southwest(Airline):
    def __init__(self, name="Southwest", rate=0.75):
        oc = OperatingCost(
        flat = {
        "Economy": 0,
        "Premium": 0,
        "Business": 50

    }, extra= {
        "Economy": 0,
        "Premium": 0.1,
        "Business": 0.25
    }
        )
        super().__init__(name, rate, oc)

# 875.00      (1000.0 * (0.75 + 0.1) + min(25, 1000.0 * .1))
# $0.10/mile up to a maximum of $25
    # def calculate_price(self, miles, seat):
    #     price = self.rate * miles

    #     if self.oc is not None:
    #         flat_cost = self.oc.get_flat()[seat]
    #         print (seat)
    #         if seat == "Premium":
    #             extra_cost = min(25, self.oc.get_extra()[seat] * miles)
    #         else:
    #             extra_cost = self.oc.get_extra()[seat] * miles
    #         print (price, flat_cost, extra_cost)
    #         return price + flat_cost + extra_cost


# 121.25      (((2 * (50 + 0.25 * 95.0)) + (1 * 95.0)) / 2.0)

#  - American charges the average of 2 * OperatingCost and $1/mile
class American(Airline):
    def __init__(self, name="American", rate=0.1, oc = OperatingCost()):
        super().__init__(name, rate, oc)


    def calculate_price(self, miles, seat):
        if self.oc is not None:
            flat_cost = self.oc.get_flat()[seat]
            if seat == "Premium":
                extra_cost = min(25, self.oc.get_extra()[seat] * miles)
            else:
                extra_cost = self.oc.get_extra()[seat] * miles

            price = 1/2 * (self.rate * miles +  2 * (flat_cost + extra_cost))
            return price


if __name__ == "__main__":

    ## improvement
    airline_dict = {
        "United": United("United")
    }
    for line in test_input:
        airline_name, miles, seat = line.split(" ")
        if airline_name == "United":
            airline = United(airline_name)
        elif airline_name == "Delta":
            airline = Delta(airline_name)
        elif airline_name == "Southwest":
            airline = Southwest(airline_name)
        elif airline_name == "American":
            airline = American(airline_name)
        print (airline_name, airline.calculate_price(float(miles), seat))

        ##

    print("Hello, candidate!")
