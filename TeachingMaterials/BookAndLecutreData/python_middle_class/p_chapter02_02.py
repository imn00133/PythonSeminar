class Car:
    """
    Car Class
    Author: Kim
    Date: 20.06.13.
    """
    car_count = 0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        Car.car_count += 1

    def __str__(self):
        return f'str : {self._company} - {self._details}'

    def __repr__(self):
        return f'Car({repr(self._company)}, {self._details})'

    def __del__(self):
        Car.car_count -= 1

    def detail_info(self):
        print(f'Current ID: {id(self)}')
        print(f'Car Detail Info: {self._company} {self._details.get("price")}')


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(id(car1))
print(id(car2))
print(id(car3))

print(car1._company == car2._company)
print(car1 is car2)

print(dir(car1))
print(dir(car2))

print(car1.__dict__)
print(car2.__dict__)

print(Car.__doc__)
# help(Car)

car1.detail_info()
Car.detail_info(car1)
car2.detail_info()
Car.detail_info(car2)

# 에러
# Car.detail_info()

print(car1.__class__, car2.__class__)
print((id(car1.__class__), id(car2.__class__)))

print(car1.car_count)
print(car2.car_count)
print(car1.__dict__)
print(car2.__dict__)

print(dir(car1))

print(car1.car_count)
print(Car.car_count)

del car2
print(car1.car_count)
print(Car.car_count)
