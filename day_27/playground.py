def add(*args):
    sum = 0
    for arg in args:
        sum += arg

    return sum


print(add(1, 1, 1, 1))


def calculate(n, **kwargs):
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
        self.make = kwargs["make"]
        self.model = kwargs.get("model")



my_car = Car(make="Nissan")
print(my_car.model)