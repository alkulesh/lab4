class Stationery:
    def __init__(self, title):
        self.title = title
    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationery):
    def draw(self):
        print("Нарисовать ручкой")
class Pencil(Stationery):
    def draw(self):
        print("Нарисовать карандашем")
class Handle(Stationery):
    def draw(self):
        print("Нарисовать маркером")

pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")
pen.draw()
pencil.draw()
handle.draw()
