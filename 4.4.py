class Cars:
    count = 0
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        Cars.count += 1

    def get_info(self):
        return f"Бренд:{self.brand}, Модель:{self.model},  Цвет: {self.color}"

    @staticmethod
    def get_count():
        return Cars.count

    @classmethod
    def updata_count(cls, new_count):
        Cars.count = new_count

car1 = Cars(input("Введите бренд первой машины "),input("Введите модель первой машины "), input("Введите цвет первой машины "))
car2 = Cars(input("Введите бренд второй машины "),input("Введите модель второй машины "),input("Введите цвет второй машины "))
car3 = Cars(input("Введите бренд третьей машины "), input("Введите модель третьей машины "),input("Введите цвет третьейй машины "))
print(car1.get_info())
print(car2.get_info())
print(car3.get_info())
print(Cars.get_count())
Cars.updata_count(5)
print(Cars.get_count())