# Chapter02-01

# 변수
car_company_1 = 'Ferrari'
car_detail_1 =[
    {'color': 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

car_company_2 = 'Bmw'
car_detail_2 =[
    {'color': 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]


car_company_3 = 'Audi'
car_detail_3 =[
    {'color': 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

# 리스트
car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list =[
    {'color': 'White', 'horsepower': 400, 'price': 8000},
    {'color': 'Black', 'horsepower': 270, 'price': 5000},
    {'color': 'Silver', 'horsepower': 300, 'price': 6000}
]

del car_company_list[1]
del car_detail_list[1]

print(car_company_list)
print(car_detail_list)

# 딕셔너리
car_dicts = [
    {'car_company': 'Ferrari', 'card_detail': {'color': 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company': 'Bmw', 'card_detail': {'color': 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company': 'Audi', 'card_detail': {'color': 'Silver', 'horsepower': 300, 'price': 6000}}
]

del car_dicts[1]

print(car_dicts)


# 클래스
class Car:
    def __init__(self, company, details):
        self._company = company
        self._details = details

    def __str__(self):
        return f'str : {self._company} - {self._details}'

    def __repr__(self):
        return f'Car({repr(self._company)}, {self._details})'


car1 = Car('Ferrari', {'color': 'White', 'horsepower': 400, 'price': 8000})
car2 = Car('Bmw', {'color': 'Black', 'horsepower': 270, 'price': 5000})
car3 = Car('Audi', {'color': 'Silver', 'horsepower': 300, 'price': 6000})

print(car1)
print(car2)
print(car3)

print(car1.__dict__)
print(car2.__dict__)
print(car3.__dict__)

print(dir(car1))

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for x in car_list:
    print(x)
