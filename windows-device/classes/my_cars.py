from car import Car, ElectricCar # or we can import entire car module by 'impot car' and access classes by its module name. for say, car.ElectricCar('tesla', 'roadster', 2016)

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())