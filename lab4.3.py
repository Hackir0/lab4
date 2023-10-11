class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")


class Pen(Stationery):
    def draw(self):
        print(f"Рисуем с помощью ручки {self.title}")


class Pencil(Stationery):
    def draw(self):
        print(f"Рисуем с помощью карандаша {self.title}")


class Handle(Stationery):
    def draw(self):
        print(f"Рисуем с помощью маркера {self.title}")


pen = Pen("синяя")
pencil = Pencil("черный")
handle = Handle("зеленый")

pen.draw()
pencil.draw()
handle.draw()
