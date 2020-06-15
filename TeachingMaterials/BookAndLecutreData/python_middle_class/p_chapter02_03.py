class Car:
    """
    Car Class
    Author: Kim
    Date: 20.06.15.
    Description: Class, Static, Instance Method
    """
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'str : {self._company} - {self._details}'

    def __repr__(self):
        return f'Car({repr(self._company)}, {self._details})'

    def detail_info(self):
        print(f'Current ID: {id(self)}')
        print(f'Car Detail Info: {self._company} {self._details.get("price")}')

    def get_price(self):
        return f'Before Car Price -> Company: {self._company}, price: {self._details.get("price")}'

    def get_price_calc(self):
        return f'After Car Price -> Company: {self._company}, price: {self._details.get("price") * Car.price_per_raise}'

    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 Or More')
            return
        cls.price_per_raise = per
        print('Succeed! price increased')

    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return f'OK! This car is {inst._company}'
        return 'Sorry. This car is not Bmw'


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})

car1.detail_info()
car2.detail_info()

print(car1._details.get('price'))
print(car2._details.get('price'))

print(car1.get_price())
print(car2.get_price())

Car.price_per_raise = 1.4
print(car1.get_price_calc())
print(car2.get_price_calc())

Car.raise_price(1)
Car.raise_price(1.6)
print(car1.get_price_calc())
print(car2.get_price_calc())

print(car1.is_bmw(car1))
print(car2.is_bmw(car2))

print(Car.is_bmw(car1))
print(Car.is_bmw(car2))
