def get_menu():
    return """\n
       1 - Просмотреть автопарк
       2 - Подсчитать общую стоимость автопарка
       3 - Вывести автомобиль с максимальной скоростью
       4 - Вывести самый дорогой автомобиль
       5 - Завершение работы программы\n
       """


class Car:
    car_count = 0  # Счетчик числа созданных автомобилей

    def __init__(self, make, model, year, price, speed):
        self.make = make
        self.model = model
        self.year = year
        self.price = price
        self.speed = speed
        Car.car_count += 1

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    @staticmethod
    def max_price(cars):
        max_price_car = max(cars, key=lambda car: car.price)
        return max_price_car

    @classmethod
    def max_speed(cls, cars):
        max_speed_car = max(cars, key=lambda car: car.speed)
        return max_speed_car


class TaxiPark:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def calculate_fleet_cost(self):
        total_cost = sum(car.price for car in self.cars)
        return total_cost


# Создаем легковые автомобили
car1 = Car("Toyota", "Camry", 2021, 25000, 180)
car2 = Car("Honda", "Civic", 2020, 22000, 200)
car3 = Car("Ford", "Focus", 2019, 18000, 170)

# Создаем таксопарк и добавляем автомобили
taxi_park = TaxiPark()
taxi_park.add_car(car1)
taxi_park.add_car(car2)
taxi_park.add_car(car3)

while True:
    print(get_menu())
    choice = input("Выберите одно из предложенных действий: ")

    if choice == '1':
        for car in taxi_park.cars:
            print(car.get_info())
    elif choice == '2':
        total_cost = taxi_park.calculate_fleet_cost()
        print(f"Общая стоимость автопарка: ${total_cost}")
    elif choice == '3':
        max_speed_car = Car.max_speed(taxi_park.cars)
        print(f"Автомобиль с максимальной скоростью: {max_speed_car.get_info()}, скорость {max_speed_car.speed} км/ч")
    elif choice == '4':
        max_price_car = Car.max_price(taxi_park.cars)
        print(f"Самый дорогой автомобиль: {max_price_car.get_info()}, стоимость ${max_price_car.price}")
    elif choice == '5':
        break
